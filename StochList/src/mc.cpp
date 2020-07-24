// Stochastic lists: Sampling multi-variable functions with population methods
// Copyright (C) 2018  Lode Pollet

// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.


#include "mc.h"
#include <iomanip>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <string>
#include <bitset>

int main() {
  int is_continue, is_keepstat;
  MC sim;
  time(&sim.times1);
  sim.times_tot = 0;
  sim.times_overall = 0;
  sim.Nwrite_cur = 10;
  
  enum {WRITE, MEASURE, LIST };
  vector<size_t> counter(LIST + 1, 0);
 
  sim.print_copyright(std::cout);
 
  
  ifstream inseed("params");
  if (inseed.fail()) {
    std::cerr << "Unable to open params\n";
    exit(1);
  }
  string s;
  inseed >> sim.seed; getline(inseed,s);
  inseed >> is_continue; getline(inseed,s);
  inseed >> is_keepstat; getline(inseed, s);
  inseed >> sim.Nlen_init; getline(inseed,s);
  inseed >> sim.Nlist_max; getline(inseed,s);
  inseed >> sim.kappa; getline(inseed, s);
  inseed >> sim.Gutzwiller_b; getline(inseed,s);
  inseed >> sim.times_runtime; getline(inseed,s);
  inseed.close();
  sim.MyGenerator.seed(sim.seed);
  // initialize
  
  sim.init();
  
  cout << setprecision(15);
  if (is_continue) {
    std::cout << "# Reading old configuration\n";
    ifstream inconf("qc_conf");
    sim.load(inconf);
    inconf.close();
    if (!is_keepstat) {
      std::cout << "# Resetting statistics\n";
      sim.reset_statistics();
    }
  }
  std::cout << "Start main loop!" << std::endl;
  
  do {
    sim.do_step();
    counter[WRITE]++;
    counter[MEASURE]++;
    counter[LIST]++;

    if (counter[WRITE] >= sim.Nwrite_cur) {
    //if (counter[WRITE] >= sim.Nwrite) {
      double eval = (sim.MCmeas_one * 1. / sim.MCmeas_zero * sim.weight_fake - sim.shift) / sim.Nsites;
      cout << "eigenvalue : " << sim.MCsteps+1.0 << "\t" << eval << "\t length : " << sim.Nlen << "\t target :  " << static_cast<size_t>(sqrt(sim.MCsteps/1.)) << "\n";
      sim.conv_log.push_back(pair<double, double>(log(sim.MCsteps+1.0), eval ));
      //sim.print_update_statistics(cout);
      sim.Nwrite_cur = sim.Nwrite_cur * 10;
      if (sim.Nwrite_cur > sim.Nwrite) sim.Nwrite_cur = sim.Nwrite;
      //sim.print_update_statistics(cout);
      counter[WRITE]=0;
      time(&sim.times2);
      sim.dtimes = sim.times2 - sim.times1;
      sim.times1 = sim.times2;
      sim.times_tot += sim.dtimes;
      sim.times_overall += sim.dtimes;
      if (sim.times_tot + 2*sim.dtimes > sim.times_runtime ) {
        cout << "\nApproaching run time limit.\n";
        ofstream outstat("qc_updates");
        sim.print_update_statistics(outstat);
        outstat.close();
        ofstream outconf("qc_conf");
        sim.save(outconf);
        outconf.close();
        ofstream outconv("qc_convergence");
        sim.print_conv(outconv);
        outconv.close();
        return 0;
      }
    }
    if (counter[MEASURE] >= sim.Nmeasure) {
      sim.update_measurements();
      counter[MEASURE]=0;
    }
  } while(1);
  return 0;
}

