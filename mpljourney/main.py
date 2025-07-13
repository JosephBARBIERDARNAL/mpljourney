import narwhals as nw
from narwhals.typing import Frame

from typing import Literal

import warnings

warnings.filterwarnings(
    "ignore",
    message=".*The 'shapely.geos' module is deprecated.*",
    category=DeprecationWarning,
)


ALL_DATASETS: list[str] = [
    "accident-london",
    "CO2",
    "earthquakes",
    "economic",
    "footprint",
    "game-sales",
    "london",
    "mariokart",
    "natural-disasters",
    "netflix",
    "newyork-airbnb",
    "newyork",
    "storms",
    "ufo",
    "us-counties",
    "walks",
    "wine",
    "world",
]

_GEOJSON_DATASETS: list[str] = ["london", "newyork", "us-counties", "world"]


def _find_file_url(dataset_name: str) -> str:
    """Constructs the raw GitHub URL for a given dataset."""
    if dataset_name not in ALL_DATASETS:
        raise ValueError(
            f"Invalid dataset: {dataset_name}. It must be one of:\n"
            f"{', '.join(ALL_DATASETS)}"
        )

    base_url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/main"
    extension: Literal[".geojson", ".csv"] = (
        ".geojson" if dataset_name in _GEOJSON_DATASETS else ".csv"
    )
    file_path: str = f"{dataset_name}/{dataset_name}{extension}"

    return f"{base_url}/{file_path}"


def load_dataset(dataset_name: str, output_format: str = "pandas"):
    """
    Load one of the available datasets from the online repository.

    Args:
        dataset_name: Name of the dataset. It must be one of "accident-london",
            "CO2", "earthquakes", "economic", "footprint", "game-sales", "london",
            "mariokart", "natural-disasters", "netflix", "newyork-airbnb", "newyork",
            "storms", "ufo", "us-counties", "walks", "wine", "world".
        output_format: Output for the dataframe. It must be one of "pandas"
            (default), "polars", "cudf", "pyarrow", "modin".
    """
    dataset_url: str = _find_file_url(dataset_name)

    if dataset_url.endswith(".geojson"):
        try:
            import geopandas as gpd

            df: gpd.GeoDataFrame = gpd.read_file(dataset_url)
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "You must have `geopandas` installed to use geo datasets. "
                "Install with `pip install geopandas`."
            )
    elif dataset_url.endswith(".csv"):
        df: Frame = nw.read_csv(dataset_url, backend=output_format).to_native()
    else:
        raise ValueError("Unsupported file type.")

    return df
