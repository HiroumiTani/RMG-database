#!/usr/bin/env python
# encoding: utf-8

name = "Bu_methyl_propyl_ether.py"
shortDesc = u"G4 with 1-D HR"
longDesc = u"""
G4 calculations run using Cantherm 1-D HR done by Lintao Bu at Nrel
made for combustion of methyl-propyl-ether
"""
entry(
    index = 0,
    label = "CH2COOCH3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,D}
4  O u0 p2 c0 {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83567,0.0145233,7.81521e-05,-2.13934e-07,1.82674e-10,142552,10.7744], Tmin=(10,'K'), Tmax=(300.05,'K')),
            NASAPolynomial(coeffs=[2.34933,0.0343378,-2.09033e-05,6.15085e-09,-6.99343e-13,142552,16.1558], Tmin=(300.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "MPO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44618,0.0474918,-6.62132e-05,1.03669e-07,-6.49171e-11,-28249.5,9.10621], Tmin=(10,'K'), Tmax=(574.1,'K')),
            NASAPolynomial(coeffs=[0.786644,0.0492491,-2.69818e-05,7.22382e-09,-7.58871e-13,-28249.5,22.8683], Tmin=(574.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "MPO1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {5,S} {14,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45234,0.05365,-0.000126472,2.5448e-07,-1.88294e-10,332813,10.2227], Tmin=(10,'K'), Tmax=(466.89,'K')),
            NASAPolynomial(coeffs=[1.9197,0.044409,-2.49072e-05,6.82697e-09,-7.32144e-13,332813,19.0608], Tmin=(466.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "MPO1QJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28174,0.0733203,-0.000166491,3.45406e-07,-2.85955e-10,176076,10.6064], Tmin=(10,'K'), Tmax=(392.77,'K')),
            NASAPolynomial(coeffs=[3.22771,0.0564821,-3.57802e-05,1.0832e-08,-1.25715e-12,176076,12.5239], Tmin=(392.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "MPO1Q-1J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {5,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68192,0.0236413,0.000212762,-7.00981e-07,6.36089e-10,220108,12.884], Tmin=(10,'K'), Tmax=(406.24,'K')),
            NASAPolynomial(coeffs=[8.35995,0.0317811,-1.74296e-05,5.21983e-09,-6.32132e-13,220108,-10.9754], Tmin=(406.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "MPO1Q2J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6879,0.132662,-0.00047552,9.36747e-07,-6.79849e-10,233953,11.311], Tmin=(10,'K'), Tmax=(426.1,'K')),
            NASAPolynomial(coeffs=[7.39266,0.047012,-2.79654e-05,8.02296e-09,-8.91373e-13,233953,-2.95402], Tmin=(426.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "MPO1Q3J",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25565,0.154331,-0.000474281,7.03353e-07,-3.81704e-10,247710,12.9621], Tmin=(10,'K'), Tmax=(555.25,'K')),
            NASAPolynomial(coeffs=[13.3669,0.0290044,-1.3386e-05,3.1023e-09,-2.88712e-13,247710,-27.8206], Tmin=(555.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "MPO1Star",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {5,S} {13,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52225,0.0408649,-5.05522e-05,7.26698e-08,-4.48502e-11,282036,9.2477], Tmin=(10,'K'), Tmax=(571.71,'K')),
            NASAPolynomial(coeffs=[1.7414,0.041958,-2.35976e-05,6.46222e-09,-6.91769e-13,282036,18.4682], Tmin=(571.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "MPO1-1OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03062,-0.00252733,0.000128158,-1.86361e-07,8.71637e-11,145477,11.2617], Tmin=(10,'K'), Tmax=(609.03,'K')),
            NASAPolynomial(coeffs=[-3.82255,0.0560851,-3.35254e-05,9.58787e-09,-1.05608e-12,145477,44.1835], Tmin=(609.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "MPO12OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80964,0.0287426,1.87539e-05,-3.39089e-08,1.19918e-11,162018,10.718], Tmin=(10,'K'), Tmax=(1075.78,'K')),
            NASAPolynomial(coeffs=[5.57892,0.039324,-1.9927e-05,4.8895e-09,-4.70381e-13,162018,-2.56211], Tmin=(1075.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "MPO1Q-1QJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91574,0.115846,-0.00035112,8.23593e-07,-7.62759e-10,75440.2,13.4872], Tmin=(10,'K'), Tmax=(332.65,'K')),
            NASAPolynomial(coeffs=[4.67696,0.0719594,-5.08301e-05,1.65677e-08,-2.02492e-12,75440.2,8.8173], Tmin=(332.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "MPO1Q3QJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1772,0.0718492,0.000156206,-7.74098e-07,8.15342e-10,96743.5,11.9998], Tmin=(10,'K'), Tmax=(373.44,'K')),
            NASAPolynomial(coeffs=[9.79049,0.0612786,-4.34018e-05,1.43735e-08,-1.78772e-12,96743.5,-19.0179], Tmin=(373.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "MPO1O-1Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00324,0.107259,-0.000391806,9.61462e-07,-8.71064e-10,-105019,10.7997], Tmin=(10,'K'), Tmax=(357.59,'K')),
            NASAPolynomial(coeffs=[3.71846,0.0615013,-4.14788e-05,1.30453e-08,-1.5518e-12,-105019,11.4601], Tmin=(357.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "MPO1Q2J-1Q",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.58812,0.152812,-0.000642455,1.56209e-06,-1.38062e-09,135152,16.3207], Tmin=(10,'K'), Tmax=(361.86,'K')),
            NASAPolynomial(coeffs=[4.99773,0.0674965,-4.55631e-05,1.42991e-08,-1.69557e-12,135152,12.4535], Tmin=(361.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "MPO-1Q12OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29344,0.0636104,-4.95383e-05,2.01739e-08,-3.40235e-12,71414.2,11.3248], Tmin=(10,'K'), Tmax=(1284.65,'K')),
            NASAPolynomial(coeffs=[10.9709,0.0397052,-2.16259e-05,5.68881e-09,-5.83484e-13,71414.2,-27.6376], Tmin=(1284.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "Ozoind1-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62664,0.0363321,4.34031e-05,-9.27261e-08,4.4423e-11,204075,11.5305], Tmin=(10,'K'), Tmax=(751.2,'K')),
            NASAPolynomial(coeffs=[3.79818,0.0549094,-3.26118e-05,9.27468e-09,-1.01799e-12,204075,7.09164], Tmin=(751.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "MPO1O3Q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9302,0.116298,-0.00047705,1.19137e-06,-1.06866e-09,-76847.8,12.7278], Tmin=(10,'K'), Tmax=(365.98,'K')),
            NASAPolynomial(coeffs=[3.28338,0.0610902,-4.03217e-05,1.24473e-08,-1.4584e-12,-76847.8,16.0769], Tmin=(365.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "MPO1Q2J3Q",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11166,0.0930877,-0.00011556,9.12963e-08,-3.28478e-11,162733,13.2566], Tmin=(10,'K'), Tmax=(620.49,'K')),
            NASAPolynomial(coeffs=[7.73174,0.0633042,-4.35597e-05,1.39376e-08,-1.67933e-12,162733,-6.82769], Tmin=(620.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "MPO1Q2Star",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u0 p0 c0 {3,D} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68793,0.0304826,0.000322109,-1.54801e-06,2.15377e-09,202667,11.0013], Tmin=(10,'K'), Tmax=(253.43,'K')),
            NASAPolynomial(coeffs=[5.00069,0.050019,-3.17871e-05,9.70755e-09,-1.14067e-12,202667,3.91943], Tmin=(253.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Ozoind13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76502,0.0315606,5.0096e-05,-8.69387e-08,3.6407e-11,210001,12.1606], Tmin=(10,'K'), Tmax=(855.73,'K')),
            NASAPolynomial(coeffs=[3.98919,0.0541525,-3.09428e-05,8.47788e-09,-8.9994e-13,210001,6.05663], Tmin=(855.73,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "MPO1Q2-1OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59505,0.042073,2.3024e-05,-6.33523e-08,2.95336e-11,-28092.2,10.8848], Tmin=(10,'K'), Tmax=(826.59,'K')),
            NASAPolynomial(coeffs=[5.68595,0.0516795,-3.02023e-05,8.44426e-09,-9.12038e-13,-28092.2,-2.8805], Tmin=(826.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "MPO1Q23OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38576,0.0659346,-4.45748e-05,9.88458e-09,8.94308e-13,104078,9.97381], Tmin=(10,'K'), Tmax=(1063.2,'K')),
            NASAPolynomial(coeffs=[14.2402,0.037064,-2.07254e-05,5.51606e-09,-5.67655e-13,104078,-46.2384], Tmin=(1063.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "MPO3Q12OCYC",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12067,0.0906382,-0.000263824,5.61366e-07,-4.55492e-10,98858.6,11.023], Tmin=(10,'K'), Tmax=(392.95,'K')),
            NASAPolynomial(coeffs=[4.03852,0.0560698,-3.55743e-05,1.07533e-08,-1.24515e-12,98858.6,9.93032], Tmin=(392.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "MPO1O-1OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {14,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1656,0.0877412,-0.000372232,9.10438e-07,-7.63069e-10,60911.1,11.1074], Tmin=(10,'K'), Tmax=(410.66,'K')),
            NASAPolynomial(coeffs=[0.52515,0.0542629,-3.37147e-05,9.84632e-09,-1.09986e-12,60911.1,27.5735], Tmin=(410.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "MPO1O3OJ",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {14,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.409,0.0647378,-0.000228776,6.1365e-07,-5.66539e-10,88331.8,13.435], Tmin=(10,'K'), Tmax=(383.52,'K')),
            NASAPolynomial(coeffs=[0.779616,0.0534078,-3.28936e-05,9.68225e-09,-1.09609e-12,88331.8,27.3161], Tmin=(383.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "MPO_CP1-1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56462,0.0370009,9.89701e-05,-2.69132e-07,1.89284e-10,-77919,11.1498], Tmin=(10,'K'), Tmax=(493.57,'K')),
            NASAPolynomial(coeffs=[3.72512,0.0589523,-3.84091e-05,1.1878e-08,-1.39978e-12,-77919,7.61967], Tmin=(493.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "Propionic",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88017,0.0184421,2.23717e-05,-3.14849e-08,1.02316e-11,87856.6,9.59501], Tmin=(10,'K'), Tmax=(1140.46,'K')),
            NASAPolynomial(coeffs=[5.14802,0.0308407,-1.60918e-05,3.95091e-09,-3.75412e-13,87856.6,-1.49115], Tmin=(1140.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "MPO1O-1O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,D}
4  C u0 p0 c0 {5,S} {12,D} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3454,0.064478,-0.000171941,3.66961e-07,-2.94518e-10,-93386.8,9.65601], Tmin=(10,'K'), Tmax=(418.93,'K')),
            NASAPolynomial(coeffs=[2.498,0.0489748,-3.19533e-05,9.75851e-09,-1.13293e-12,-93386.8,15.478], Tmin=(418.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "MPO_CP13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47754,0.0460187,1.10417e-05,-5.5054e-08,2.94415e-11,-48789.1,11.7138], Tmin=(10,'K'), Tmax=(735.88,'K')),
            NASAPolynomial(coeffs=[4.74967,0.0529554,-3.13329e-05,8.91441e-09,-9.805e-13,-48789.1,3.41835], Tmin=(735.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "MPO1O3O",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,D}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2758,0.0799826,-0.000357235,9.09099e-07,-7.94684e-10,140022,11.7998], Tmin=(10,'K'), Tmax=(390.03,'K')),
            NASAPolynomial(coeffs=[1.64397,0.0454345,-2.71377e-05,7.75226e-09,-8.54154e-13,140022,23.1365], Tmin=(390.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

