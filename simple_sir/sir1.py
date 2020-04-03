import matplotlib.pyplot as plt 
import numpy as np 


# https://www.maplesoft.com/applications/download.aspx?SF=127836/SIRModel.pdf

n_days = 40
R0 = 2 # How many in total will a person infect if everyone is susceptible 
effective_infective_duration = 2 # For what duration will the infection period be
beta = R0 / 2
gamma = 1 / effective_infective_duration

infectives = [0.001]
susceptibles = [1 - infectives[-1]]
removed = [0]
checksum = [1]
days = [0]


t = 0
dt = 0.1
while t < n_days:

    new_infected = beta * infectives[-1] * susceptibles[-1] * dt
    recovered =  gamma * infectives[-1] * dt

    susceptibles.append(susceptibles[-1] - new_infected)
    infectives.append(infectives[-1] + new_infected  - recovered)
    removed.append(removed[-1] + recovered)
    checksum.append(infectives[-1] + removed[-1] + susceptibles[-1])
    t = t + dt
    days.append(t)

plt.plot(days, susceptibles, days, infectives,days, removed,  days, checksum)
plt.legend(('Susceptible', 'Infected', 'Recovered', 'Sum'))
plt.xlabel('Day')
plt.ylabel('Fraction')
plt.title('SIR simulation')
plt.show()
