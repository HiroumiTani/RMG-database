#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H + CH3O <=> C2H2 + CH2O",
    reactant1 = 
"""
C2H
1 *1 C 1 0 {2,T}
2    C 0 0 {1,T} {3,S}
3    H 0 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 *3 C 1 0 {2,S} {3,S} {4,S}
2 *2 O 0 2 {1,S} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *4 H 0 0 {2,S}
""",
    product1 = 
"""
C2H2
1 *1 C 0 0 {2,T} {3,S}
2    C 0 0 {1,T} {4,S}
3 *4 H 0 0 {1,S}
4    H 0 0 {2,S}
""",
    product2 = 
"""
CH2O
1 *3 C 0 0 {2,D} {3,S} {4,S}
2 *2 O 0 2 {1,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H + CH2OH --> C2H2 + CH2O

pg. 504: Discussion on evaluated data

Entry 39,21 (a): CH2OH + C2H --> C2H2 + CH2O

Author suggest a disproportionation rate coefficient of 6.0x10^-11 cm3/molecule/s, due

to very exothermic rxn.  No data available at the time.
MRH 30-Aug-2009
""",
)

