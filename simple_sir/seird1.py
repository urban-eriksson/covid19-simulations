import matplotlib.pyplot as plt 
import numpy as np 

# The latency period of exposed before getting infectous
class IncubatorSimple:
    def __init__(self, incubation_time, dt):
        N = int(incubation_time  / dt) + 1
        self._queue = np.zeros(N)

    def get_infected(self):
        return sum(self._queue[0])

    def get_exposed(self):
        return sum(self._queue)

    def add_exposed(self, fraction):
        self._queue = np.append(self._queue[1:], fraction)


# The latency period of exposed before getting infectous
class Incubator:
    def __init__(self, mu, dt, sigma=None):
        if not sigma:
            sigma = mu / 2
        N = int(mu  / dt)
        self._t = np.linspace(0, 2*mu, 2*N+1)
        self._envelope = np.exp(-0.5 * (self._t-mu)**2 / sigma**2)
        self._envelope = self._envelope / sum(self._envelope)
        #plt.plot(self._t,self._envelope)
        #plt.show()

        self._queue = np.zeros(2*N+1)

    def get_infected(self):
        return sum(self._envelope * self._queue)

    def get_exposed(self):
        return sum(self._queue * np.cumsum(self._envelope))

    def add_exposed(self, fraction):
        self._queue = np.append(self._queue[1:], fraction)


# Lethally infected enters here at the moment they are infected 
# determined by the cfr (case fatality rate)
class Decimator:
    def __init__(self, mu, dt, sigma=None):
        if not sigma:
            sigma = mu / 2
        N = int(mu  / dt)
        self._t = np.linspace(0, 2*mu, 2*N+1)
        self._envelope = np.exp(-0.5 * (self._t-mu)**2 / sigma**2)
        self._envelope = self._envelope / sum(self._envelope)

        self._queue = np.zeros(2*N+1)

    def get_deceased(self):
        return sum(self._envelope * self._queue)

    # i.e. People treated in ICU etc. It can be made part of the infectous or not
    def get_infected(self):
        return sum(self._queue * np.cumsum(self._envelope))

    def add_infected(self, fraction):
        self._queue = np.append(self._queue[1:], fraction)

class DecimatorSimple:
    def __init__(self, time_to_death, dt):
        N = int(time_to_death  / dt) + 1
        self._queue = np.zeros(N)

    def get_deceased(self):
        return sum(self._queue[0])

    # i.e. People treated in ICU etc. It can be made part of the infectous or not
    def get_infected(self):
        return sum(self._queue)

    def add_infected(self, fraction):
        self._queue = np.append(self._queue[1:], fraction)



# https://www.maplesoft.com/applications/download.aspx?SF=127836/SIRModel.pdf

R0 = 2 # How many in total will a person infect if everyone is susceptible 
CFR = 0.04 # case fatality rate if defined as how many of confirmed will die
MTD = 15 # mean time to death from showing infection
ICR = 0.2 # infected to confirmed ratio
initially_exposed = 0.001

effective_infectious_duration = 2 # For what duration will the infection period be
beta = R0 / effective_infectious_duration
gamma = 1 / effective_infectious_duration
incubation_period = 5
dt = 0.1
incubator = Incubator(incubation_period, dt)
decimator = Decimator(MTD, dt)

# seed values
days = [0]
exposed = [initially_exposed]
incubator.add_exposed(exposed[0])
infectious = [0] 
susceptibles = [1 - exposed[0]]
recovered = [0]
confirmed = [0]
dailyconfirmed = [0]
icutreatment = [0]
deceased = [0]
dailydeceased = [0]
checksum = [1]

n_days = 120
t = 0
while t < n_days:

    new_exposed = beta * infectious[-1] * susceptibles[-1] * dt
    new_infected = incubator.get_infected()
    new_recovered = gamma * infectious[-1] * dt
    new_deceased = decimator.get_deceased()

    susceptibles.append(susceptibles[-1] - new_exposed)
    infectious.append(infectious[-1] + (1 - CFR * ICR) * new_infected  - new_recovered)   
    recovered.append(recovered[-1] + new_recovered)
    incubator.add_exposed(new_exposed)
    exposed.append(incubator.get_exposed())
    decimator.add_infected(CFR * ICR * new_infected) 
    deceased.append(deceased[-1] + new_deceased)
    icutreatment.append(decimator.get_infected()) # todo, number in icu treament are higher than will be deceased

    confirmed.append(confirmed[-1] + ICR * new_infected)
    dailyconfirmed.append(ICR * new_infected) 
    dailydeceased.append(new_deceased)


    checksum.append(infectious[-1] + recovered[-1] + susceptibles[-1] + exposed[-1] + deceased[-1] + icutreatment[-1])
    t = t + dt
    days.append(t)

plt.subplot(3, 1, 1)
plt.plot(days, susceptibles, days, recovered, days, checksum)
plt.legend(['Susceptible','Recovered', 'Checksum'])
plt.xlabel('Days')
plt.ylabel('Fraction')
plt.title('SEIRD simulation')

plt.subplot(3, 1, 2)
plt.plot(days, exposed, days, infectious)
plt.legend(['Exposed', 'Infectous'])
plt.xlabel('Days')
plt.ylabel('Fraction')

plt.subplot(3, 1, 3)
plt.plot(days, icutreatment, days, deceased)
plt.legend(['In ICU treatment', 'Deceased'])
plt.xlabel('Days')
plt.ylabel('Fraction')

plt.show()

Ntotal = 1e7

plt.subplot(2, 1, 1)
plt.plot(days, [Ntotal*x for x in dailyconfirmed])
plt.legend(['Daily confirmed'])
plt.xlabel('Days')
plt.ylabel('Count')
plt.title(f'Ntotal={Ntotal:e}')

plt.subplot(2, 1, 2)
plt.plot(days, [Ntotal*x for x in dailydeceased],'r')
plt.legend(['Daily deceased'])
plt.xlabel('Days')
plt.ylabel('Count')

plt.show()
