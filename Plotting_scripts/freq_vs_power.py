import numpy as np
import matplotlib.pyplot as plt

# Dataset
x = np.array([4.104, 4.4498, 4.7621, 5.0440, 5.3071, 5.5430, 5.7567, 5.9496, 6.1117])
y = np.array([0.385, 0.486, 0.602, 0.722, 0.859, 1.008, 1.167, 1.3384, 1.518])

# Plotting the Graph
plt.plot(x, y,)
plt.plot(x, y,'o')

plt.title("Frequency VS Power(mW) @ 0V Vcntrl")
plt.xlabel("Frequency(Ghz)")
plt.ylabel("Power(mW)")
plt.show()