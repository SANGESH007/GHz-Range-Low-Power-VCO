import numpy as np
import matplotlib.pyplot as plt

# Dataset
x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([4.7621, 4.7096, 4.6397, 4.5658, 4.4714, 4.3740, 4.2653, 4.1615, 4.0568, 3.9660, 3.8902  ])

# Plotting the Graph
plt.plot(x, y,)
plt.plot(x, y,'o')

plt.title("Frequency VS Vcntrl @ 1.8V VDD")
plt.xlabel("Vcntrl")
plt.ylabel("Frequency(Ghz)")
plt.show()
