// Stochastic lists: Sampling multi-variable functions with population methods
// Copyright (C) 2018 Lode Pollet

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

#pragma once

#include <time.h>
#include <random>
#include <vector>
#include <bitset>
#include <iostream>

using namespace std;


class MC {
public:
  MC () : Nmeasure(1)
        , Nwrite(10000000)
        , eps_const(1e-14)
        , max_order(2)
        , number_statistics(4)
        , number_updates(3)
        , MyGenerator(rd())
        , rnd(0,1)
  {
    update_prob.resize(number_updates);
    update_statistics.resize(number_statistics);
    for (size_t j =0; j < number_statistics; j++) update_statistics[j].resize(number_updates);
    
  };
  enum {upd_change_col, upd_from_norm, upd_to_norm};
  // constants
  const size_t Nmeasure;                // frequency of MC measurement
  const size_t Nwrite;                  // frequency of output to screen
  const double eps_const;
  const size_t max_order;               // maximum diagram order
  const size_t number_statistics;
  const size_t number_updates;

  static constexpr size_t dim = 2;
  static constexpr size_t Nx = 10;      // linear system size
  static constexpr size_t Ny = 10;
 
  static constexpr size_t Nsites = Nx*Ny;     // total number of sites
  vector<vector<size_t> > nb;  // adjacency for square lattice
  
  size_t Nwrite_cur;                    // frequency of output to screen ( more often in beginning)

  // Hamiltonian variables
  double J_Heis;
  double XXZ;
  double shift;               // constant to make (shift - H ) positive definite

  // stochastic list
  size_t Nlist_max, Nlen_init, Nlen;
  vector< bitset<Nsites> > XPsi;        // stochastic list of configurations; spin configurations stored as bits
  
  
  // random number generators
  random_device rd;
  unsigned int seed;
  mt19937 MyGenerator;
  uniform_real_distribution<double> rnd;
  
  // updates
  vector<double> update_prob;
  double p_change_col, p_from_norm, p_to_norm;
  vector<vector<double> > update_statistics; // (0) : impossible (1) : rejected (2) : accepted (3) : total attempted
  size_t order;
  
  
  time_t times_runtime, times_tot, times1, times2, dtimes, times_overall;
  
  size_t list_index;
  bitset<Nsites> row_index;       // index i of matrix H_{ij}   ( = final state index)
  double trA;                     // weight of hamiltonian matrix element or its norm
  double weight_fake;             // normalization optimization parameter
  //vector<pair<bitset<Nsites> , double> > col_list;
  
  double Gutzwiller_b;
  double kappa;
  
  double MCsteps;
  double MCsteps_zero;
  double MCmeas_zero, MCmeas_one;
  size_t Nmeas;
  vector< pair<double, double> > conv_log;

  double Gutzwiller(bitset<Nsites>& state) {
    double sum = 0.;
    for (size_t s1 = 0; s1 < Nsites; s1++) {
      for (size_t j=0 ; j < dim; j++) {
        sum += (state[s1]-0.5) * (state[nb[s1][j]]-0.5);
      }
    }
    double prod = exp(- Gutzwiller_b * sum );
    return prod;
  }

  
 
 
  //size_t heatbath(const vector<pair<size_t,double> >& v, const double sv) {
  size_t heatbath(const vector<pair<bitset<Nsites>,double> >& v, const double sv) {
    double q = rnd(MyGenerator) * sv;
    //cout << "# HB q " << q << "\t sv " << sv << "\t size " << v.size() << "\n";
    double s = fabs(v[0].second);
    size_t inc = 0;
    for (;;) {
      
      //bitset<Nsites> state = v[inc].first;
      if (q < s) break;
      inc++;
      s += fabs(v[inc].second);
    }
    return inc;
  }
  
  bool Metropolis(const double& x) {
    if (x > 1) return (true);
    if (rnd(MyGenerator) < x) return (true);
    return (false);
  }

  
  void do_step();
  int from_norm();
  int to_norm();
  int change_col();
  
  //double make_Hamiltonian(const bitset<Nsites>& );
  void update_measurements();
  
  bool is_not_close(const double val1, const double val2) const {
    const double tol = 1e-8;
    bool answ = false;
    if (fabs(val1) > 1.) {
      if (fabs(1. - val1/val2) > tol) return true;
    }
    else {
      if (fabs(val1 - val2) > tol) return true;
    }
    return answ;
  }
  
  void init();
  void print_copyright(std::ostream& os) const;
  void print_update_statistics(std::ostream& os) const;
  void reset_update_statistics();
  void reset_statistics();
  void print_Eigenvalue_meas(std::ostream&) const;
  void print_list();
  void print_params(std::ostream&) const;
  void print_conv(std::ostream& );
  void save(std::ostream&);
  void load(std::istream&);
    
    
};



