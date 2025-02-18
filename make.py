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
df.head(10)
```

![](img/{dataset_name}.png)

    """
    return content


def top_of_file():
    content = """
<!-- Automatically generated, do not change by hand. Use make.py instead. -->

# `mpljourney`: datasets for [matplotlib-journey.com](https://www.matplotlib-journey.com/)

`mpljourney` is a small package with datasets used in the [Matplotlib Journey online course](https://www.matplotlib-journey.com/).

The datasets are either pandas or geopandas dataframes. Geopandas dataframes are mainly used to provide polygons for drawing maps.

<br><br>

## Installation

```bash
pip install git+https://github.com/JosephBARBIERDARNAL/mpljourney.git
```

<br><br>

## All datasets

"""
    return content


if __name__ == "__main__":
    resave_images = False
    readme_content = top_of_file()
    for dataset_name in ALL_DATASETS.keys():
        print(f"Saving: {dataset_name}")

        # create and save a GT table
        df = load_dataset(dataset_name).head(10)
        is_geodf = isinstance(df, gpd.GeoDataFrame)
        if is_geodf:
            df = df.drop(columns="geometry")
        if resave_images:
            table = GT(df)
            table.save(file=f"img/{dataset_name}.png", scale=2, web_driver="firefox")

        # get code snippet for the dataset
        code_snippet = code_and_image(dataset_name, is_geodf=is_geodf)
        readme_content += code_snippet

    # save to readme
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
