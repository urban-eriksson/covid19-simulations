import numpy as np 
import matplotlib.pyplot as plt
from read_data import extract_confirmed_deceased
from seird import seird_simulate
from scipy.optimize import minimize

def plot_comparison(official,simulated, titstr):
    plt.subplot(2, 1, 1)
    plt.plot(official['time'], official['confirmed'], simulated['time'], [N*x for x in simulated['confirmed']])
    plt.legend(['Official confirmed','Simulated confirmed'])
    #plt.xlabel('Days')
    plt.ylabel('Count')
    plt.title(titstr)
    plt.subplot(2, 1, 2)
    plt.plot(official['time'], official['deceased'], simulated['time'], [N*x for x in simulated['deceased']])
    plt.legend(['Official deceased','Simulated deceased'])
    plt.xlabel('Days')
    plt.ylabel('Count')
    plt.show()

country = 'Italy'
N = 60.36e6
#country = 'Sweden'
#N = 10.23e6
#country = 'Spain'
#N = 46.94e6
#country = 'United Kingdom'
#N = 66.65e6
#country = 'Germany'
#N = 83.02e6
#country = 'US'
#N = 328.2e6


official = extract_confirmed_deceased(country,N)

initially_exposed = 0.005
R0 = 2.5 # How many in total will a person infect if everyone is susceptible 
ICR = 0.02 # infected to confirmed ratio
CFR = 0.1 # case fatality rate if defined as how many of confirmed will die
MTD = 5 # mean time to death from showing infection

x0 = [initially_exposed, R0, CFR]

Npoints = len(official['time'])
simulated = seird_simulate(x0, Npoints)

plot_comparison(official, simulated, 'Initial conditions')

def loss_function(x):
    simulation = seird_simulate(x,Npoints)
    loss = sum([(c1 / N - c2)**2 for c1, c2 in zip(official['confirmed'], simulation['confirmed'])])
    loss += 10*sum([(d1 / N - d2)**2 for d1, d2 in zip(official['deceased'], simulation['deceased'])])
    print(loss*1e8)
    return loss

xopt = minimize(loss_function, x0, method='Nelder-Mead', tol=1e-6, options={'maxiter': 70})
R0opt = f'{xopt["x"][1]:.3f}'
#ICRopt = f'{xopt["x"][2]:.3f}'
ICRopt = f'{ICR:.3f}'
CFRopt = f'{xopt["x"][2]:.3f}'

print('Final result')
print(xopt['x'])
print('Initally exposed: ' + str(xopt['x'][0]))
print('R0: ' + R0opt)
print('ICR: ' + ICRopt)
print('CFR: ' + CFRopt)
simulated = seird_simulate(xopt['x'], Npoints + 60)

pdata = simulated['plot_data']



plt.subplot(2, 1, 1)
plt.plot(official['time'],official['daily_confirmed'],pdata['time'],[N*x for x in pdata['daily_confirmed']])
plt.legend(['Official daily confirmed','Simulated daily confirmed'])
#plt.xlabel('Days')
plt.ylabel('Count')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(official['time'],official['daily_deceased'],pdata['time'],[N*x for x in pdata['daily_deceased']])
plt.legend(['Official daily deceased','Simulated daily deceased'])
plt.xlabel('Days')
plt.ylabel('Count')
plt.grid()

plt.show()


plot_comparison(official, simulated, 'Country=' + country + ', R0=' + R0opt + ', ICR=' + ICRopt + ', CFR=' + CFRopt )


plt.subplot(3, 1, 1)
plt.plot(pdata['time'], pdata['susceptibles'], pdata['time'], pdata['recovered'])
plt.legend(['Susceptible','Recovered'])
#plt.xlabel('Days')
plt.ylabel('Fraction')

plt.subplot(3, 1, 2)
plt.plot(pdata['time'], pdata['exposed'], pdata['time'], pdata['infectious'])
plt.legend(['Exposed', 'Infectous'])
#plt.xlabel('Days')
plt.ylabel('Fraction')

plt.subplot(3, 1, 3)
plt.plot(pdata['time'], pdata['icutreatment'], pdata['time'], pdata['deceased'])
plt.legend(['In ICU treatment', 'Deceased'])
plt.xlabel('Days')
plt.ylabel('Fraction')

plt.show()


