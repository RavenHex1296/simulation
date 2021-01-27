import matplotlib.pyplot as plt

susceptible = 1000
infected = 1
recovered = 0
susceptible_values = []
infected_values = []
recovered_values = []
times = []

for n in range(226):
    times.append(n)
    times.append(n + 0.5)

def clone(n):
    cloned_value = 0
    return cloned_value + n

for _ in range(len(times)):
    susceptible_values.append(susceptible)
    infected_values.append(infected)
    recovered_values.append(recovered)

    cloned_susceptible = clone(susceptible)
    cloned_infected = clone(infected)
    
    susceptible += -0.0003 * cloned_susceptible * cloned_infected
    infected += 0.0003 * cloned_susceptible * cloned_infected - 0.02 * infected
    recovered += 0.02 * cloned_infected

plt.style.use('bmh')
plt.plot(times, susceptible_values, label='Number of susceptible people')
plt.plot(times, infected_values, label='Number of infected people')
plt.plot(times, recovered_values, label='Number of recovered people')
plt.legend(loc='best')
plt.xlabel('Time Passed')
plt.ylabel('Susceptible/Infected/Recovered People')
plt.savefig('sir_model.png')
