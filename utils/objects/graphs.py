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


@st.cache_data
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
        )
    )

    return fig


@st.cache_data
def get_fig_spectral_analysis(circle_selection=['All']):
    df = pd.read_csv("data/outputs/data_spectra_cicles_box_reloaded.tsv.csv", sep='\t')

    if circle_selection != ['All']:
        df_filtered = df.loc[df['Circle of Hell'].isin(circle_selection),:]
    else:
        df_filtered = df
    fig = px.line(df_filtered, x='Wavelength', y='Intensity', color='Circle of Hell')

    # Update graph layout
    fig.update_layout(
        title="Spectral Signatures Across the <br>Nine Circles of Hell",
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


def get_fig_heatmap(heatmap_data):
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
    domains = ["1", "2", "3", "4", "5",
               "6", "7", "8", "9"]

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
        title='Heatmap of Infernal populations',
        xaxis_title="Circles of Hell",
        yaxis_title="Creatures of the damned",
    )
    return heatmap

@st.cache_data
def get_fig_barplot_e_sources(mode):
    y_column = 'energy_emissions' if mode == 'Units (Infernals)' else 'share_percent'

    df = pd.read_csv('data/outputs/data_barplot_e_sources.csv')
    fig = px.bar(df,
                 x='circle', y=y_column, color='energy_source',
                 labels={"energy_source": "Energy source"}
                 )

    fig.update_layout(
        title=dict(text="Hell's energy outputs <br>in Infernals (666 heat units)",
                   pad=dict(t=50, b=50, l=50, r=50)),
        xaxis_title="Circle of Hell",
        yaxis_title="Engergy emmisions, Infernals",
    )

    return fig
