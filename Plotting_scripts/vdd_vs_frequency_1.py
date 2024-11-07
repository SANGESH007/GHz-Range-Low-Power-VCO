import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt 

# Dataset
x = np.array([1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.6, 3.8, 4, 4.3, 4.6, 4.9, 5 ])
y = np.array([4.104, 4.4498, 4.7621, 5.0440, 5.3071, 5.5430, 5.7567, 5.9496, 6.1117, 6.2546, 6.3620, 6.4736, 6.5956, 6.6800, 6.7824, 6.8481, 6.8920, 6.9506, 7.008, 7.07, 7.13, 7.18, 7.2, 7.15, 6.96, 6.85])

# Create a spline for smoother plotting
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plot the smooth curve
plt.plot(X_, Y_)
plt.plot(x, y, '*')

# Annotate each data point
for (i, j) in zip(x, y):
    plt.text(i, j, f'({i:.1f}, {j:.4f})', fontsize=6, ha='right', va='bottom')

# Labels and title
plt.title("VDD VS Frequency(GHz) @ 0V Vcntrl")
plt.xlabel("VDD")
plt.ylabel("Frequency (GHz)")
plt.legend()
plt.show()
