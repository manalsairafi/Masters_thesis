#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:06:50 2023

@author: Manal Alsairafi
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import os

'''direct detection limits'''

file = input('Result directory: ')

run = input('Run -- 00 format: ')

scan_results = file+'/output/scan_run_'+run+'.txt'

headers = []    
with open(scan_results) as f:
        for line in f:
            if line.startswith('#'):
                headers.append(line[9:-1])
            else:
                break

headers = headers[1:]

data = np.loadtxt(scan_results, comments='#', unpack=True, usecols=range(1,len(headers)+1))


dark_matter = '9000005'#change depending on the model output
DM_mass_header = 'mass#'+dark_matter

DM_name = r'$\eta^0_R$'

masses = data[headers.index(DM_mass_header)]


coupling_number = []
for i in headers:
    if 'frblock#' in i:
        number = int(i[8:])
        coupling_number.append(number)

#coupling -- change here depending on the model/setup
coupling = str(coupling_number[0])  
coupling_header = 'frblock#'+coupling
couplings = data[headers.index(coupling_header)]
    
coupling_name = r'$\lambda_L$'
        

SI_SD = 'SI'#spin independent - change to SD for spin dependent cross sections

#sigma = direct detection cross section

sigmas_p = data[headers.index('sigmaN_'+SI_SD+'_p')]
sigmas_n = data[headers.index('sigmaN_'+SI_SD+'_n')]
sigmas_lim = data[headers.index('lim_sigmaN_'+SI_SD+'_p')]

#for the cresst limits:
#toolarge: sigma > limit
#justright: sigma allowed
#nolim: no limit provided from the data

sigmas_toolarge = []
sigmas_justright = []
sigmas_nolim = []

masses_toolarge = []
masses_justright = []
masses_nolim = []

coupling_toolarge = []
coupling_justright = []
coupling_nolim = []

for i in range(len(sigmas_p)):
    #too large
    if sigmas_lim[i] == -1:
        sigmas_nolim.append(sigmas_p[i])
        masses_nolim.append(masses[i])
        coupling_nolim.append(couplings[i])
        
    elif  sigmas_p[i] > sigmas_lim[i] or sigmas_n[i] > sigmas_lim[i]:
        sigmas_toolarge.append(sigmas_p[i])
        masses_toolarge.append(masses[i])
        coupling_toolarge.append(couplings[i])
    
    else:
        sigmas_justright.append(sigmas_p[i])
        masses_justright.append(masses[i])
        coupling_justright.append(couplings[i])

#to create the exclusion region    
mass_coupling = list(zip(masses_toolarge, coupling_toolarge))
mass_coupling_pos = [x for x in mass_coupling if x[1] >= 0]
mass_coupling_neg = [x for x in mass_coupling if x[1] < 0]

mass_coupling_pos.sort(key=lambda x:x[0])
mass_coupling_neg.sort(key=lambda x:x[0])

mass_coupling_pos_ll = [mass_coupling_pos[i:i + 40] for i in range(0, len(mass_coupling_pos), 1)] 
mass_coupling_neg_ll = [mass_coupling_neg[i:i + 40] for i in range(0, len(mass_coupling_neg), 1)] 

#limits for positive coupling
min_mass = [] 
min_coupling = []
for i in range(len(mass_coupling_pos_ll)-1):
    threes = mass_coupling_pos_ll[i]
    threes.sort(key=lambda x:x[1])
    min_mass.append(threes[0][0])
    min_coupling.append(threes[0][1])

#limits for negative coupling
min_massn = []
min_couplingn = []
for i in range(len(mass_coupling_neg_ll)-1):
    threes = mass_coupling_neg_ll[i]
    threes.sort(key=lambda x:x[1])
    min_massn.append(threes[-1][0])
    min_couplingn.append(threes[-1][1])

#constants:
mH = 125.25
vev = 246.22
lam1=mH**2/(2.*vev**2)


'''relic density limits'''         
file = input('Result directory: ')

run = input('Run -- 00 format: ')

# Path for analysis file
analysis_path = os.path.join(file, 'analysis')
if not os.path.exists(analysis_path):
    os.mkdir(analysis_path)

scan_results = file+'/output/scan_run_'+run+'.txt'
param_card = file+'/cards/param_card.dat'

output = file+'/analysis'


