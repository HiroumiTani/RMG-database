#!/usr/bin/env python
# encoding: utf-8

name = "Hydrazine_Decomposition"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "H2NN(T)",
    molecule =
"""
multiplicity 3
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.04729, -0.00311119, 2.29222e-05, -2.62291e-08, 9.90206e-12, 43492.6, 5.33183],
                Tmin = (10, 'K'),
                Tmax = (786.77, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.23132, 0.00869189, -4.48164e-06, 1.14412e-09, -1.15473e-13, 43698.8, 13.1517],
                Tmin = (786.77, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (361.629, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: N[N]

    calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ
    rotors calculated at b3lyp/6-311++g(df,pd)

    Thermodynamics for H2NN(T):
      Enthalpy of formation (298 K)   =    88.859 kcal/mol
      Entropy of formation (298 K)    =    56.175 cal/(mol*K)
       =========== =========== =========== =========== ===========
       Temperature Heat cap.   Enthalpy    Entropy     Free energy
       (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
       =========== =========== =========== =========== ===========
               300       9.040      88.877      56.236      72.007
               400      10.026      89.830      58.969      66.242
               500      11.054      90.884      61.317      60.226
               600      12.023      92.039      63.419      53.987
               800      13.622      94.611      67.108      40.924
              1000      14.845      97.463      70.285      27.178
              1500      16.816     105.431      76.720      -9.648
              2000      17.873     114.129      81.717     -49.305
              2400      18.407     121.391      85.025     -82.670
       =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 2,
    label = "NH2NHNH2",
    molecule =
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.79065, 0.0213782, -3.99354e-05, 9.75082e-08, -8.58502e-11, 22590.4, 6.83707],
                Tmin = (10, 'K'),
                Tmax = (429.355, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.487, 0.0237268, -1.3915e-05, 3.96331e-09, -4.38596e-13, 22792.7, 13.0758],
                Tmin = (429.355, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (187.822, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (174.604, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: NNN

    calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ
    rotors calculated at b3lyp/6-311++g(df,pd)

    Thermodynamics for NH2NHNH2:
      Enthalpy of formation (298 K)   =    48.625 kcal/mol
      Entropy of formation (298 K)    =    67.011 cal/(mol*K)
       =========== =========== =========== =========== ===========
       Temperature Heat cap.   Enthalpy    Entropy     Free energy
       (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
       =========== =========== =========== =========== ===========
               300      16.985      48.659      67.124      28.521
               400      19.862      50.501      72.406      21.539
               500      22.534      52.624      77.131      14.059
               600      24.866      54.997      81.451       6.126
               800      28.640      60.366      89.147     -10.952
              1000      31.445      66.388      95.855     -29.467
              1500      35.619      83.287     109.502     -80.966
              2000      37.696     101.665     120.062    -138.458
              2400      38.787     116.973     127.036    -187.913
       =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 3,
    label = "NH2NHNHNH2",
    molecule =
"""
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  N u0 p1 c0 {1,S} {4,S} {6,S}
3  N u0 p1 c0 {1,S} {7,S} {8,S}
4  N u0 p1 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",

    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.4889, 0.0587737, -0.000306151, 8.66171e-07, -8.12383e-10, 33175.8, 8.41442],
                Tmin = (10, 'K'),
                Tmax = (374.732, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.682102, 0.0385376, -2.42183e-05, 7.13449e-09, -8.02431e-13, 33738.6, 23.9032],
                Tmin = (374.732, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (275.806, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (220.334, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12/cc-pVTZ//B3LYP/6-311G(2d,d,p)""",
    longDesc =
    u"""
    SMILES: NNNN

    calculated by alongd (xc1103) at the CCSD(T)-F12/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotors calculated at ???

    Thermodynamics for NH2NHNHNH2 (N4H6):
    Enthalpy of formation (298 K)   =    70.447 kcal/mol
    Entropy of formation (298 K)    =    76.012 cal/(mol*K)
     =========== =========== =========== =========== ===========
     Temperature Heat cap.   Enthalpy    Entropy     Free energy
     (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
     =========== =========== =========== =========== ===========
             300      20.615      70.488      76.150      47.643
             400      25.155      72.775      82.697      39.696
             500      29.287      75.502      88.765      31.120
             600      32.835      78.613      94.427      21.957
             800      38.426      85.770     104.683       2.024
            1000      42.394      93.875     113.710     -19.835
            1500      47.721     116.613     132.076     -81.501
            2000      49.921     141.089     146.143    -151.198
            2400      51.031     161.289     155.348    -211.545
     =========== =========== =========== =========== ===========
    """,
)


entry(
    index = 4,
    label = "NH2NHN(S)",
    molecule =
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {3,D} {6,S}
3 N u0 p2 c-1 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.9699, 0.00187928, 5.2548e-05, -1.04631e-07, 6.53935e-11, 40913.3, 8.08867],
                Tmin = (10, 'K'),
                Tmax = (500.934, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.84747, 0.0168672, -1.03741e-05, 3.12044e-09, -3.64782e-13, 40950.2, 11.9733],
                Tmin = (500.934, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (340.164, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12/cc-pVTZ//B3LYP/6-311G(2d,d,p)""",
    longDesc =
    u"""
    SMILES: NN[N]

    calculated by alongd (xc1103) at the CCSD(T)-F12/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotors calculated at ???

    Thermodynamics for NH2NHN(S):
      Enthalpy of formation (298 K)   =    84.392 kcal/mol
      Entropy of formation (298 K)    =    65.190 cal/(mol*K)
       =========== =========== =========== =========== ===========
       Temperature Heat cap.   Enthalpy    Entropy     Free energy
       (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
       =========== =========== =========== =========== ===========
               300      13.846      84.420      65.282      64.835
               400      16.110      85.921      69.584      58.087
               500      17.994      87.629      73.388      50.935
               600      19.594      89.510      76.814      43.422
               800      22.157      93.698      82.820      27.442
              1000      24.038      98.328      87.978      10.350
              1500      26.810     111.127      98.319     -36.352
              2000      28.243     124.921     106.246     -87.571
              2400      29.030     136.384     111.468    -131.141
       =========== =========== =========== =========== ===========
    """,
)






