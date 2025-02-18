
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



### accident-london



```py
from mpljourney import load_dataset

df = load_dataset("accident-london")
df.head(10)
```

![](img/accident-london.png)

    

### CO2



```py
from mpljourney import load_dataset

df = load_dataset("CO2")
df.head(10)
```

![](img/CO2.png)

    

### earthquakes



```py
from mpljourney import load_dataset

df = load_dataset("earthquakes")
df.head(10)
```

![](img/earthquakes.png)

    

### economic



```py
from mpljourney import load_dataset

df = load_dataset("economic")
df.head(10)
```

![](img/economic.png)

    

### footprint



```py
from mpljourney import load_dataset

df = load_dataset("footprint")
df.head(10)
```

![](img/footprint.png)

    

### game-sales



```py
from mpljourney import load_dataset

df = load_dataset("game-sales")
df.head(10)
```

![](img/game-sales.png)

    

### london

The `geometry` column with the polygons is hidden.

```py
from mpljourney import load_dataset

df = load_dataset("london")
df.head(10)
```

![](img/london.png)

    

### mariokart



```py
from mpljourney import load_dataset

df = load_dataset("mariokart")
df.head(10)
```

![](img/mariokart.png)

    

### natural-disasters



```py
from mpljourney import load_dataset

df = load_dataset("natural-disasters")
df.head(10)
```

![](img/natural-disasters.png)

    

### netflix



```py
from mpljourney import load_dataset

df = load_dataset("netflix")
df.head(10)
```

![](img/netflix.png)

    

### newyork-airbnb



```py
from mpljourney import load_dataset

df = load_dataset("newyork-airbnb")
df.head(10)
```

![](img/newyork-airbnb.png)

    

### newyork

The `geometry` column with the polygons is hidden.

```py
from mpljourney import load_dataset

df = load_dataset("newyork")
df.head(10)
```

![](img/newyork.png)

    

### storms



```py
from mpljourney import load_dataset

df = load_dataset("storms")
df.head(10)
```

![](img/storms.png)

    

### ufo



```py
from mpljourney import load_dataset

df = load_dataset("ufo")
df.head(10)
```

![](img/ufo.png)

    

### us-counties

The `geometry` column with the polygons is hidden.

```py
from mpljourney import load_dataset

df = load_dataset("us-counties")
df.head(10)
```

![](img/us-counties.png)

    

### walks



```py
from mpljourney import load_dataset

df = load_dataset("walks")
df.head(10)
```

![](img/walks.png)

    

### wine



```py
from mpljourney import load_dataset

df = load_dataset("wine")
df.head(10)
```

![](img/wine.png)

    

### world

The `geometry` column with the polygons is hidden.

```py
from mpljourney import load_dataset

df = load_dataset("world")
df.head(10)
```

![](img/world.png)

    