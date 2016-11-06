# Assn 1

## Project Directory
```
/Comp366/Assn1/
├── DoubleQ.py  -- Part 2 of the assn
├── README.md
├── __pycache__
│   ├── DoubleQ.cpython-33.pyc
│   ├── blackjack.cpython-33.pyc
│   └── randomPolicy.cpython-33.pyc
├── blackjack.pdf  -- Project description
├── blackjack.py  -- Helper functions for writing this project
├── collaborator.txt
├── doc  -- Charts of our observed returns
│   ├── averageVsAlphaChart.png
│   ├── averageVsAlphaMultiChart.png
│   ├── averageVsEpsChart.png
│   └── averageVsEpsMultiChart.png
├── multiscript.py  -- Our multi-threaded implementation of running DoubleQ
├── niceScript.sh  -- A way to start script.py with nice 19 (for running on lab machines)
├── outputs  -- Our recorded data from running DoubleQ (csv's with eps,alpha,avg return)
│   ├── multioutput(1k).txt
│   ├── multioutput(1mil).txt
│   ├── output(100k).txt
│   └── output(1mil).txt
├── part3.txt  -- One of the deliverables (our best run of DoubleQ after tuning the params)
├── policy.txt  -- A print out of the policy (when to hit and when to stick)
├── randomPolicy.py  -- Part 1 of the assn
└── script.py  -- Single threaded running of DoubleQ

3 directories, 22 files
```

## What we did to find the best return
1. We ran 100k episodes to test out our scripts
  1. eps [0,1] w/ increments of 0.1
  1. alpha [0.001, 2) w/ increments of 0.1
1. We ran script.py for 220 different combinations of eps & alpha
  1. eps [0,1] w/ increments of 0.1
  1. alpha [0.001, 2) w/ increments of 0.1
1. We ran multiscript.py for 180 different combinations of eps & alpha
  1. eps [0.5,1] w/ increments of 0.1
  1. alpha [0.00001,0.001) w/ increments of 0.000033


## Graphs
![averageVsAlphaChart](/doc/averageVsAlphaChart.png?raw=true "Alpha")
![averageVsAlphaMultiChart](/doc/averageVsAlphaMultiChart?raw=true "Alpha Multi")
![averageVsEpsChart](/doc/averageVsEpsChart?raw=true "Eps")
![averageVsEpsMultiChart](/doc/averageVsEpsMultiChart?raw=true "Eps Multi")

