# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 10.3.0 for Linux x86 (64-bit) (October 9, 2015)
# Date: Tue 11 Jul 2023 11:42:49


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*ScL2)',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-2*complex(0,1)*ScL2',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-3*complex(0,1)*ScL2',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*ScL3)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(complex(0,1)*ScL3) - complex(0,1)*ScL4',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = 'ScL4/2. - ScL5/2.',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(complex(0,1)*ScL4)/2. + (complex(0,1)*ScL5)/2.',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(complex(0,1)*ScL3) - complex(0,1)*ScL4 - complex(0,1)*ScL5',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*ScL3) - complex(0,1)*ScL4 + complex(0,1)*ScL5',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-ScL4/2. + ScL5/2.',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(complex(0,1)*ScL5)',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-2*complex(0,1)*ScL5',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-ee/(2.*sw)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(complex(0,1)*ScL3*vev)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(complex(0,1)*ScL5*vev)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ScL4*vev)/2. - (ScL5*vev)/2.',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(complex(0,1)*ScL4*vev)/2. + (complex(0,1)*ScL5*vev)/2.',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(complex(0,1)*ScL3*vev) - complex(0,1)*ScL4*vev - complex(0,1)*ScL5*vev',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(complex(0,1)*ScL3*vev) - complex(0,1)*ScL4*vev + complex(0,1)*ScL5*vev',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(ScL4*vev)/2. + (ScL5*vev)/2.',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-yb',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = 'yb',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(yb/cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-ySc1',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'ySc1',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ySc1/cmath.sqrt(2))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(complex(0,1)*ySc1)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'ySc1/cmath.sqrt(2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-ySc12',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'ySc12',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(ySc12/cmath.sqrt(2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(complex(0,1)*ySc12)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'ySc12/cmath.sqrt(2)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-ySc13',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'ySc13',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(ySc13/cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(complex(0,1)*ySc13)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'ySc13/cmath.sqrt(2)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-ySc2',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'ySc2',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(ySc2/cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(complex(0,1)*ySc2)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'ySc2/cmath.sqrt(2)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-ySc21',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'ySc21',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-(ySc21/cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(complex(0,1)*ySc21)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = 'ySc21/cmath.sqrt(2)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-ySc23',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = 'ySc23',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(ySc23/cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(complex(0,1)*ySc23)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = 'ySc23/cmath.sqrt(2)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-ySc3',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = 'ySc3',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ySc3/cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(complex(0,1)*ySc3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'ySc3/cmath.sqrt(2)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-ySc31',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = 'ySc31',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(ySc31/cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(complex(0,1)*ySc31)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = 'ySc31/cmath.sqrt(2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-ySc32',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = 'ySc32',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(ySc32/cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(complex(0,1)*ySc32)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = 'ySc32/cmath.sqrt(2)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-yt',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = 'yt',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-ytau',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = 'ytau',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

