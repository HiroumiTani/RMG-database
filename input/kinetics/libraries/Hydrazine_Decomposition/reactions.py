#!/usr/bin/env python
# encoding: utf-8

name = "Hydrazine_Decomposition"
shortDesc = u"Hydrazine_Decomposition"
longDesc = u"""
 
"""

#-- N2H2 system--#
entry(
    index = 1,
    label = "H2NN(T) <=> H2NN(S)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
    Artificial transition from Triplet H2NN to Single H2NN.
""",
)

entry(
    index = 2,
    label = "N2H2 <=> H2NN(S)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-13.8511, 0.627501, -0.0350114, -0.0157004],
            [18.6057, 0.921662, -0.0465612, -0.0135683],
            [0.872831, 0.303498, -0.00455267, 0.0138132],
            [-0.385871, -0.0298657, 0.014964, 0.0163484],
            [-0.109817, -0.0368455, 0.01052, 0.00200981],
            [0.0287755, 0.00903461, 0.00265585, -0.00447134],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1097) at the CCSD(T)-F12a/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at  ???
""",
)

entry(
    index = 3,
    label = "H2NN(S) <=> N2 + H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-7.38087, 0.785943, -0.0774501, -0.00780201],
            [13.7989, 0.922225, -0.0752493, -0.00274985],
            [0.820108, 0.0140637, 0.0321019, 0.00895573],
            [-0.259037, -0.114722, 0.0437119, -0.00278543],
            [-0.0439093, 0.0568612, 0.00916914, -0.00975332],
            [-0.00659426, 0.0444414, -0.0093558, -0.000200908],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1097) at the CCSD(T)-F12a/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at  ???
""",
)

entry(
    index = 4,
    label = "N2H2 <=> N2 + H2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-17.7388, 0.472326, -0.160124, -0.097477],
            [23.191, 1.22126, -0.111845, 0.084807],
            [0.135253, -0.169954, 0.147134, 0.0181789],
            [-0.227456, 0.0392644, 0.0457154, -0.0320669],
            [-0.114344, 0.0576512, -0.0238903, 0.00670782],
            [-0.0357095, 0.000914306, -0.00598934, 0.00651496],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1097) at the CCSD(T)-F12a/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at  ???
""",
)

entry(
    index = 5,
    label = "H2NN(S) <=> NNH + H",
    degeneracy = 2,
    kinetics = Chebyshev(
        coeffs = [
            [-6.79535, -0.188745, -0.34384, 0.0497407],
            [13.029, 0.534428, 0.150297, -0.0233699],
            [-0.325696, 0.18094, 0.0883039, -0.00179],
            [-0.192609, -6.73287e-05, 0.0234701, 0.0039534],
            [-0.0810202, -0.00920937, 0.00618382, -0.000998913],
            [-0.0306573, -0.00107408, 0.00268743, -0.00152199],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1097) at the CCSD(T)-F12a/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at  ???
""",
)

entry(
    index = 6,
    label = "N2H2 <=> NNH + H",
    degeneracy = 2,
    kinetics = Chebyshev(
        coeffs = [
            [-14.863, 0.722928, -0.252228, 0.033144],
            [19.9042, -0.225503, 0.126307, 0.0170199],
            [-0.494738, 0.0656686, 0.0477197, -0.017545],
            [-0.218506, 0.0423105, 0.015279, -0.00408882],
            [-0.104384, 0.0174777, 0.00850125, -8.56115e-05],
            [-0.0502859, 0.00560463, 0.00500782, -7.98848e-05],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1097) at the CCSD(T)-F12a/cc-pVTZ//B3LYP/6-311G(2d,d,p) level of theory
frequencies calculated at  ???
""",
)

#--N3H5 system--#
entry(
    index = 7,
    label = "NH2 + N2H3 <=> H2NN(S) + NH3",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.21757, 'cm^3/(mol*s)'),
        n = 6.42471,
        Ea = (61.9432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 16 data points; dA = *|/ 1.81287, dn = +|- 0.0756373, dEa = +|- 0.49381 kJ/mol',
    ),
    longDesc = 
u"""
calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ in Molpro
rotor for NH2NHNH2 calculated at b3lyp/6-311++g(df,pd) in G03
Using BAC; frequencyScaleFactor = 0.975
""",
)

