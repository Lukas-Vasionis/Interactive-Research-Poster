import pickle

import pandas as pd
import numpy as np


def get_data_temp_cicles_box():
    # Circles of Hell
    circles = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']

    # Simulated average temperatures for each circle (excluding the 8th circle and special case for the 9th)
    temperatures = np.array([45, 120, 200, 320, 500, 666, 880, None, -300], dtype=float)

    # temperatures = np.random.uniform(low=45, high=900, size=8)
    # temperatures = np.insert(temperatures, 7, np.nan)  # Inserting NaN for the 8th circle as it has no data
    # temperatures[-1] = -200  # Setting the 9th circle's temperature
    #
    # Simulating the 1st and 3rd quartiles as varying from 0.5 to 1.5 standard deviations from the mean
    # Assuming a standard deviation range for the sake of demonstration
    std_dev_range = np.random.uniform(0.5, 4, size=(8, 2))

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
    df.loc[:, 'lowerfence'] = df['1st Quartile'] - abs(df['1st Quartile'] * np.random.uniform(0.5, 0.1))
    df.loc[:, 'upperfence'] = df['3rd Quartile'] + abs(df['3rd Quartile'] * np.random.uniform(0.5, 0.1))

    df.to_csv('outputs/data_temp_cicles_box.tsv', sep='\t', index=False)


def get_data_spectra_cicles_box():
    # Reinitialize data due to execution state reset, then create a DataFrame
    x = np.linspace(200, 800, 600)  # Wavelength range

    def gaussian(x, mu, sigma, amplitude):
        return amplitude * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

    # Common compounds across some circles
    common_compound1 = gaussian(x, 300, 30, 1)
    common_compound2 = gaussian(x, 500, 35, 0.9)
    common_compound3 = gaussian(x, 650, 20, 1.2)

    # Define spectral data for each circle with unique and common peaks
    circles_data = {
        '1st': common_compound1 + gaussian(x, 220, 30, 0.7) + gaussian(x, 720, 25, 0.5),
        '2nd': common_compound2 + gaussian(x, 280, 25, 0.9) + gaussian(x, 400, 40, 0.8),
        '3rd': common_compound3 + gaussian(x, 350, 30, 1.1) + gaussian(x, 450, 25, 1.0),
        '4th': common_compound1 + common_compound2 + gaussian(x, 750, 30, 0.7),
        '5th': common_compound2 + gaussian(x, 330, 20, 1.1) + gaussian(x, 570, 25, 0.9),
        '6th': common_compound3 + gaussian(x, 380, 30, 1.2) + gaussian(x, 460, 35, 0.8),
        '7th': common_compound1 + common_compound3 + gaussian(x, 620, 20, 1.0),
        '8th': common_compound2 + common_compound3 + gaussian(x, 250, 25, 1.0),
        '9th': common_compound1 + gaussian(x, 540, 20, 1.3) + gaussian(x, 600, 35, 0.9),
    }

    # Create a DataFrame to store the data for the 9 circles of hell
    df_circles = pd.DataFrame(data={
        'Wavelength': x,
        '1st': circles_data['1st'],
        '2nd': circles_data['2nd'],
        '3rd': circles_data['3rd'],
        '4th': circles_data['4th'],
        '5th': circles_data['5th'],
        '6th': circles_data['6th'],
        '7th': circles_data['7th'],
        '8th': circles_data['8th'],
        '9th': circles_data['9th']
    })
    df_circles.to_csv("outputs/data_spectra_cicles_box.tsv", "\t", index=False)


    return df_circles


def get_data_heatmap_creature_counts(rows=30, cols=9):
    np.random.seed(45)  # For reproducibility
    matrix = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        main_circle = np.random.randint(0, cols)
        # Adjust the main count to ensure there's enough room for another >300 count
        main_count = int(np.random.uniform(0.7, 0.85) * 666)  # Reduce upper limit to 85%

        matrix[i, main_circle] = main_count

        remaining_count = 666 - main_count
        high_count_circle = np.random.choice([j for j in range(cols) if j != main_circle])
        # Ensure there's at least 301 for the high count
        high_count = np.random.randint(301, max(302, remaining_count))  # Ensure high_count is viable
        matrix[i, high_count_circle] = high_count

        remaining_count -= high_count
        if remaining_count > 0:
            other_counts = np.random.multinomial(remaining_count, np.ones(cols) / cols)
            other_counts[main_circle] = 0  # Reset the main circle to prevent double counting
            other_counts[high_count_circle] = 0  # Reset the high count circle to prevent double counting
            matrix[i] += other_counts

    matrix=np.array(matrix)
    with open("outputs/data_heatmap_creature_counts.pickle", 'wb') as f:
        pickle.dump(matrix, f, protocol=pickle.HIGHEST_PROTOCOL)
    return matrix
# get_data_heatmap_creature_counts(rows=30, cols=9)