void MC::init() {
  
  
  order = 0;
  
  row_index = 0;
  //list_index = 0;
  trA = 0.0;
  weight_fake = 2*Nsites;
  J_Heis = 1.0;
  XXZ = 1.0;
  shift = Nsites* 0.5;
  
  nb.resize(Nsites);
  for (size_t j=0; j < Nsites; j++) nb[j].resize(2*dim);
  
  for (size_t j =0; j < Ny; j++) {
    size_t y = j*Nx;
    for (size_t i = 0; i < Nx; i++) {
      i == Nx-1 ? nb[i+y][0] = y : nb[i+y][0] = i+y+1;
      i == 0 ? nb[i+y][2] = y + Nx-1 : nb[i+y][2] = i+y-1;
      j == Ny - 1 ? nb[i+y][1] = i : nb[i+y][1] = (j+1)*Nx + i;
      j == 0 ? nb[i+y][3] = (Ny-1)*Nx + i : nb[i+y][3] = (j-1)*Nx + i;
    }
  }
  
  Nlen = Nlen_init;
  XPsi.resize(Nlen);
  
  for (size_t n=0; n < XPsi.size(); n++) {
    bitset<Nsites> state;
    for (;;) {
      state.set(static_cast<size_t>(rnd(MyGenerator) * Nsites));
      if (state.count() == Nsites/2) break;
    }
    XPsi[n] = state;
  }
  //for (size_t i=0; i < Nsites; i++) { Hist_corr_meas[i] = 0.; }
  
  update_prob[upd_from_norm] = 1.;
  
  update_prob[upd_change_col] = 0.0;
  update_prob[upd_to_norm] = 1.;
  
  p_from_norm = update_prob[upd_from_norm] ;
  
  p_change_col = update_prob[upd_change_col];
  p_to_norm = p_change_col + update_prob[upd_to_norm];

  
  if (is_not_close(p_from_norm,1.)) {
    std::cerr << "# check update probabilities order 0\n";
    exit(1);
  }
  if (is_not_close(p_to_norm,1.)) {
    std::cerr << "# check update probabilities order 1\n";
    std::cerr << p_change_col << " " << p_to_norm << "\n";
    std::cerr << update_prob[upd_change_col] << " " << update_prob[upd_to_norm] << "\n";
    exit(1);
  }

  
  reset_statistics();
  MCsteps = 0;
  print_params(cout);
  ofstream out_params("qc_params");
  print_params(out_params);
  out_params.close();
}

/*
double MC::make_Hamiltonian( const bitset<Nsites>& state_in) {
  double s = 0;
  bitset<Nsites> state = state_in;
  col_list.clear();
  // potential energy part
  double Vp = 0.;
  for (size_t j=0; j < Nsites; j++) {
    //size_t k = (j+1) % Nsites;
    for (size_t idim =0; idim < dim; idim++) {
      size_t k = nb[j][idim];
      Vp += (state[j] - 0.5)  * (state[k]-0.5);
    }
  }
  double w = shift - Vp * J_Heis * XXZ ;
  if (w < 0) {
    std::cerr << "negative diagonal element? " << Vp * J_Heis * XXZ  << "\t" << shift << "\n";
    exit(1);
  }
  col_list.push_back(pair<bitset<Nsites>, double>(state, w) );
  s += w;
  // kinetic energy part
  for (size_t j=0; j < Nsites; j++) {
    //size_t k = (j+1) % Nsites;
    for (size_t idim =0; idim < dim; idim++) {
      size_t k = nb[j][idim];
      if (state.test(j) xor state.test(k) ) {
        state.flip(j);
        state.flip(k);
      
        col_list.push_back( pair<bitset<Nsites>, double>(state, J_Heis/2) );
        s += fabs(J_Heis/2);
        state.flip(j);
        state.flip(k);
        if (J_Heis/2 < 0) {
          std::cerr << "negative off-diagonal element?\n";
          exit(1);
        }
      }
    }
  }
  
 
  std::cerr << " Heatbath updates are switched off. Uncomment only after careful checking at own risk.\n";
 return s;
}
*/

void MC::do_step() {
  
  int a;
  if (order == 0) {
    a = from_norm();
    update_statistics[3][upd_from_norm] += 1; update_statistics[a][upd_from_norm] += 1;
  }
  else if (order == 1) {
    /*
    double q = rnd(MyGenerator);
    if (q < p_change_col) {
     a = change_col();
     update_statistics[3][upd_change_col] += 1; update_statistics[a][upd_change_col] += 1;
    }
    else if (q < p_to_norm) {
      a = to_norm();
      update_statistics[3][upd_to_norm] += 1; update_statistics[a][upd_to_norm] += 1;
    }
    */
    a = to_norm();
    update_statistics[3][upd_to_norm] += 1; update_statistics[a][upd_to_norm] += 1;
  }
}


