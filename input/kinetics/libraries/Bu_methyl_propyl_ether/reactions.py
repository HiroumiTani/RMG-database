#!/usr/bin/env python
# encoding: utf-8

name = "Bu_methyl_propyl_ether"
shortDesc = u"Library for COCCC combustion reactions not covered by families"
longDesc = u"""
G4 calculations from Lintao Bu at Nrel
related to COCCC combustion
"""
entry(
    index = 1,
    label = "MPO1O-1Q + HCOOH <=> HCOOH + MPO_CP1-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.756e0, 'cm^3/(mol*s)'), n=1.816, Ea=(-3.086, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 2,
    label = "MPO1O-1Q <=> Propionic + OH + CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.742e15, 's^-1'), n=-0.392, Ea=(45.800, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 3,
    label = "MPO1O-1OJ <=> Propionic + CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.443e11, 's^-1'), n=0.444, Ea=(9.642, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 4,
    label = "MPO1Q3J <=> CH3OCHO + C2H4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.574e5, 's^-1'), n=1.509, Ea=(17.217, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 5,
    label = "MPO1O3Q + HCOOH <=> HCOOH + MPO_CP13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.065e10, 's^-1'), n=-3.325, Ea=(-8.340, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)


