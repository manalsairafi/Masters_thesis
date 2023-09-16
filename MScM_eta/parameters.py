# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 10.3.0 for Linux x86 (64-bit) (October 9, 2015)
# Date: Tue 11 Jul 2023 11:42:49



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

ScLL = Parameter(name = 'ScLL',
                 nature = 'external',
                 type = 'real',
                 value = 0.5,
                 texname = '\\text{ScLL}',
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

ScL2 = Parameter(name = 'ScL2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{ScL2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 2 ])

ScD1 = Parameter(name = 'ScD1',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{ScD1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

ScD2 = Parameter(name = 'ScD2',
                 nature = 'external',
                 type = 'real',
                 value = 1.e-10,
                 texname = '\\text{ScD2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

DM1 = Parameter(name = 'DM1',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{DM1}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

DM2 = Parameter(name = 'DM2',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{DM2}',
                lhablock = 'FRBlock',
                lhacode = [ 6 ])

DM3 = Parameter(name = 'DM3',
                nature = 'external',
                type = 'real',
                value = 300,
                texname = '\\text{DM3}',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

th12no = Parameter(name = 'th12no',
                   nature = 'external',
                   type = 'real',
                   value = 33.44,
                   texname = '\\text{th12no}',
                   lhablock = 'FRBlock',
                   lhacode = [ 8 ])

th23no = Parameter(name = 'th23no',
                   nature = 'external',
                   type = 'real',
                   value = 49.2,
                   texname = '\\text{th23no}',
                   lhablock = 'FRBlock',
                   lhacode = [ 9 ])

th13no = Parameter(name = 'th13no',
                   nature = 'external',
                   type = 'real',
                   value = 8.57,
                   texname = '\\text{th13no}',
                   lhablock = 'FRBlock',
                   lhacode = [ 10 ])

dCPno = Parameter(name = 'dCPno',
                  nature = 'external',
                  type = 'real',
                  value = 197,
                  texname = '\\text{dCPno}',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

sqDm21no = Parameter(name = 'sqDm21no',
                     nature = 'external',
                     type = 'real',
                     value = 7.42e-23,
                     texname = '\\text{sqDm21no}',
                     lhablock = 'FRBlock',
                     lhacode = [ 12 ])

sqDm3lno = Parameter(name = 'sqDm3lno',
                     nature = 'external',
                     type = 'real',
                     value = 2.517e-21,
                     texname = '\\text{sqDm3lno}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

z1r = Parameter(name = 'z1r',
                nature = 'external',
                type = 'real',
                value = 45,
                texname = '\\text{z1r}',
                lhablock = 'FRBlock',
                lhacode = [ 14 ])

z1i = Parameter(name = 'z1i',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{z1i}',
                lhablock = 'FRBlock',
                lhacode = [ 15 ])

z2r = Parameter(name = 'z2r',
                nature = 'external',
                type = 'real',
                value = 60,
                texname = '\\text{z2r}',
                lhablock = 'FRBlock',
                lhacode = [ 16 ])

z2i = Parameter(name = 'z2i',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{z2i}',
                lhablock = 'FRBlock',
                lhacode = [ 17 ])

z3r = Parameter(name = 'z3r',
                nature = 'external',
                type = 'real',
                value = 30,
                texname = '\\text{z3r}',
                lhablock = 'FRBlock',
                lhacode = [ 18 ])

z3i = Parameter(name = 'z3i',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{z3i}',
                lhablock = 'FRBlock',
                lhacode = [ 19 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Meta0R = Parameter(name = 'Meta0R',
                   nature = 'external',
                   type = 'real',
                   value = 1000,
                   texname = '\\text{Meta0R}',
                   lhablock = 'MASS',
                   lhacode = [ 9000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Weta0R = Parameter(name = 'Weta0R',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{Weta0R}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000005 ])

Weta0I = Parameter(name = 'Weta0I',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{Weta0I}',
                   lhablock = 'DECAY',
                   lhacode = [ 9000006 ])

WetaP = Parameter(name = 'WetaP',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WetaP}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000007 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9000008 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9000009 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9000010 ])

c12no = Parameter(name = 'c12no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos((cmath.pi*th12no)/180.)',
                  texname = '\\text{c12no}')

c13no = Parameter(name = 'c13no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos((cmath.pi*th13no)/180.)',
                  texname = '\\text{c13no}')

c23no = Parameter(name = 'c23no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos((cmath.pi*th23no)/180.)',
                  texname = '\\text{c23no}')

cz1 = Parameter(name = 'cz1',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.cos((cmath.pi*(complex(0,1)*z1i + z1r))/180.)',
                texname = '\\text{cz1}')

cz2 = Parameter(name = 'cz2',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.cos((cmath.pi*(complex(0,1)*z2i + z2r))/180.)',
                texname = '\\text{cz2}')

cz3 = Parameter(name = 'cz3',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.cos((cmath.pi*(complex(0,1)*z3i + z3r))/180.)',
                texname = '\\text{cz3}')

expdCPno = Parameter(name = 'expdCPno',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cmath.exp(-(dCPno*complex(0,1)))',
                     texname = '\\text{expdCPno}')

Meta0I = Parameter(name = 'Meta0I',
                   nature = 'internal',
                   type = 'real',
                   value = 'Meta0R + ScD2',
                   texname = '\\text{Meta0I}')

MetaP = Parameter(name = 'MetaP',
                  nature = 'internal',
                  type = 'real',
                  value = 'Meta0R + ScD1',
                  texname = '\\text{MetaP}')

MN1 = Parameter(name = 'MN1',
                nature = 'internal',
                type = 'real',
                value = 'DM1 + Meta0R',
                texname = '\\text{MN1}')

MN2 = Parameter(name = 'MN2',
                nature = 'internal',
                type = 'real',
                value = 'DM2 + Meta0R',
                texname = '\\text{MN2}')

MN3 = Parameter(name = 'MN3',
                nature = 'internal',
                type = 'real',
                value = 'DM3 + Meta0R',
                texname = '\\text{MN3}')

Mnu1no = Parameter(name = 'Mnu1no',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{Mnu1no}')

Mnu2no = Parameter(name = 'Mnu2no',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(sqDm21no)',
                   texname = '\\text{Mnu2no}')

Mnu3no = Parameter(name = 'Mnu3no',
                   nature = 'internal',
                   type = 'real',
                   value = 'cmath.sqrt(sqDm3lno)',
                   texname = '\\text{Mnu3no}')

s12no = Parameter(name = 's12no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin((cmath.pi*th12no)/180.)',
                  texname = '\\text{s12no}')

s13no = Parameter(name = 's13no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin((cmath.pi*th13no)/180.)',
                  texname = '\\text{s13no}')

s23no = Parameter(name = 's23no',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin((cmath.pi*th23no)/180.)',
                  texname = '\\text{s23no}')

sz1 = Parameter(name = 'sz1',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sin((cmath.pi*(complex(0,1)*z1i + z1r))/180.)',
                texname = '\\text{sz1}')

sz2 = Parameter(name = 'sz2',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sin((cmath.pi*(complex(0,1)*z2i + z2r))/180.)',
                texname = '\\text{sz2}')

sz3 = Parameter(name = 'sz3',
                nature = 'internal',
                type = 'complex',
                value = 'cmath.sin((cmath.pi*(complex(0,1)*z3i + z3r))/180.)',
                texname = '\\text{sz3}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

RCI1x1 = Parameter(name = 'RCI1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cz2*cz3',
                   texname = '\\text{RCI1x1}')

RCI1x2 = Parameter(name = 'RCI1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(cz3*sz1*sz2) - cz1*sz3',
                   texname = '\\text{RCI1x2}')

RCI1x3 = Parameter(name = 'RCI1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(cz1*cz3*sz2) + sz1*sz3',
                   texname = '\\text{RCI1x3}')

RCI2x1 = Parameter(name = 'RCI2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cz2*sz3',
                   texname = '\\text{RCI2x1}')

RCI2x2 = Parameter(name = 'RCI2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cz1*cz3 - sz1*sz2*sz3',
                   texname = '\\text{RCI2x2}')

RCI2x3 = Parameter(name = 'RCI2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(cz3*sz1) - cz1*sz2*sz3',
                   texname = '\\text{RCI2x3}')

RCI3x1 = Parameter(name = 'RCI3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'sz2',
                   texname = '\\text{RCI3x1}')

RCI3x2 = Parameter(name = 'RCI3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cz2*sz1',
                   texname = '\\text{RCI3x2}')

RCI3x3 = Parameter(name = 'RCI3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cz1*cz2',
                   texname = '\\text{RCI3x3}')

ScLambda1 = Parameter(name = 'ScLambda1',
                      nature = 'internal',
                      type = 'real',
                      value = '(MN1*(-((Meta0I**2*cmath.log(Meta0I**2/MN1**2))/(Meta0I**2 - MN1**2)) + (Meta0R**2*cmath.log(Meta0R**2/MN1**2))/(Meta0R**2 - MN1**2)))/(32.*cmath.pi**2)',
                      texname = '\\text{ScLambda1}')

ScLambda2 = Parameter(name = 'ScLambda2',
                      nature = 'internal',
                      type = 'real',
                      value = '(MN2*(-((Meta0I**2*cmath.log(Meta0I**2/MN2**2))/(Meta0I**2 - MN2**2)) + (Meta0R**2*cmath.log(Meta0R**2/MN2**2))/(Meta0R**2 - MN2**2)))/(32.*cmath.pi**2)',
                      texname = '\\text{ScLambda2}')

ScLambda3 = Parameter(name = 'ScLambda3',
                      nature = 'internal',
                      type = 'real',
                      value = '(MN3*(-((Meta0I**2*cmath.log(Meta0I**2/MN3**2))/(Meta0I**2 - MN3**2)) + (Meta0R**2*cmath.log(Meta0R**2/MN3**2))/(Meta0R**2 - MN3**2)))/(32.*cmath.pi**2)',
                      texname = '\\text{ScLambda3}')

UPMNSno1x1 = Parameter(name = 'UPMNSno1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'c12no*c13no',
                       texname = '\\text{UPMNSno1x1}')

UPMNSno1x2 = Parameter(name = 'UPMNSno1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'c13no*s12no',
                       texname = '\\text{UPMNSno1x2}')

UPMNSno1x3 = Parameter(name = 'UPMNSno1x3',
                       nature = 'internal',
                       type = 'complex',
                       value = 'expdCPno*s13no',
                       texname = '\\text{UPMNSno1x3}')

UPMNSno2x1 = Parameter(name = 'UPMNSno2x1',
                       nature = 'internal',
                       type = 'complex',
                       value = '-(c23no*s12no) - c12no*expdCPno*s13no*s23no',
                       texname = '\\text{UPMNSno2x1}')

UPMNSno2x2 = Parameter(name = 'UPMNSno2x2',
                       nature = 'internal',
                       type = 'complex',
                       value = 'c12no*c23no - expdCPno*s12no*s13no*s23no',
                       texname = '\\text{UPMNSno2x2}')

UPMNSno2x3 = Parameter(name = 'UPMNSno2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'c13no*s23no',
                       texname = '\\text{UPMNSno2x3}')

UPMNSno3x1 = Parameter(name = 'UPMNSno3x1',
                       nature = 'internal',
                       type = 'complex',
                       value = '-(c12no*c23no*expdCPno*s13no) + s12no*s23no',
                       texname = '\\text{UPMNSno3x1}')

UPMNSno3x2 = Parameter(name = 'UPMNSno3x2',
                       nature = 'internal',
                       type = 'complex',
                       value = '-(c23no*expdCPno*s12no*s13no) - c12no*s23no',
                       texname = '\\text{UPMNSno3x2}')

UPMNSno3x3 = Parameter(name = 'UPMNSno3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'c13no*c23no',
                       texname = '\\text{UPMNSno3x3}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

ScLambda1x1 = Parameter(name = 'ScLambda1x1',
                        nature = 'internal',
                        type = 'real',
                        value = '1/ScLambda1',
                        texname = '\\text{ScLambda1x1}')

ScLambda2x2 = Parameter(name = 'ScLambda2x2',
                        nature = 'internal',
                        type = 'real',
                        value = '1/ScLambda2',
                        texname = '\\text{ScLambda2x2}')

ScLambda3x3 = Parameter(name = 'ScLambda3x3',
                        nature = 'internal',
                        type = 'real',
                        value = '1/ScLambda3',
                        texname = '\\text{ScLambda3x3}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

ySc1 = Parameter(name = 'ySc1',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RCI1x1*UPMNSno1x1*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda1x1) + RCI1x2*UPMNSno2x1*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda1x1) + RCI1x3*UPMNSno3x1*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda1x1)',
                 texname = '\\text{ySc1}')

ySc12 = Parameter(name = 'ySc12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI1x1*UPMNSno1x2*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda1x1) + RCI1x2*UPMNSno2x2*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda1x1) + RCI1x3*UPMNSno3x2*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda1x1)',
                  texname = '\\text{ySc12}')

ySc13 = Parameter(name = 'ySc13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI1x1*UPMNSno1x3*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda1x1) + RCI1x2*UPMNSno2x3*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda1x1) + RCI1x3*UPMNSno3x3*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda1x1)',
                  texname = '\\text{ySc13}')

ySc2 = Parameter(name = 'ySc2',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RCI2x1*UPMNSno1x2*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda2x2) + RCI2x2*UPMNSno2x2*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda2x2) + RCI2x3*UPMNSno3x2*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda2x2)',
                 texname = '\\text{ySc2}')

ySc21 = Parameter(name = 'ySc21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI2x1*UPMNSno1x1*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda2x2) + RCI2x2*UPMNSno2x1*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda2x2) + RCI2x3*UPMNSno3x1*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda2x2)',
                  texname = '\\text{ySc21}')

ySc23 = Parameter(name = 'ySc23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI2x1*UPMNSno1x3*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda2x2) + RCI2x2*UPMNSno2x3*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda2x2) + RCI2x3*UPMNSno3x3*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda2x2)',
                  texname = '\\text{ySc23}')

ySc3 = Parameter(name = 'ySc3',
                 nature = 'internal',
                 type = 'complex',
                 value = 'RCI3x1*UPMNSno1x3*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda3x3) + RCI3x2*UPMNSno2x3*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda3x3) + RCI3x3*UPMNSno3x3*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda3x3)',
                 texname = '\\text{ySc3}')

ySc31 = Parameter(name = 'ySc31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI3x1*UPMNSno1x1*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda3x3) + RCI3x2*UPMNSno2x1*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda3x3) + RCI3x3*UPMNSno3x1*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda3x3)',
                  texname = '\\text{ySc31}')

ySc32 = Parameter(name = 'ySc32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'RCI3x1*UPMNSno1x2*cmath.sqrt(Mnu1no)*cmath.sqrt(ScLambda3x3) + RCI3x2*UPMNSno2x2*cmath.sqrt(Mnu2no)*cmath.sqrt(ScLambda3x3) + RCI3x3*UPMNSno3x2*cmath.sqrt(Mnu3no)*cmath.sqrt(ScLambda3x3)',
                  texname = '\\text{ySc32}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

ScL1 = Parameter(name = 'ScL1',
                 nature = 'internal',
                 type = 'real',
                 value = 'MH**2/vev**2',
                 texname = '\\text{ScL1}')

ScL5 = Parameter(name = 'ScL5',
                 nature = 'internal',
                 type = 'real',
                 value = '-(((Meta0I + Meta0R)*ScD2)/vev**2)',
                 texname = '\\text{ScL5}')

ScM = Parameter(name = 'ScM',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(Meta0R**2 - ScLL*vev**2)',
                texname = '\\text{ScM}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

ScL4 = Parameter(name = 'ScL4',
                 nature = 'internal',
                 type = 'real',
                 value = '-ScL5 - (2*(Meta0R + MetaP)*ScD2)/vev**2',
                 texname = '\\text{ScL4}')

ScL3 = Parameter(name = 'ScL3',
                 nature = 'internal',
                 type = 'real',
                 value = '-ScL4 - ScL5 + ScLL',
                 texname = '\\text{ScL3}')

