# covid19-simulations
Different approaches for the simulation of spread and decline of covid19

First commit simple_sir. Visual studio code project

Todo: incubation time, proximity factor (1-dimensional?), fit parameters to real data. 
- Probably there is a need take into account the probability for an infected person to be identified as "confirmed".
- The R0 is definitely a function of time. One can for simplicity have two values. One before and one after lockdown.

## SEIRD model

Susceptible-Exposed-Infectous-Recovered-Deceased

To make a run a few constants need to be specified such as R0, incubation perios, CFR etc.

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/seird.png">
</p>

To get the daily figures in numbers, the total population size needs to be specified. 

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/daily_figures.png">
</p>


## Data read 

From John Hopkins (https://github.com/CSSEGISandData/)

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/data_read_example.png">
</p>
