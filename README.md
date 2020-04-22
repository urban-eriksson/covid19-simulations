# What is herd immunity

Herd immunity is a term for the situation when an infectious disease shows a declining spread due to the fact that a sufficient large percentage of a population is immune to the infection. The percentage required to reach herd immunity is not some fixed percentage. It is furthermore not solely given by R0, the reproduction number of the particular disease, as measured in a population at the early stages of an epidemic. Instead, the percentage required to reach herd immunity is only dependent on the effective reproduction number, Re, at a specific point in time. The Re can be broken down into serveral contributing factors. First we have the R0, how contagious the disease is, is the starting point, but then there are several other things which influence Re, like social distancing, washing hands, wearing masks, contact tracing and so on. These measures will affect how large percentage will be required to reach herd immunity, and if the measures are effective enough this percentage will go towards zero. An application has been developed to show the effect on how many infected and deceased there will be in total depending on what measures are taken and how effective they are assumed to be.

# covid19-simulations
Different approaches for the simulation of spread and decline of covid19

## The SEIRID model

A somewhat simplified model in (seird2.py) used in simulations2.py. Some parameters are fitted to data while other can be given.

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/model1.png">
</p>

## Simulations using SEIRD model (simulations1.py)

These simulations for Sweden point towards herd immunity and a high infected-to-confirmed ratio (ICR) of about x100. Actually the model needs to be updated to reflect a time varying R factor to avoid that.

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/seird3.png">
</p>

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/seird2.png">
</p>

<p align="center"> 
<img src="https://github.com/urban-eriksson/covid19-simulations/blob/master/images/sweden1.png">
</p>


First commit simple_sir. Visual studio code project

Todo: incubation time, proximity factor (1-dimensional?), fit parameters to real data. 
- Probably there is a need take into account the probability for an infected person to be identified as "confirmed".
- The R0 is definitely a function of time. One can for simplicity have two values. One before and one after lockdown.

## SEIRD model

Susceptible-Exposed-Infectious-Recovered-Deceased

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
