import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_plotly_events import plotly_events
import streamlit as st
import plotly.graph_objects as go

# topo data "topo data "https://contourmapcreator.urgr8.ch/"

def generate_temperature_data_for_boxplot(temp_average, num_measurements, num_conditions):
    """
    Generate simulated temperature fluctuation data for multiple conditions.

    Parameters:
    - temp_average: The average temperature around which fluctuations occur (can be a single value or a list of values for each condition).
    - num_measurements: The number of temperature measurements to generate per condition.
    - num_conditions: The number of different conditions (e.g., months, locations) to simulate.

    Returns:
    - A 2D numpy array where each row represents the simulated temperature measurements for a condition.
    """
    # Check if temp_average is a single value or a list
    if not isinstance(temp_average, list):
        temp_averages = [temp_average] * num_conditions
    else:
        temp_averages = temp_average

    # Ensure the length of temp_averages matches num_conditions
    if len(temp_averages) != num_conditions:
        raise ValueError("Length of temp_averages must equal num_conditions")

    # Define the standard deviation for the temperature fluctuations.
    std_deviation = 3.0

    # Initialize an empty list to store each condition's temperature data
    temperatures_all_conditions = []

    # Generate temperature measurements for each condition
    for avg_temp in temp_averages:
        temperatures = np.random.normal(loc=avg_temp, scale=std_deviation, size=num_measurements)
        temperatures_all_conditions.append(temperatures)

    return np.array(temperatures_all_conditions)


# Example usage:
temp_averages = [25, 20, 15]  # Average temperatures for three different conditions
num_measurements = 100  # Number of measurements per condition
num_conditions = 3  # Number of conditions

temperatures = generate_temperature_data_for_boxplot(temp_averages, num_measurements, num_conditions)
print(temperatures)
# You can now use this data to create box plots with matplotlib, seaborn, or any other plotting library.


def fig_sp_line():
    # Select other Plotly events by specifying kwargs
    df = px.data.stocks()
    c1, c2 = st.columns(2)

    with c1:
        fig = px.line(df, x='date', y="GOOG", markers=True)
        selected_points_fig = plotly_events(fig, select_event=True)

    with c2:
        try:
            selected_points_fig_x = list(map(lambda el: el['x'], selected_points_fig))
            selected_points_fig_y = list(map(lambda el: el['y'], selected_points_fig))
            fig2 = px.line(x=selected_points_fig_x, y=selected_points_fig_y)
            st.plotly_chart(fig2)
        except Exception:
            pass

    # Generate a grid of elevation data
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(x) * np.cos(y) + np.sin(np.sqrt(x**2 + y**2))

    # Create a Plotly figure for the contour plot
    fig = go.Figure(data=
    go.Contour(
        z=z,
        x=x[0],  # X coordinates
        y=y[:, 0],  # Y coordinates
        colorscale="Viridis")
    )

    fig.update_layout(title='Random Topographical Data', xaxis_title='X', yaxis_title='Y')
    st.plotly_chart(fig)

def temperature_plot():
    # Defining a mock temperature dataset suitable for creating a heat map of Hell with 9 circles
    # Assuming Hell's circles increase in temperature as we go deeper, except the last circle is frozen

    data = [
        [24, 26, 20, 25, 26, 19, 15, 24, 30, 21],
        [None, 50, 56, 75, 86, 69, 55, 74, 50, 0],
        [None, None, 156, 155, 146, 169, 135, 184, None, None],
        [None, None, 210, 200, 194, 195, 189, 220, None, None],
        [None, None, 245, 230, 240, 236, 201, None, None, None],
        [None, None, None, 340, 326, 316, 56, None, None, None],
        [None, None, None, 450, 465, 480, 456, None, None, None],
        [None, None, None, None, 520, 536, 590, None, None, None],
        [None, None, None, None, -225, -200, None, None, None, None],
    ]
    data_array = np.array(data)
    data_array = np.where(data_array == None, np.nan, data_array)
    print(data_array)
    # Interpolate missing values using linear interpolation
    # Note: We exclude the first and last row since they contain only one non-missing value
    for i in range(1, data_array.shape[0] - 1):
        mask = np.isnan(data_array[i])  # Mask for missing values
        x = np.arange(len(data_array[i]))  # x-coordinates
        y = data_array[i]  # Known values
        data_array[i][mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), y[~mask])  # Linear interpolation

    # Display the modified heatmap data
    print("Modified Heatmap Data with Interpolated Values:")
    print(data_array)
    fig = px.imshow(data_array)
    fig.update_layout(
        plot_bgcolor='black',
    )
    # fig.update_xaxes(
    #     # mirror=True,
    #     # ticks='outside',
    #     # showline=True,
    #     # linecolor='black',
    #     gridcolor='black'
    # )
    # fig.update_yaxes(
    #     # mirror=True,
    #     # ticks='outside',
    #     # showline=True,
    #     # linecolor='black',
    #     gridcolor='black'
    # )
    fig.show()