int MC::from_norm() {
  size_t indx =static_cast<size_t>(rnd(MyGenerator)* Nlen);
  bitset<Nsites> state1 = XPsi[indx];
  //trA = make_Hamiltonian(state1);
  //size_t ind2 = heatbath(col_list, trA);
  bitset<Nsites> state = state1;
  size_t idim = static_cast<size_t>(rnd(MyGenerator) * (dim+1));
  double wx = weight_fake;
  double wy;
  double pxy = update_prob[upd_from_norm] / (dim + 1.);
  double pyx = update_prob[upd_to_norm];
  //size_t ind2;
  double g1 = 1.;
  double g2 = 1.;
  if (idim != dim) {
    size_t j = static_cast<size_t>(rnd(MyGenerator)* Nsites);  
    size_t k = nb[j][idim];
    if (state.test(j) xor state.test(k) ) {
      state.flip(j);
      state.flip(k);
    }
    else {
      return 1;
    }
    //ind2 = state;
    trA = -abs(J_Heis/2);
    pxy /= Nsites;
    g1 = Gutzwiller(state1);
    g2 = Gutzwiller(state);
    //cout << "Gutzwiler : " << g1 << "\t" << g2 << "\n";
  }
  else {
    double Vp = 0.;
    for (size_t j=0; j < Nsites; j++) {
      //size_t k = (j+1) % Nsites;
      for (size_t idim =0; idim < dim; idim++) {
        size_t k = nb[j][idim];
        Vp += (state[j] - 0.5)  * (state[k]-0.5);
      }
    }
    double w = shift - Vp * J_Heis * XXZ ;
    if (w < 0) {
      std::cerr << "negative diagonal element? " << Vp * J_Heis * XXZ  << "\t" << shift << "\n";
      exit(1);
    }
    trA = w;
    //ind2 = indx;
  }
  trA *= g2/g1;
  wy = abs(trA) ;
  
  
  double ratio = wy * pyx / wx / pxy;
  
  if (Metropolis(std::fabs(ratio))) {
    row_index = state;
    order = 1;
    return 2;
  }
  else {
    return 1;
  }
}

int MC::to_norm() {
  // nothing to do
  double wy = weight_fake;
  double wx = abs(trA);
  double pyx = update_prob[upd_from_norm] / (dim + 1.);
  if (trA < 0) pyx /= Nsites;
  double pxy = update_prob[upd_to_norm];
  double ratio = wy * pyx / wx / pxy;
  
  if (Metropolis(std::fabs(ratio))) {
    //std::cout << "# to_norm accepted " << ratio << "\t" << 1./ratio << "\n";
    order = 0;
    return 2;
  }
  else {
    return 1;
  }
}

int MC::change_col() {
  //size_t ind2 = heatbath(col_list, trA);
  //list_index = ind2;
  //row_index = col_list[ind2].first;
  return 2;
}


void MC::update_measurements() {
  MCsteps++;
  if (order == 0) { MCmeas_zero += 1.;  }
  
  if (order == 1 ) {
    MCmeas_one += 1.;
    //bitset<Nsites> state(row_index);
    size_t Nlen_t = static_cast<size_t>(sqrt(MCsteps/kappa));
    if (Nlen_t <= Nlen || MCsteps < 1e4 ) {
      size_t indx =static_cast<size_t>(rnd(MyGenerator)* XPsi.size());
      XPsi[indx] = row_index;
    } 
    else {
      if (Nlen >= Nlist_max) {
        cout << "Exiting. The list is over " << Nlist_max << "\n";
        ofstream outstat("qc_updates");
        print_update_statistics(outstat);
        outstat.close();
        ofstream outconf("qc_conf");
        save(outconf);
        outconf.close();
        ofstream outconv("qc_convergence");
        print_conv(outconv);
        outconv.close();
        exit(0);
      }
      //cout << "# Increasing : " << Nlen << "\t" << MCsteps << "\n";
      XPsi.push_back(row_index);
      Nlen++;
    }
  }
}

void MC::print_update_statistics(std::ostream& os) const {
  std::vector<string> name;
  os << setprecision(10);
  name.push_back("# CHANGE_COL           ");
  name.push_back("# FROM_NORM            ");
  name.push_back("# TO_NORM              ");

  os << "\n\n# UPDATE STATISTICS";
  os << "\n" << "# col 1 : all updates"
  << "\n" << "# col 2 : possible updates"
  << "\n" << "# col 3 : rejected updates"
  << "\n" << "# col 4 : accepted updates"
  << "\n" << "# col 5 : acceptance factor with respect to all attempts"
	 << "\n" << "# col 6 : acceptance factor with respect to Metropolis ratio only.\n";
  for (size_t i = 0; i < number_updates; i++) {
    os << "\n" << name[i] << "\t" << update_statistics[3][i] << "\t" << update_statistics[3][i] - update_statistics[0][i] << "\t"
	   << update_statistics[1][i] << "\t" << update_statistics[2][i]
	   << "\t" <<  update_statistics[2][i] / update_statistics[3][i]
	   << "\t" << update_statistics[2][i] / (update_statistics[3][i] - update_statistics[0][i]);
  }
  os << "\n\n";
  os << "# Total number of steps : " << MCsteps << "\tfraction in order zero : " << (MCmeas_zero*1.) / MCsteps << "\t" << (MCmeas_one*1.) / MCsteps <<  "\n";

}


void MC::reset_statistics() {
  reset_update_statistics();
  //MCsteps = 0;
  MCmeas_zero = 0;
  MCmeas_one = 0;
  
}

