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
    kinetics = Arrhenius(A=(1.27, 'cm^3/(mol*s)'), n=1.97, Ea=(-6.111, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 2,
    label = "MPO1O-1Q <=> Propionic + OH + CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54e15, 's^-1'), n=-0.465, Ea=(45.378, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)

entry(
    index = 3,
    label = "MPO1O-1OJ <=> Propionic + CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.54e15, 's^-1'), n=-0.465, Ea=(45.378, 'kcal/mol'), T0=(1, 'K')),
    shortDesc = u"""G4 calculation with 1-D HR by Lintao Bu at Nrel""",
)


