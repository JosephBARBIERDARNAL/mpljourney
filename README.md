

<!-- Automatically generated, uses README.qmd to modify README.md -->

# `mpljourney`

A collection of cool datasets for Python.

Those datasets are primarly used for
[matplotlib-journey.com](https://www.matplotlib-journey.com/), an online
course to master data visualization with Python, but anyone can use
those datasets too.

> Note that `mpljourney` does not embed datasets directly with it, but
> fetches them from a [separate
> repo](https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey).

<br>

To load of one the available datasets:

``` python
from mpljourney import load_dataset

df = load_dataset("accident-london")
```

By default it loads it as a `pandas` dataframe, but it can also be any
of: "polars", "cudf", "pyarrow", "modin", assuming you have the
associated library installed on your machine:

``` python
from mpljourney import load_dataset

df = load_dataset("accident-london", output_format="polars")
```

<br>

Install with:

``` shell
pip install mpljourney
```

<br><br>

## All datasets

## accident-london

![](img/accident-london.png)

## CO2

![](img/CO2.png)

## earthquakes

![](img/earthquakes.png)

## economic

![](img/economic.png)

## footprint

![](img/footprint.png)

## game-sales

![](img/game-sales.png)

## london

'london' is a geo dataset. The `geometry` column is hidden here to make
the table snippet readable.

![](img/london.png)

## mariokart

![](img/mariokart.png)

## natural-disasters

![](img/natural-disasters.png)

## netflix

![](img/netflix.png)

## newyork-airbnb

![](img/newyork-airbnb.png)

## newyork

'newyork' is a geo dataset. The `geometry` column is hidden here to make
the table snippet readable.

![](img/newyork.png)

## storms

![](img/storms.png)

## ufo

![](img/ufo.png)

## us-counties

'us-counties' is a geo dataset. The `geometry` column is hidden here to
make the table snippet readable.

![](img/us-counties.png)

## walks

![](img/walks.png)

## wine

![](img/wine.png)

## world

'world' is a geo dataset. The `geometry` column is hidden here to make
the table snippet readable.

![](img/world.png)
