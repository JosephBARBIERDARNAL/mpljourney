from mpljourney import load_dataset, ALL_DATASETS
from great_tables import GT
import geopandas as gpd


def code_and_image(dataset_name: str, is_geodf: bool) -> None:
    if is_geodf:
        message = "The `geometry` column with the polygons is hidden."
    else:
        message = ""
    content = f"""

### {dataset_name}

{message}

```py
from mpljourney import load_dataset

df = load_dataset("{dataset_name}")
```

![](img/{dataset_name}.png)

    """
    return content


def top_of_file():
    content = """
<!-- Automatically generated, do not change by hand. Use make.py instead. -->

# `mpljourney`: datasets for [matplotlib-journey.com](https://www.matplotlib-journey.com/)

`mpljourney` is a small package with datasets used in the [Matplotlib Journey online course](https://www.matplotlib-journey.com/).

The datasets are either pandas or geopandas dataframes. Geopanda dataframes are mainly used to provide polygons for drawing maps.

<br><br>

## Installation

```bash
pip install mpljourney
```

<br><br>

## All datasets

"""
    return content


if __name__ == "__main__":
    readme_content = top_of_file()
    for dataset_name in ALL_DATASETS.keys():
        # create and save a GT table
        df = load_dataset(dataset_name).head(10)
        is_geodf = isinstance(df, gpd.GeoDataFrame)
        if is_geodf:
            df = df.drop(columns="geometry")
        table = GT(df)
        print(f"Saving: {dataset_name}")
        table.save(file=f"img/{dataset_name}.png", scale=2, web_driver="firefox")

        # get code snippet for the dataset
        code_snippet = code_and_image(dataset_name, is_geodf=is_geodf)
        readme_content += code_snippet

    # save to readme
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