#loading the data:
headers = []    
with open(scan_results) as f:
        for line in f:
            if line.startswith('#'):
                headers.append(line[9:-1])
            else:
                break

headers = headers[1:]

data = np.loadtxt(scan_results, comments='#', unpack=True, usecols=range(1,len(headers)+1))

#to find annihilation processes
relic_ind = []
relic_head = []

for i in range(len(headers)):
    if ' %_relic_' in headers[i]:
        relic_ind.append(i)
        relic_head.append(headers[i][9:])
    elif '%_relic_' in headers[i]:
        relic_ind.append(i)
        relic_head.append(headers[i][8:])
        
for i in range(len(relic_head)):
    relic_head[i] = relic_head[i].split('>')
    for j in range(2):
        relic_head[i][j] = relic_head[i][j].split('.')


proc = data[relic_ind[0]:relic_ind[-1]+1]

pdg_file = '/PDG_MC_numbering.txt'
pdg_part = list(np.loadtxt(pdg_file, comments='#', usecols=[0], dtype = np.str_))
pdg_num = list(np.loadtxt(pdg_file, comments='#', usecols=[1], dtype = np.str_))
pdg_type = list(np.loadtxt(pdg_file, comments='#', usecols=[2], dtype = np.str_))

def convert_pdg(pdg):
    if pdg in pdg_num:
        return pdg_part[pdg_num.index(pdg)]
    else:
        raise Exception('PDG code '+pdg+' not found. update your list')

def processes(relic_headers):
    n = len(relic_headers)
    x = relic_headers
    for i in range(n):
        string = ''
        m = len(x[i][0])
        for j in range(m):
            if j < m-1:
                string += convert_pdg(x[i][0][j]) + ' + '
            else:
                string += convert_pdg(x[i][0][j])
        string += r' $\rightarrow$ '
        m = len(x[i][1])
        for j in range(m):
            if j < m-1:
                string += convert_pdg(x[i][1][j]) + ' + '
            else:
                string += convert_pdg(x[i][1][j])
                
        x[i] = [string]   
    return x

relic_head = processes(relic_head)

proc = np.transpose(proc)

def maxn(lst,n):
    lst2 = sorted(lst, reverse = True)
    return lst2[n-1]

domin_process = []
for i in range(len(proc)): #for given mass and coupling
    dom = max(proc[i])
    if np.isnan(dom):
        domin_process.append('non')
    else:
        dom_index = list(proc[i]).index(dom)
        dom_header = relic_head[dom_index][0]
        n = 2
        
        while dom_header.find(r"$\rightarrow$ $\eta") != -1:
            dom = maxn(proc[i], n)
            dom_index = list(proc[i]).index(dom)
            dom_header = relic_head[dom_index][0]
            n += 1
            
        domin_process.append(dom_header)

domin_process_list = list(dict.fromkeys(domin_process))

dark_matter = '9000005'
DM_mass_header = 'mass#'+dark_matter

DM_name = r'$\eta^0_R$'

masses = data[headers.index(DM_mass_header)]

#coupling 
coupling_number = []
for i in headers:
    if 'frblock#' in i:
        number = int(i[8:])
        coupling_number.append(number)

coupling = str(coupling_number[0])  
coupling_header = 'frblock#'+coupling
couplings = data[headers.index(coupling_header)]
coupling_name = r'$\lambda_L$'

#making list for data of dominant process
mass_coup_domin = []
for i in range(len(domin_process_list)):
    mass_coup_domin.append([[],[]])
    for j in range(len(domin_process)):
        if domin_process[j] == domin_process_list[i]:
            mass_coup_domin[i][0].append(masses[j])
            mass_coup_domin[i][1].append(couplings[j])

#for plotting with different colors
from matplotlib import cm
number_of_lines= len(domin_process_list)
cm_subsection = np.linspace(0, 1, number_of_lines) 

color_lst = sorted([cm.magma(x) for x in cm_subsection],reverse=True)


lam2 = float(input('value given for lam2: '))
    
#vacuum condition
xmass = np.linspace(0, 100,10)
yvac_cond = np.full((1,10), -np.sqrt(lam1*lam2))
ymin = np.full((1,10),-1)
    
#positive masses
ypos_mass = xmass**2/((246)**2)
ymax = np.full((1,10),1)
 
