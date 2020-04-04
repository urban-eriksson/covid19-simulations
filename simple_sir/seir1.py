import matplotlib.pyplot as plt 
import numpy as np 

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




# https://www.maplesoft.com/applications/download.aspx?SF=127836/SIRModel.pdf

R0 = 2 # How many in total will a person infect if everyone is susceptible 
effective_infectious_duration = 2 # For what duration will the infection period be
beta = R0 / effective_infectious_duration
gamma = 1 / effective_infectious_duration

incubation_period = 5
dt = 0.1
incubator = Incubator(incubation_period, dt)

# Test of the incubator (it is perhaps shifted by dt)
# infectious = [0] 
# incubator.add_exposed(1)
# newly_infected = [0]
# n_days = 12
# t = 0
# while t < n_days:

#     infectious.append(infectious[-1] + incubator.get_infected())
#     newly_infected.append(incubator.get_infected() / dt)
#     incubator.add_exposed(0)
#     t = t + dt
#     days.append(t)

# plt.plot(days, infectious, days, newly_infected)
# plt.legend(('Total infected','Newly infected per day'))
# plt.xlabel('Day')
# plt.ylabel('Fraction')
# plt.show()


# seed values
exposed = [0.001]
incubator.add_exposed(exposed[0])
infectious = [0] 
susceptibles = [1 - exposed[0]]
recovered = [0]
checksum = [1]
days = [0]

n_days = 120
t = 0
while t < n_days:

    new_exposed = beta * infectious[-1] * susceptibles[-1] * dt
    new_infected = incubator.get_infected()
    new_recovered = gamma * infectious[-1] * dt

    susceptibles.append(susceptibles[-1] - new_exposed)
    infectious.append(infectious[-1] + new_infected  - new_recovered)
    recovered.append(recovered[-1] + new_recovered)
    incubator.add_exposed(new_exposed)
    exposed.append(incubator.get_exposed())
    checksum.append(infectious[-1] + recovered[-1] + susceptibles[-1] + exposed[-1])
    t = t + dt
    days.append(t)

plt.plot(days, susceptibles, days, exposed, days, infectious,days, recovered,  days, checksum)
plt.legend(('Susceptible', 'Exposed', 'Infected', 'Recovered', 'Sum'))
plt.xlabel('Day')
plt.ylabel('Fraction')
plt.title('SEIR simulation')
plt.show()
