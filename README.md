# Masters thesis
This repository contains the files used for my Masters thesis project on simulating processes from the Scotogenic model for dark matter and neutrino masses.

## Abstract

This thesis discusses the Minimal Scotogenic Model (MScM) which provides a solution to small neutrino masses as well as dark matter candidates. The model adds an inert scalar doublet and right-handed Majorana fermion singlets with three generations. The neutrino masses in the model are generated via one-loop interactions with the new particles of the model. The model provides different scenarios for dark matter depending on the mass hierarchy. The first studied scenario is where the neutral real component of the inert doublet is the lightest particle in the model, thus the dark matter candidate and the second is where the three fermion generations are the dark matter candidates. Upon examining the new interactions from the new physics extension, we find that the dark matter candidate in either case interacts weakly with the standard model particles, thus we are able to classify these cases as weakly interacting massive particles. The model's parameter space is confined with theoretical constraints on vacuum stability and perturbativity and from measurements of relic abundance as well as from direct detection experiments. The experiment of interest is the CRESST experiment. To test the parameter space of the model, simulations are to calculate the relic abundance and the dark matter-nucleon scattering cross section (relevant for direct detection). Specifically of interest is the low mass region [1,100] GeV. The simulations result in exclusion plots on the parameters of the model and indicate that the model is viable.


## Files
* analysis.py : Python code to generate exclusion plots for the analysis of the results.
* PDG_MC_numbering.txt : a .txt file with the PDG codes of the SM and MScM particles used in analysis.py.
* MScM_eta : LO UFO formatted file for the model with $\eta^0_R$ as the dark matter candidate.

**Note**
See thesis Appendix E for how the UFO files are generate for LO and NLO calculations.
