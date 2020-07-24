#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int main() {
  vector<double> tau;
  vector<double> bare;
  vector<double> err;
  vector<double> lst3, lst4, lst5, lst6;
  ifstream inbare("green_bare");
  double d1,d2,d3;
  int inc = 0;
  for (;;) {
    inbare >> d1 >> d2 >> d3;
    if (inbare.fail()) break;
    inc++;
    tau.push_back(d1);
    bare.push_back(d2);
    err.push_back(d3);
  }
  inbare.close();
  ifstream inlist3("green3");
  inc = 0;
  for (;;) {
    inlist3 >> d1 >> d2 >> d3;
    if (inlist3.fail()) break;
    if (d1 != tau[inc]) {
      cerr << "Error with times : " << inc << "\t" << d1 << "\t" << tau[inc] << "\n";
      exit(1);
    }
    inc++;
    lst3.push_back(d2); 
  }
  inlist3.close();
ifstream inlist6("green6");
  inc = 0;
  for (;;) {
    inlist6 >> d1 >> d2 >> d3;
    if (inlist6.fail()) break;
    if (d1 != tau[inc]) {
      cerr << "Error with times : " << inc << "\t" << d1 << "\t" << tau[inc] << "\n";
      exit(1);
    }
    inc++;
    lst6.push_back(d2);
  }
  inlist6.close();
  for (size_t i =0; i < tau.size(); i++) {
    if (tau[i] > 0.5) break;
    cout << tau[i] << "\t" << bare[i] << "\t" << err[i] << "\t" << lst3[i] << "\t" <<  (lst3[i] - bare[i])/(bare[i]) << "\t" <<  lst6[i] << "\t" << (lst6[i] - bare[i])/(bare[i]) << "\n";
 
  } 
  return 0;
}
