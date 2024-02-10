import matplotlib.pyplot as plt
import numpy as np

# Generate excessive data (replace this with your data)
x = np.arange(0, 10000)
y = np.random.rand(10000)

# Subsample the data for better visualization
subsample_factor = 10
x_subsampled = x[::subsample_factor]
y_subsampled = np.mean(y.reshape(-1, subsample_factor), axis=1)

# Create a scaled graph using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(x_subsampled, y_subsampled, label='Excessive Data', color='blue')
plt.title('Scaled Graph of Excessive Data')
plt.xlabel('Data Points (Subsampled)')
plt.ylabel('Values (Subsampled Mean)')
plt.legend()
plt.show()
