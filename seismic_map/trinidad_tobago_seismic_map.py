"""
Trinidad and Tobago Seismic Event Visualization

This script reads seismic event data from an Excel file and creates
a map visualization showing earthquake locations, depths, and magnitudes
for the Trinidad and Tobago region.
"""

import numpy as np
import pandas as pd
import pygmt


def load_seismic_data(filepath):
    """
    Load seismic event data from an Excel file.

    Args:
        filepath (str): Path to the Excel file containing seismic data

    Returns:
        pd.DataFrame: DataFrame containing seismic event data
    """
    df = pd.read_excel(filepath)
    df.columns = df.columns.str.strip().str.lower()
    print(df)
    print(f"\nDataFrame columns: {df.columns.tolist()}")
    return df


def create_seismic_map(df, output_file=None):
    """
    Create a seismic event map for the Trinidad and Tobago region.

    Args:
        df (pd.DataFrame): DataFrame containing seismic event data with
            latitude, longitude, depth, and magnitude columns
        output_file (str, optional): Path to save the figure. If None,
            the figure is displayed only.
    """
    # Define the geographic region for Trinidad and Tobago
    region = [-63, -60, 9, 12]

    # Initialize the figure
    fig = pygmt.Figure()

    # Set up basemap with Mercator projection
    fig.basemap(region=region, projection="M15c", frame=True)

    # Add coastlines and water bodies
    fig.coast(land="black", water="skyblue")

    # Add location labels
    locations = [
        ("Scorborough", -60.71, 11.16, "white"),
        ("Port of Spain", -61.403, 10.648, "white"),
        ("Parque Nacional Delta del Orinoco", -61.37, 9.148, "white"),
        ("Guiria", -62.20, 10.63, "white"),
        ("TRINIDAD", -61.451, 10.317, "red"),
        ("TOBAGO", -60.809, 11.217, "red"),
        ("Gulf of Paria", -62.14, 10.28, "black"),
        ("Temblador", -62.72, 9.05, "white"),
    ]

    for name, lon, lat, color in locations:
        fig.text(
            x=lon,
            y=lat,
            text=name,
            font=f"12p,Helvetica-Bold,{color}",
        )

    # Create color palette for depth visualization
    pygmt.makecpt(
        cmap="viridis",
        series=[df["depth"].min(), df["depth"].max()],
    )

    # Plot seismic events
    # Size scaled by magnitude, color by depth
    fig.plot(
        x=df["longitude"],
        y=df["latitude"],
        size=0.01 * 2 ** df["magnitude"],
        color=df["depth"],
        cmap=True,
        style="cc",
        pen="black",
    )

    # Add colorbar to show depth scale
    fig.colorbar(frame='af+l"Depth (km)"')

    # Display or save the figure
    if output_file:
        fig.savefig(output_file)
        print(f"Figure saved to {output_file}")
    else:
        fig.show()


def main():
    """
    Execute the seismic data visualization.
    """
    data_file = "Trinidad_tobago_Event.xlsx"

    df = load_seismic_data(data_file)
    create_seismic_map(df)


if __name__ == "__main__":
    main()
