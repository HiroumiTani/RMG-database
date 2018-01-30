#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "MPO1O3Q <=> MPO_CP13",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.552e10, 's^-1'),
        n = -0.334,
        Ea = (11.444, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 calculation with 1-D HR by Lintao Bu at Nrel
""",
)