#perturbativity
d1 = 50 #mass splitting delta1
d2 = 50 #mass splitting delta2

f = 2*(d1/246**2)*(d1+2*xmass)
g = (d1/246**2)*(d2+2*xmass)
h = 2*g**2+f**2-12*lam1
yminpert = (-np.sqrt(f**2+2*f*g+g**2-2*h)-f-g)/2
ymaxpert = (np.sqrt(f**2+2*f*g+g**2-2*h)-f-g)/2
   
omegas = data[headers.index('Omegah^2')] #values for relic density

#toolarge: omega > PLANCK measurement
#justright: omega in the PLANCK three sigma region
#small: omega < PLANCK measurement

omegas_toolarge = []
omegas_justright = []
omegas_small = []

masses_toolarge = []
masses_justright = []
masses_small = []

coupling_toolarge = []
coupling_justright = []
coupling_small = []


for i in range(len(omegas)):
    if  omegas[i] > 0.13 or omegas[i] == -1:
        omegas_toolarge.append(omegas[i])
        masses_toolarge.append(masses[i])
        coupling_toolarge.append(couplings[i])
    
    elif  omegas[i] <= 0.123 and omegas[i] >= 0.117:
        omegas_justright.append(omegas[i])
        masses_justright.append(masses[i])
        coupling_justright.append(couplings[i])
    
    elif omegas[i] < 0.11:
        omegas_small.append(omegas[i])
        masses_small.append(masses[i])
        coupling_small.append(couplings[i])


fig, (ax1, ax2) = plt.subplots(1,2, sharey=True, gridspec_kw={'width_ratios':[1,0.8]})
fig.set_figheight(3)
fig.set_figwidth(10)

mynorm = plt.Normalize(vmin=0, vmax=0.11)
sm = plt.cm.ScalarMappable(cmap='OrRd', norm=mynorm)

ax1.scatter(masses_toolarge, coupling_toolarge, c = 'grey', s=10)
ax1.scatter(masses_small, coupling_small, c=omegas_small, cmap='OrRd',s=10)
ax1.scatter(masses_justright, coupling_justright, c = 'indigo',s=10)

style = pat.ArrowStyle('simple',head_length=15.5, head_width=6.97, tail_width=4)
triangle = pat.FancyArrowPatch((107.85,0.98),(107.85,0.99),fc='grey', ec='black', clip_on = False, arrowstyle=style)
ax1.add_patch(triangle)

rect = plt.Rectangle((106.3,0.69),3,0.12, fc='indigo', ec='black', clip_on = False)
ax1.add_patch(rect)

ax1.fill_between(xmass, yvac_cond[0], ymin[0], color = 'gray', alpha =0.3)
ax1.fill_between(xmass, yminpert,-1, color = 'peru', alpha=0.5, hatch = 'xx')
ax1.fill_between(xmass, ymaxpert, 1, color = 'peru', alpha=0.5, hatch = 'xx')
#ax1.fill_between(xmass, ypos_mass, 1, color = 'pink', alpha = 0.3)
ax1.fill_between(min_mass, min_coupling, 1, color='navy', alpha=0.25)
ax1.fill_between(min_massn, min_couplingn, -1, color='navy', alpha=0.25)

ax1.text(111,0.72, s= r'(PLANCK)')


cbar = fig.colorbar(sm, shrink=0.85, anchor=(0.0,0.0), ax=ax1)
cbar.set_label(r'$\Omega h^2$')

ax1.set(xlabel = 'Dark matter '+DM_name+' mass [GeV]', ylabel = coupling_name,
        xlim=[0,100], ylim=[-1,1])

for i in range(len(domin_process_list)):
    if domin_process_list[i] != 'non' and len(mass_coup_domin[i][0])>1:
        ax2.scatter(mass_coup_domin[i][0],mass_coup_domin[i][1], label = domin_process_list[i], color = color_lst[i], s=10)
    
ax2.legend(loc='lower center', ncol=4, bbox_to_anchor=(-0.25, -0.7))

ax2.set(xlabel = 'Dark matter '+DM_name+' mass [GeV]',
        xlim=[0,100], ylim=[-1,1])

#saving the plots
fig.savefig(analysis_path+'/'+'relic_run_'+run+'_1_'+str(d1)+'_'+str(d2)+'.png', dpi=300, bbox_inches='tight')
fig.show()
