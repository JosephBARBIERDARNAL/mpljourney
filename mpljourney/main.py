import narwhals as nw

from narwhals.typing import Frame
import os

PACKAGE_DIR: str = os.path.dirname(os.path.abspath(__file__))

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


def _find_file_path(dataset_name: str) -> str:
    if dataset_name not in ALL_DATASETS:
        raise ValueError(
            f"Invalid dataset: {dataset_name}. It must be one of:\n"
            f"{', '.join(ALL_DATASETS)}"
        )

    path_with_datasets: str = os.path.join(PACKAGE_DIR, "datasets")
    csv_path: str = os.path.join(path_with_datasets, f"{dataset_name}.csv")
    geojson_path: str = os.path.join(path_with_datasets, f"{dataset_name}.geojson")

    is_csv: bool = os.path.isfile(csv_path)
    is_geojson: bool = os.path.isfile(geojson_path)

    if is_csv:
        return csv_path
    elif is_geojson:
        return geojson_path
    else:
        raise ValueError("Dataset not found.")


def load_dataset(dataset_name: str, output_format: str = "pandas"):
    """
    Load of the available datasets in mpljourney.

    Args:
        dataset_name: Name of the dataset. It must be one of "accident-london",
            "CO2", "earthquakes", "economic", "footprint", "game-sales", "london",
            "mariokart", "natural-disasters", "netflix", "newyork-airbnb", "newyork",
            "storms", "ufo", "us-counties", "walks", "wine", "world".
        output_format: Output for the dataframe output. It must be one of "pandas"
            (default), "polars", "cudf", "pyarrow", "modin".
    """
    dataset_path: str = _find_file_path(dataset_name)

    if dataset_path.endswith(".geojson"):
        try:
            import geopandas as gpd

            df = gpd.read_file(dataset_path)
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "You must have `geopandas` installed to use geo datasets. "
                "Install with `pip install geopandas`."
            )
    elif dataset_path.endswith(".csv"):
        df: Frame = nw.read_csv(dataset_path, backend=output_format).to_native()

    return df
