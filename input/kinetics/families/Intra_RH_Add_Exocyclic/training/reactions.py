#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "MPO1Q-1Q <=> MPO_CP1-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.416e11, 's^-1'), n=0.153, Ea=(35.947, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)