entry(
    index = 8,
    label = "NH2 + N2H3 <=> H2NN(T) + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.21757, 'cm^3/(mol*s)'),
        n = 6.42471,
        Ea = (61.9432, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 16 data points; dA = *|/ 1.81287, dn = +|- 0.0756373, dEa = +|- 0.49381 kJ/mol',
    ),
    longDesc = 
u"""
calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ in Molpro
rotor for NH2NHNH2 calculated at b3lyp/6-311++g(df,pd) in G03
Using BAC; frequencyScaleFactor = 0.975
""",
)

entry(
    index = 9,
    label = "N2H3 + NH2 <=> NH2NHNH2",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [7.31491, 2.08021e-07, -1.45151e-07, 8.19448e-08],
            [-0.0334447, -1.57978e-07, 1.10233e-07, -6.22316e-08],
            [-0.0078716, 2.70658e-08, -1.88857e-08, 1.06619e-08],
            [-0.00131193, 9.05743e-10, -6.32001e-10, 3.56797e-10],
            [-0.000245987, -2.72783e-11, 1.90338e-11, -1.07456e-11],
            [-4.91989e-05, 2.7058e-09, -1.88802e-09, 1.06588e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ in Molpro
rotor for NH2NHNH2 calculated at b3lyp/6-311++g(df,pd) in G03
Using BAC; frequencyScaleFactor = 0.975
""",
)

entry(
    index = 10,
    label = "NH2NHNH2 <=> NH3 + H2NN(S)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [0.765758, 1.10577e-07, -7.71573e-08, 4.35591e-08],
            [0.261864, -5.4252e-08, 3.78554e-08, -2.13712e-08],
            [-3.88158e-09, 6.85752e-09, -4.78497e-09, 2.70135e-09],
            [-4.62533e-10, 8.1715e-10, -5.70183e-10, 3.21896e-10],
            [-2.87309e-10, 5.07584e-10, -3.54177e-10, 1.99951e-10],
            [-9.46802e-10, 1.6727e-09, -1.16716e-09, 6.58918e-10],
        ],
        kunits = 's^-1',
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ in Molpro
rotor for NH2NHNH2 calculated at b3lyp/6-311++g(df,pd) in G03
Using BAC; frequencyScaleFactor = 0.975
""",
)

entry(
    index = 11,
    label = "N2H3 + NH2 <=> NH3 + H2NN(S)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Chebyshev(
        coeffs = [
            [-0.606233, -2, -1.45553e-07, 8.21715e-08],
            [-0.394372, -1.58205e-07, 1.1039e-07, -6.23208e-08],
            [-0.0153585, 2.70525e-08, -1.88764e-08, 1.06567e-08],
            [0.00873974, 9.12485e-10, -6.36711e-10, 3.59453e-10],
            [0.00574802, -2.40898e-11, 1.68149e-11, -9.4956e-12],
            [0.00699728, 2.71332e-09, -1.89327e-09, 1.06884e-09],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (0.01, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1089) at the CCSD(T)-F12/cc-pVTZ//M06-2x/cc-pVTZ level of theory
frequencies calculated at M06-2x/cc-pVTZ in Molpro
rotor for NH2NHNH2 calculated at b3lyp/6-311++g(df,pd) in G03
Using BAC; frequencyScaleFactor = 0.975
""",
)

#--N4H6 system--#
entry(
    index = 12,
    label = "H4N2 + H2NN(S) <=> N4H6",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [4.52142, 0.296043, -0.0355924, -0.00103696],
            [4.74921, 0.51088, -0.0528356, -0.00377167],
            [0.00580131, 0.32333, -0.0151673, -0.00582329],
            [-0.108793, 0.140205, 0.0116166, -0.00445702],
            [-0.0539451, 0.0316949, 0.0160641, -0.000833559],
            [-0.0192986, -0.00370379, 0.00811318, 0.00148977],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.1, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1106) at the CBS-QB3 level of theory
frequencies calculated at ub3lyp/6-311+g(2d,pd) freq iop(7/33=1) 
rotors calculated at ub3lyp/6-311g(2d,pd)
""",
)

entry(
    index = 13,
    label = "N4H6 <=> NH2NHN(S) + NH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-2.94768, 0.32912, -0.0407721, -0.000675425],
            [13.1871, 0.554322, -0.056741, -0.00413338],
            [-0.311025, 0.324552, -0.00929554, -0.00712396],
            [-0.269243, 0.118364, 0.0189964, -0.0047967],
            [-0.096138, 0.0130464, 0.018548, -3.19563e-05],
            [-0.0350758, -0.0100068, 0.00683165, 0.0021508],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.1, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1106) at the CBS-QB3 level of theory
frequencies calculated at ub3lyp/6-311+g(2d,pd) freq iop(7/33=1) 
rotors calculated at ub3lyp/6-311g(2d,pd)
""",
)

entry(
    index = 14,
    label = "H4N2 + H2NN(S) <=> NH2NHN(S) + NH3",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [1.94043, -1.01204, -0.0508346, -0.000798978],
            [8.39742, 0.74083, -0.0479071, -0.00798805],
            [0.393227, 0.294603, 0.0285135, -0.00946687],
            [-0.0660822, 0.00219188, 0.0414661, 0.000196971],
            [-0.0117972, -0.0623047, 0.0132224, 0.0062298],
            [0.0340405, -0.0253279, -0.00594649, 0.00355654],
        ],
        kunits = 's^-1',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.1, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1106) at the CBS-QB3 level of theory
frequencies calculated at ub3lyp/6-311+g(2d,pd) freq iop(7/33=1) 
rotors calculated at ub3lyp/6-311g(2d,pd)
""",
)

entry(
    index = 15,
    label = "N2 + NH3 <=> NH2NHN(S)",
    degeneracy = 1,
    kinetics = Chebyshev(
        coeffs = [
            [-33.6002, 0.652942, -0.0558797, -0.0046576],
            [36.3342, 0.687895, -0.0080199, -0.00542001],
            [-0.00383436, 0.12376, 0.0360771, 0.00262623],
            [-0.157707, 0.020043, 0.0138919, 0.0024742],
            [-0.074457, 0.00730114, 0.00411986, 0.000928166],
            [-0.0382373, -0.00477101, 0.00120969, 0.000576539],
        ],
        kunits = 'cm^3/(mol*s)',
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
        Pmin = (0.1, 'bar'),
        Pmax = (100, 'bar'),
    ),
    longDesc =
u"""
calculated by alongd (xc1107) at the CBS-QB3 level of theory
frequencies calculated at ub3lyp/6-311+g(2d,pd) freq iop(7/33=1) 
rotors calculated at ub3lyp/6-311g(2d,pd)
""",
)


#
#
##entry(
##    index = 0,
##    label = "NH2 + NH2 <=> H4N2",
##    degeneracy = 1.0,
##    kinetics = Chebyshev(
##        coeffs = [
##            [11.72, 0.2963, -0.0007635, -7.995e-05],
##            [-1.244, 0.003058, 0.0004983, 5.236e-05],
##            [-0.4721, 0.0008139, 0.00013, 1.309e-05],
##            [-0.1447, 6.636e-06, 1.553e-06, 2.676e-07],
##            [-0.0422, 1.19e-05, 1.74e-06, 1.375e-07],
##            [-0.003908, -0.0001309, -2.015e-05, -1.86e-06],
##        ],
##        kunits = 'cm^3/(mol*s)',
##        Tmin = (500, 'K'),
##        Tmax = (3000, 'K'),
##        Pmin = (0.493, 'atm'),
##        Pmax = (1.974, 'atm'),
##    ),
##)
#
##entry(
##    index = 1,
##    label = "NH2 + NH2 <=> N2H3 + H",
##    degeneracy = 1.0,
##    kinetics = Chebyshev(
##        coeffs = [
##            [6.844, -7.326e-06, -1.245e-06, -1.424e-07],
##            [3.05, 7.244e-06, 1.231e-06, 1.408e-07],
##            [0.123, 5.578e-07, 9.478e-08, 1.084e-08],
##            [0.04916, -4.475e-07, -7.603e-08, -8.695e-09],
##            [0.01741, -2.781e-07, -4.724e-08, -5.403e-09],
##            [0.006903, -6.777e-09, -1.153e-09, -1.321e-10],
##        ],
##        kunits = 'cm^3/(mol*s)',
##        Tmin = (500, 'K'),
##        Tmax = (3000, 'K'),
##        Pmin = (0.493, 'atm'),
##        Pmax = (1.974, 'atm'),
##    ),
##)
#
