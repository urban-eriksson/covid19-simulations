# R0 - the reproduction number

R0 is the basic reproduction number: how many persons will on average an infectious person infect, given that nobody in the population is immune (everyone is susceptible). R0 is dependent on several factors such as the how infectious the virus itself is, how many social interactions persons have, and what measures are taken to avoid the spread of the disease. What is not taken into account is that different people behave very differently, and this can have a huge impact on the dynamics of the spread of a disease.

For example, compare two persons, one who has many social interactions and one who is self isolating. It is quite obvisous that the person who has many social interactions also has a higher R0 than the other person. If we take this one step further it can also be assumed that the person who has many social interactions will more likely infect another person who has many social interactions. Therefore it is not enough just to consider R0 for a single person. It is hypothesized that the spreading can be modeled by ... of R0 for the "infecter" and the "infectee". The different R0:s can be assigned to groups of people with similar characteristics, and simulations can be run to see how this looks in a theoretical case.


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

# What is herd immunity

Herd immunity is a term for the situation when an infectious disease shows a declining spread due to the fact that a sufficient large percentage of a population is immune to the infection. The percentage required to reach herd immunity is not some fixed percentage. It is furthermore not solely given by R0 at the beginning of an epidemic. Instead, the projected percentage required to reach herd immunity is only dependent on the current reproduction number, R, at a specific point in time. The R can be broken down into serveral contributing factors, like social distancing, washing hands, wearing masks, contact tracing and so on. These measures will affect how large percentage will be required to reach herd immunity, and if the measures are effective enough this percentage will go towards zero. A possible project is to develop an application to show the effect on how many infected and deceased there will be in total depending on what measures are taken and how effective the measures are assumed to be in reducing R0.
