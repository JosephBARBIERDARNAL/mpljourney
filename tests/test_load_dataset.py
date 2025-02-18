from mpljourney import load_dataset, ALL_DATASETS
import pandas as pd
import geopandas as gpd


def test_load_all_datasets():
    for dataset_name in ALL_DATASETS.keys():
        df = load_dataset(dataset_name)
        assert isinstance(df, (pd.DataFrame, gpd.GeoDataFrame))
