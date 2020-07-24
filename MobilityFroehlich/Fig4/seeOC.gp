plot [0:15] []\
     "T8_0.dat" with lines, "T4_0.dat" with lines,\
     "T2_0.dat" with lines, "T1_0.dat" with lines,\
     "T0_5.dat" with lines, "T0_25.dat" with lines,\
     "T0_125.dat" with lines
pause -1

set log x

plot [0.01:20] []\
     "T8_0.dat" with lines, "T4_0.dat" with lines,\
     "T2_0.dat" with lines, "T1_0.dat" with lines,\
     "T0_5.dat" with lines, "T0_25.dat" with lines,\
     "T0_125.dat" with lines
pause -1

set log y

plot [0.01:20] [0.01:]\
     "T8_0.dat" with lines, "T4_0.dat" with lines,\
     "T2_0.dat" with lines, "T1_0.dat" with lines,\
     "T0_5.dat" with lines, "T0_25.dat" with lines,\
     "T0_125.dat" with lines
pause -1

