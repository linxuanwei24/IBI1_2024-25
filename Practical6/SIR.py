# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define basic variables
N = 10000     # population
beta = 0.3    # infection probability
gamma = 0.05  # recovery probability
Susceptible = [9999]
Infected = [1]
Recovered = [0]

# for each loop:
# get the number of people of S/I/R from the former loop
# infected_probability = infected / 10000 * beta
# create two variables new_infected and new_recovered as counter
# choose "susceptible" times randomly, count the new infected
# chosse "infectd" times randomly, count the new recovered
# calculate the S/I/R in this loop, add them to each's array
for i in range (1000):
    susceptible = Susceptible[i]
    infected = Infected[i]
    recovered = Recovered[i]
    infected_probability = infected / 10000 * beta
    new_infected , new_recovered = 0 , 0
    for j in range (susceptible):
        a = np.random.choice(range(2) , 1 , p = [1 - infected_probability , infected_probability])
        a = int(a)
        new_infected += a
    for j in range (infected):
        b = np.random.choice(range(2) , 1 , p = [1 - gamma , gamma])
        b = int(b)
        new_recovered += b
    infected = infected + new_infected - new_recovered
    recovered = recovered + new_recovered
    susceptible = N - infected - recovered
    Susceptible.append(susceptible)
    Infected.append(infected)
    Recovered.append(recovered)

# plot the results
plt.plot(Susceptible , label = "Susceptible")
plt.plot(Infected , label = "Infected")
plt.plot(Recovered , label = "Recovered")
plt.legend()
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.show()