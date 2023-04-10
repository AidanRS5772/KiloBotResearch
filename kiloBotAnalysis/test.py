import numpy as np

# create example data as numpy array
data = np.array([[253.33971292, 18.78947368],
                 [374.33653846, 248.625     ],
                 [373.82874618, 258.02752294],
                 [381.83013699, 245.28493151],
                 [382.95907928, 262.21994885],
                 [389.80689655, 255.9862069 ],
                 [630.17127072, 496.14917127]])

# create a boolean mask to select data points to keep
mask = np.logical_and(data[:,0] <= 600, data[:,1] >= 50)

# use the mask to filter the data
filtered_data = data[mask]

# print the filtered data
print("Filtered data:")
print(filtered_data)
