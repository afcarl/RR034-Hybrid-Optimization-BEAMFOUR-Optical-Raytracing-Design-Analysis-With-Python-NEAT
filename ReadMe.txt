
Hybrid Optimization BEAMFOUR Optical Raytracing Design & Analysis w/ Python-NEAT:

A hybrid optimization of an optical raytracing design and analysis of a reflective based LED array point focus system is developed. Using NeuroEvolution of Augmenting Topologies (NEAT), a form of genetic algorithm reinforcement learning, is utilized in combination with a modified version of the BEAMFOUR optical raytracing design and analysis program's internal unconstrained optimizer. The AutoIt script language was used to automate the BEAMFOUR interactive mouse picks, all under Python control.

Overview of Operation Video: https://youtu.be/D6gi2aUchEU

Pre-Requisits/Reference:

1. "BEAMFOUR": http://www.stellarsoftware.com/, https://github.com/StellarSoftwareBerkeley/BeamFour/tree/master
2. "Python-NEAT": https://github.com/CodeReclaimers/neat-python
3. "NEAT" algorithm: https://en.wikipedia.org/wiki/Neuroevolution_of_augmenting_topologies, https://www.cs.ucf.edu/~kstanley/neat.html
4. "AutoIt": https://www.autoitscript.com/site/
5. "Netbeans": https://netbeans.org/


Operation: ./0_test/evolve_BEAM4_e.py


*****************************************************
START: Example of "INPUT.OPT" Input:
*****************************************************
 3 surfaces INPUT.OPT (RMS=x.xxx)
   X         Y         Z       Pitch :   type?     Diam     OffOx      Curv     Asph     f
--------:---------:---------:---------:--------:---------:---------:---------:---------:----:--
   0    :   0.0   :    6.3  :  17.2022? Mirror :         :         :  -0.1670: -70.1537: S  :
   0    :   0.0   :   -5.0  :-201.2879: Mirror :         :         :  -0.0440:  -0.0007:    :
   0    :   0.0   :   50.0  :    0    :        :   100   :         :    0    :    0    :    :
*****************************************************
END: Example of "INPUT.OPT" Input:
*****************************************************


*****************************************************
START: Example of "INPUT.RAY" Input:
*****************************************************
  656 rays    INPUT.RAY (RMS=x.xxx)
     X0      Z0       W0         U0        @wave1       Xgoal      Xfinal       notes
---------:-------:----------:-----------:----------:------------:------------:----------:--
   -0.05 :  0.0  :  1.0000  :   0.0000  :          r   -35.0    :  -43.843284:OK 3      :
   -0.05 :  0.0  :  0.9998  :  -0.0175  :          r   -35.0    :  -43.629640:OK 3      :
   -0.05 :  0.0  :  0.9994  :  -0.0349  :          r   -35.0    :  -43.301612:OK 3      :
... (content removed) ...
   -2.35 :  0.0  :  0.9613  :   0.2756  :          y   -35.0    :  -46.958323:OK 3      :
   -2.35 :  0.0  :  0.9563  :   0.2924  :          y   -35.0    :  -47.830311:OK 3      :
   -2.35 :  0.0  :  0.9511  :   0.3090  :          y   -35.0    :  -48.692712:OK 3      :
*****************************************************
END: Example of "INPUT.RAY" Input:
*****************************************************


*****************************************************
START: Example of Output:
*****************************************************
Done
Iteration = 13
RMS Average =    7.16E00
Nrays = 652
Ngoals = 1
Nterms = 652
Nadj = 1
*****************************************************
END: Example of Output:
*****************************************************

