import mpljourney
from mpljourney import load_dataset, ALL_DATASETS
import pandas as pd
import geopandas as gpd
import pytest


@pytest.mark.parametrize("dataset_name", ALL_DATASETS)
def test_load_dataset(dataset_name):
    df = load_dataset(dataset_name)
    assert isinstance(df, (pd.DataFrame, gpd.GeoDataFrame))
    assert len(df) >= 5


def test_version():
    assert mpljourney.__version__ == "0.1.0"
