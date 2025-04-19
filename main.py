import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_steps = 30
D0 = 100
P0 = 2000

# Initialize arrays to store population and density values
D = np.zeros(num_steps)
P = np.zeros(num_steps)

# Initialize initial values
D[0] = D0
P[0] = P0

# Define the dynamics functions
def deer_growth(deer, plants):
    return 1.5 * deer * (plants / 3000)

def deer_decline(deer):
    return 1.1 * deer

def plant_growth(plants):
    return 0.8 * (1 - plants / 3000) * plants

def plant_decline(deer, plants):
    return 1.2 * deer * (plants / 3000)

# Simulate dynamics
for t in range(1, num_steps):
    D[t] = D[t - 1] + deer_growth(D[t - 1], P[t - 1]) - deer_decline(D[t - 1])
    P[t] = P[t - 1] + plant_growth(P[t - 1]) - plant_decline(D[t - 1], P[t - 1])

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps), D, label='Deer Population', color='brown')
plt.plot(range(num_steps), P, label='Plant Density', color='green')
plt.xlabel('Time Steps')
plt.ylabel('Population / Density')
plt.title('Population Dynamics of Deer and Plant Density')
plt.legend()
plt.grid(True)
plt.show()