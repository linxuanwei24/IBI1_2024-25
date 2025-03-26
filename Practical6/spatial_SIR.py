# import necessaary libiraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100 , 100))
outbreak = np.random.choice(range(100) , 2)
population[outbreak[0] , outbreak[1]]  = 1

# heat map
plt.figure(figsize = (6 , 4) , dpi = 150)
plt.imshow(population , cmap = "viridis" , interpolation = "nearest")
plt.show()

# define basic variables
N = 10000     # population
beta = 0.3    # infection probability
gamma = 0.05  # recovery probability

Timepoint = [10 , 40 , 50]
for timepoint in Timepoint:
    for i in range (timepoint):
        rows, cols = np.where(population == 1)
        infected_number = len(rows)
        for j in range (infected_number):
            b = np.random.choice(range(2) , 1 , p = [1 - gamma , gamma])
            b = int(b)
            population[rows[j] , cols[j]] += b # recovered = 2
        
            # four corners
            if rows[j] == 0 and cols[j] == 0:
                a = np.random.choice(range(2) , 3 , p = [1 - beta , beta])
                if population[1 , 0] == 0:
                    population[1 , 0] += a[0]
                if population[0 , 1] == 0:
                    population[0 , 1] += a[1]
                if population[1 , 1] == 0:
                    population[1 , 1] += a[2]
            elif rows[j] == 0 and cols[j] == 99:
                a = np.random.choice(range(2) , 3 , p = [1 - beta , beta])
                if population[1 , 99] == 0:
                    population[1 , 99] += a[0]
                if population[1 , 98] == 0:
                    population[1 , 98] += a[1]
                if population[0 , 98] == 0:
                    population[0 , 98] += a[2]
            elif rows[j] == 99 and cols[j] == 0:
                a = np.random.choice(range(2) , 3 , p = [1 - beta , beta])
                if population[99 , 1] == 0:
                    population[99 , 1] += a[0]
                if population[98 , 0] == 0:
                    population[98 , 0] += a[1]
                if population[98 , 1] == 0:
                    population[98 , 1] += a[2]
            elif rows[j] == 99 and cols[j] == 99:
                a = np.random.choice(range(2) , 3 , p = [1 - beta , beta])
                if population[99 , 98] == 0:
                    population[99 , 98] += a[0]
                if population[98 , 98] == 0:
                    population[99 , 98] += a[1]
                if population[98 , 99] == 0:
                    population[98 , 99] += a[2]
            # the uppest row
            elif rows[j] == 0:
                a = np.random.choice(range(2) , 5 , p = [1 - beta , beta])
                if population[rows[j] , cols[j] + 1] == 0:
                    population[rows[j] , cols[j] + 1] += a[0]
                if population[rows[j] , cols[j] - 1] == 0:
                    population[rows[j] , cols[j] - 1] += a[1]
                if population[rows[j] + 1 , cols[j]] == 0:
                    population[rows[j] + 1 , cols[j]] += a[2]
                if population[rows[j] + 1 , cols[j] - 1] == 0:
                    population[rows[j] + 1 , cols[j] - 1] += a[3]
                if population[rows[j] + 1 , cols[j] + 1] == 0:
                    population[rows[j] + 1 , cols[j] + 1] += a[4]
            # the lowest row
            elif rows[j] == 99:
                a = np.random.choice(range(2) , 5 , p = [1 - beta , beta])
                if population[rows[j] , cols[j] + 1] == 0:
                    population[rows[j] , cols[j] + 1] += a[0]
                if population[rows[j] , cols[j] - 1] == 0:
                    population[rows[j] , cols[j] - 1] += a[1]
                if population[rows[j] - 1 , cols[j]] == 0:
                    population[rows[j] - 1 , cols[j]] += a[2]
                if population[rows[j] - 1 , cols[j] - 1] == 0:
                    population[rows[j] - 1 , cols[j] - 1] += a[3]
                if population[rows[j] - 1 , cols[j] + 1] == 0:
                    population[rows[j] - 1 , cols[j] + 1] += a[4]
            # the left column
            elif cols[j] == 0:
                a = np.random.choice(range(2) , 5 , p = [1 - beta , beta])
                if population[rows[j] + 1 , cols[j]] == 0:
                    population[rows[j] + 1 , cols[j]] += a[0]
                if population[rows[j] - 1 , cols[j]] == 0:
                    population[rows[j] - 1 , cols[j]] += a[1]
                if population[rows[j] , cols[j] + 1] == 0:
                    population[rows[j] , cols[j] + 1] += a[2]
                if population[rows[j] + 1 , cols[j] + 1] == 0:
                    population[rows[j] + 1 , cols[j] + 1] += a[3]
                if population[rows[j] - 1 , cols[j] + 1] == 0:
                    population[rows[j] - 1 , cols[j] + 1] += a[4]
            # the right column
            elif cols[j] == 99:
                a = np.random.choice(range(2) , 5 , p = [1 - beta , beta])
                if population[rows[j] + 1 , cols[j]] == 0:
                    population[rows[j] + 1 , cols[j]] += a[0]
                if population[rows[j] - 1 , cols[j]] == 0:
                    population[rows[j] - 1 , cols[j]] += a[1]
                if population[rows[j] , cols[j] - 1] == 0:
                    population[rows[j] , cols[j] - 1] += a[2]
                if population[rows[j] + 1 , cols[j] - 1] == 0:
                    population[rows[j] + 1 , cols[j] - 1] += a[3]
                if population[rows[j] - 1 , cols[j] - 1] == 0:
                    population[rows[j] - 1 , cols[j] - 1] += a[4]
            # middle, has 8 neighbors
            else:
                a = np.random.choice(range(2) , 8 , p = [1 - beta , beta])
                if population[rows[j] - 1 , cols[j] - 1] == 0:
                    population[rows[j] - 1 , cols[j] - 1] += a[0]
                if population[rows[j] - 1 , cols[j]] == 0:
                    population[rows[j] - 1 , cols[j]] += a[1]
                if population[rows[j] - 1 , cols[j] + 1] == 0:
                    population[rows[j] - 1 , cols[j] + 1] += a[2]
                if population[rows[j] , cols[j] - 1] == 0:
                    population[rows[j] , cols[j] - 1] += a[3]
                if population[rows[j] , cols[j] + 1] == 0:
                    population[rows[j] , cols[j] + 1]+= a[4]
                if population[rows[j] + 1 , cols[j] - 1] == 0:
                    population[rows[j] + 1 , cols[j] - 1] += a[5]
                if population[rows[j] + 1 , cols[j]] == 0:
                    population[rows[j] + 1 , cols[j]] += a[6]
                if population[rows[j] + 1 , cols[j] + 1] == 0:
                    population[rows[j] + 1 , cols[j] + 1] += a[7]

    plt.figure(figsize = (6 , 4) , dpi = 150)
    plt.imshow(population , cmap = "viridis" , interpolation = "nearest")
    plt.show()