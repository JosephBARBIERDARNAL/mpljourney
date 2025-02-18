import pandas as pd
import geopandas as gpd
from typing import Union
import os

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

ALL_DATASETS = {
    "accident-london": "accident-london.csv",
    "CO2": "CO2.csv",
    "earthquakes": "earthquakes.csv",
    "economic": "economic.csv",
    "footprint": "footprint.csv",
    "game-sales": "game-sales.csv",
    "london": "london.geojson",
    "mariokart": "mariokart.csv",
    "natural-disasters": "natural-disasters.csv",
    "netflix": "netflix.csv",
    "newyork-airbnb": "newyork-airbnb.csv",
    "newyork": "newyork.geojson",
    "storms": "storms.csv",
    "ufo": "ufo.csv",
    "us-counties": "us-counties.geojson",
    "walks": "walks.csv",
    "wine": "wine.csv",
    "world": "world.geojson",
}


def load_dataset(dataset_name: str) -> Union[pd.DataFrame, gpd.GeoDataFrame]:
    dataset_file = ALL_DATASETS[dataset_name]
    dataset_path = os.path.join(PACKAGE_DIR, "datasets", dataset_file)
    if not os.path.isfile(dataset_path):
        raise ValueError(f"No dataset found at: {dataset_path}")
    if dataset_path.endswith(".geojson"):
        df = gpd.read_file(dataset_path)
    elif dataset_path.endswith(".csv"):
        df = pd.read_csv(dataset_path)
    else:
        raise ValueError(f"Unexpected file extension: {dataset_path}")
    return df


if __name__ == "__main__":
    print(load_dataset("economic"))
