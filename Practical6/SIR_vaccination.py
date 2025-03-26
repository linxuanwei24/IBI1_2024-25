# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define basic variables
N = 10000     # population
beta = 0.3    # infection probability
gamma = 0.05  # recovery probability
Vaccinated = [0 , 1000 , 2000 , 3000 , 4000 , 5000 , 6000 , 7000 , 8000 , 9000 , 10000]

for vaccinated in Vaccinated:
    Infected = [1]
    Recovered = [0]
    Susceptible = [9999 - vaccinated]

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
        susceptible = N - infected - recovered - vaccinated
        Susceptible.append(susceptible)
        Infected.append(infected)
        Recovered.append(recovered)


    # plot the results
    rate_label = vaccinated / 100
    rate_label = str(rate_label) + "%"
    plt.plot(Infected , label = rate_label)

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()