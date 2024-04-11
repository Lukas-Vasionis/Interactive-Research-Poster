import pandas as pd
import numpy as np

def get_data_temp_cicles_box():
    # Circles of Hell
    circles = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']

    # Simulated average temperatures for each circle (excluding the 8th circle and special case for the 9th)
    temperatures=np.array([45,120,200,320,500,666,880, None, -200], dtype=float)

    # temperatures = np.random.uniform(low=45, high=900, size=8)
    # temperatures = np.insert(temperatures, 7, np.nan)  # Inserting NaN for the 8th circle as it has no data
    # temperatures[-1] = -200  # Setting the 9th circle's temperature
    #
    # Simulating the 1st and 3rd quartiles as varying from 0.5 to 1.5 standard deviations from the mean
    # Assuming a standard deviation range for the sake of demonstration
    std_dev_range = np.random.uniform(0.5, 2, size=(8, 2))

    std_dev_range = np.insert(std_dev_range, 7, [np.nan, np.nan], axis=0)  # For the 8th circle
    q1 = temperatures - std_dev_range[:, 0] * 50  # Arbitrary deviation for quartiles
    q3 = temperatures + std_dev_range[:, 1] * 50
    # Shaping data into a pandas DataFrame
    data = {
        'Circle': circles,
        'Temperature': temperatures,
        '1st Quartile': q1,
        '3rd Quartile': q3
    }

    df = pd.DataFrame(data)
    print(df.to_string())
    df.to_csv('outputs/data_temp_cicles_box.tsv', sep='\t', index=False)
get_data_temp_cicles_box()