import os
import pickle

import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from streamlit_plotly_events import plotly_events
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
# import scipy.cluster.hierarchy as sch
import plotly.figure_factory as ff
import plotly.graph_objects as go
from data import get_data


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

    # """# Example usage:
    # temp_averages = [25, 20, 15]  # Average temperatures for three different conditions
    # num_measurements = 100  # Number of measurements per condition
    # num_conditions = 3  # Number of conditions
    #
    # temperatures = generate_temperature_data_for_boxplot(temp_averages, num_measurements, num_conditions)
    #
    #
    # # print(temperatures)
    #
    # # You can now use this data to create box plots with matplotlib, seaborn, or any other plotting library.
    # """
    return np.array(temperatures_all_conditions)


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
    z = np.sin(x) * np.cos(y) + np.sin(np.sqrt(x ** 2 + y ** 2))

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

    fig.show()


def fig_box_temp_circles(circle_selection=['All']):
    df = pd.read_csv('data/outputs/data_temp_cicles_box.tsv', sep='\t',
                     keep_default_na=False)
    if circle_selection != ['All']:
        df_filtered = df.loc[df['Circle'].isin(circle_selection), :]
    else:
        df_filtered = df

    fig = go.Figure()
    for i, row in df_filtered.iterrows():
        # Skipping the 8th circle since it has no data
        if pd.isna(row['Temperature']):
            continue

        fig.add_trace(go.Box(
            y=[row['lowerfence'], row['1st Quartile'], row['Temperature'], row['3rd Quartile'], row['upperfence']],
            name=row['Circle'],
            boxpoints=False,  # No outliers
            marker_color='rgba(139, 0, 0, 0.8)',  # Dark red with transparency
            line=dict(color='#DAA520'),  # Golden border
        ))

    fig.update_layout(
        title="Thermal Landscape Across the Circles of Hell",
        xaxis_title="Circles of Hell",
        yaxis_title="Temperature (°C)",
    )

    fig.update_layout(
        plot_bgcolor='rgba(111, 0, 0, 0.9)',
        paper_bgcolor='rgba(111, 0, 0, 0.9)',
        font=dict(
            color='rgba(255, 255, 255, 0.9)',
            family="Arial, sans-serif",
            size=12,
        ),
        xaxis=dict(
            color='rgba(255, 255, 255, 0.9)',
            gridcolor='rgba(218, 165, 32, 0.5)'
        ),
        yaxis=dict(
            color='rgba(255, 255, 255, 0.9)',
            gridcolor='rgba(218, 165, 32, 0.5)'
        ),

    )

    return fig


def get_fig_spectral_analysis(circle_selection=['All']):
    df = pd.read_csv("data/outputs/data_spectra_cicles_box.tsv", sep='\t')

    if circle_selection != ['All']:
        df_filtered = df.loc[:, [x for x in df.columns if x in circle_selection + ['Wavelength']]]
    else:
        df_filtered = df
    fig = go.Figure()

    # Add traces for each circle based on DataFrame columns
    for circle in df_filtered.columns[1:]:  # Skip the 'Wavelength' column
        fig.add_trace(go.Scatter(x=df_filtered['Wavelength'], y=df_filtered[circle], mode='lines', name=circle))

    # Update graph layout
    fig.update_layout(
        title="Spectral Signatures Across the Nine Circles of Hell",
        xaxis_title="Wavelength (nm)",
        yaxis_title="Intensity",
        plot_bgcolor='rgba(10, 10, 10, 1)',  # Dark background for contrast
        paper_bgcolor='rgba(10, 10, 10, 1)',
        font=dict(color="white"),
        legend_title_text='Circle'
    )

    fig.update_layout(
        plot_bgcolor='rgba(111, 0, 0, 0.9)',
        paper_bgcolor='rgba(111, 0, 0, 0.9)',
        font=dict(
            color='rgba(255, 255, 255, 0.9)'
        ),
        xaxis=dict(
            color='rgba(255, 255, 255, 0.9)',
            gridcolor='rgba(218, 165, 32, 0.5)'
        ),
        yaxis=dict(
            color='rgba(255, 255, 255, 0.9)',
            gridcolor='rgba(218, 165, 32, 0.5)'
        )
    )
    return fig


def get_fig_heatmap():
    # Names of creatures
    creatures = [
        "Abarimon", "Sibitti", "Strigae",  # First Circle: Limbo
        "Asmoday", "Xaphania", "Vetala",  # Second Circle: Lust
        "Aldinach", "Gorgonops", "Fafnir",  # Third Circle: Gluttony
        "Mammonas", "Plouton", "Kubera",  # Fourth Circle: Greed
        "Lyssa", "Furcas", "Alecto",  # Fifth Circle: Anger
        "Belial", "Naberius", "Sammael",  # Sixth Circle: Heresy
        "Areskagal", "Tartaruchi", "Draug",  # Seventh Circle: Violence
        "Pazuzu", "Surgat", "Janus",  # Eighth Circle: Fraud
        "Cocytus", "Judas", "Brutus",  # Ninth Circle: Treachery
        "Antaeus", "Tisiphone", "Belphegor"  # Additional Creatures
    ]

    # Domains and corresponding average temperatures
    domains = ["1st Circle", "2nd Circle", "3rd Circle", "4th Circle", "5th Circle",
               "6th Circle", "7th Circle", "8th Circle", "9th Circle"]

    with open("data/outputs/data_heatmap_creature_counts.pickle", 'rb') as f:
        heatmap_data = pickle.load(f)

    heatmap = go.Heatmap(
        z=heatmap_data,
        x=domains,
        y=creatures,
        colorscale='RdBu',
        colorbar=dict(title='Population'),
        showscale=True
    )

    heatmap = go.Figure(data=heatmap)

    # Update layout to accommodate the heatmap
    heatmap.update_layout(
        title='Heatmap for Creatures of Hell',
        xaxis_title="Circles of Hell",
        yaxis_title="Creatures of the damned",
    )
    return heatmap
