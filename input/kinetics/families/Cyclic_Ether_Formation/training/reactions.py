#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H3O3 <=> C2H2O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+17, 's^-1', '*|/', 2.51189),
        n = -1.1,
        Ea = (27.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
)
    
entry(
    index = 2,
    label = "MPO1Q2J-1Q-1 <=> MPO-1Q12OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.75e11, 's^-1'), n=0.025, Ea=(10.813, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 3,
    label = "MPO1Q2J-1Q-2 <=> MPO1Q2-1OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e8, 's^-1'), n=0.376, Ea=(13.863, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 4,
    label = "MPO1Q-1J <=> MPO1-1OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.092, 's^-1'), n=3.667, Ea=(21.351, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 5,
    label = "MPO1Q2J-1 <=> MPO12OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e17, 's^-1'), n=-2.844, Ea=(12.492, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 6,
    label = "MPO1Q3J <=> MPO13OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.659e4, 's^-1'), n=1.438, Ea=(16.939, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 7,
    label = "MPO1Q2J3Q-1 <=> MPO3Q12OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.217e25, 's^-1'), n=-5.469, Ea=(13.266, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

entry(
    index = 8,
    label = "MPO1Q2J3Q-2 <=> MPO1Q23OCYC + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.069e14, 's^-1'), n=-0.176, Ea=(13.802, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 Calculation with 1-D HR done by Lintao Bu at Nrel
""",
)