void MC::reset_update_statistics() {
  for (size_t i= 0; i < number_statistics; i++) {
    for (size_t j = 0; j < number_updates; j++) {
      update_statistics[i][j] = 0;
    }
  }
}
                         
                         

void MC::save(std::ostream& os) {
  os << order << "\n";
  os << times_overall << "\n";
  //os << list_index << "\n";
  os << row_index << "\n";
  os << trA << "\n";
  os << weight_fake << "\n";
  os << MCsteps  << "\t" << MCmeas_zero << "\t" << MCmeas_one << "\n";
  os << Nwrite_cur << "\n";
  //os << col_list.size() << "\n";
  //for (size_t i=0; i < col_list.size(); i++) {
  //  os << col_list[i].first << "\t" << col_list[i].second << "\n";
  //}
  
  // update_stat
  for (size_t i= 0; i < number_statistics; i++) {
    for (size_t j = 0; j < number_updates; j++) {
      os << update_statistics[i][j] << "\t";
    }
  }
  os << conv_log.size() << "\n";
  for (vector< pair<double, double> >::iterator it = conv_log.begin(); it != conv_log.end(); ++it) {
    os << it->first << "\t" << it->second << "\n";
  }
  os << XPsi.size() << "\n";
  for (size_t n=0 ; n < XPsi.size(); n++) os << XPsi[n] << "\n";
  os << Nlen  << "\n";
  os << MyGenerator;
}

void MC::load(std::istream& is) {
  is >> order;
  is >> times_overall;
  //is >> list_index;
  is >> row_index;
  is >> trA ;
  is >> weight_fake ;
  is >> MCsteps >> MCmeas_zero >> MCmeas_one;
  is >> Nwrite_cur;
  size_t n;
  //is >> n;
  //col_list.resize(n);
  //for (size_t i=0; i < col_list.size(); i++) {
  //  is >> col_list[i].first >> col_list[i].second ;
  //}
  
  // update_stat
  for (size_t i= 0; i < number_statistics; i++) {
    for (size_t j = 0; j < number_updates; j++) {
      is >> update_statistics[i][j];
    }
  }
  if (is.fail()) {
    std::cerr << "# Unable to load qc_conf (upd)\n";
  }
  is >> n;
  conv_log.resize(n);
  for (vector< pair<double, double> >::iterator it = conv_log.begin(); it != conv_log.end(); ++it) {
    is >> it->first >> it->second;
  }
  size_t Nlen_psi;
  is >> Nlen_psi;
  XPsi.resize(Nlen_psi);
  for (size_t n=0 ; n < XPsi.size(); n++) {
    is >> XPsi[n] ;
    if (is.fail()) {
      std::cerr << "# Unable to load qc_conf (XPsi) \n";
    }
  }
  is >> Nlen;
  if (is.fail()) {
    std::cerr << "# Unable to load qc_conf (Nlen) \n";
  }
  is >> MyGenerator;
}

void MC::print_conv(std::ostream& os) {
  for (vector< pair<double, double> >::iterator it = conv_log.begin(); it != conv_log.end(); ++it) {
    os << it->first << "\t" << it->second << "\n";
  }
}

void MC::print_params(std::ostream& os) const {
  os << "# Stochastic list simulation of a 2D Heisenberg model using protocol3:\n";
  os << "# The list length P is proportional to the sqrt(MCtime / kappa).\n";
  os << "# System and simulation parameters : \n";
  os << "Max length    : " << Nlist_max << "\n";
  os << "Init length   : " << Nlen_init << "\n";
  os << "Current len   : " << Nlen << "\n";
  os << "Seed rnd Gen  : " << seed << "\n";
  os << "NWrite        : " << Nwrite << "\n";
  os << "Nsites        : " << Nsites << "\t" << Nx << "\t" << "\n";
  os << "J_Heis        : " << J_Heis << "\n";
  os << "XXZ           : " << XXZ << "\n";
  os << "shift         : " << shift << "\n";
  os << "kappa         : " << kappa << "\n";
  os << "Gutzwiller_b  : " << Gutzwiller_b << "\n";
  os << "runtime       : " << times_runtime << "\n";
  
}

void MC::print_copyright(std::ostream& os) const {
  os << "\n"
  << "-------------------------------------------------------------\n"
  << "Copyright (C) 2018 Lode Pollet\n"
  << "This program comes with ABSOLUTELY NO WARRANTY.\n"
  << "This is free software, and you are welcome to redistribute it\n"
  << "under certain conditions.\n"
  << "-------------------------------------------------------------\n"
  << "\n";
}

void MC::print_list()  {
  for (size_t n=0; n < Nlen; n++) cout << XPsi[n]  << "\n";
}




