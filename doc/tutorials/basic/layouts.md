# Layout Content

In this guide, we will learn how to layout, i.e., arrange, Python objects, including Panel components:

- *Layouts* are available in the `pn` namespace.
- Arrange Python objects, including Panel components, using [`pn.Column`](../../reference/layouts/Column.ipynb) and [`pn.Row`](../../reference/layouts/Row.ipynb).
- Layouts like [`Column`](../../reference/layouts/Column.ipynb) and [`Row`](../../reference/layouts/Row.ipynb) behave like lists.
- A *layout* will automatically use `pn.panel` to determine how to best display non-Panel objects.
- Create complex arrangements by combining and nesting *layouts*.
- Explore all available *layouts* and their *reference guides* in the [Layouts Section](../../reference/index.md#layouts) of the [Component Gallery](../../reference/index.md).

In this tutorial, we will **not learn** how to:

- Use specific *layouts* in detail. Details are covered in the *[reference guides](../../reference/index.md#layouts)*.
- Style *layouts*. This topic is covered in another tutorial.

:::{note}
When we ask to *run the code* in the sections below, we may execute the code directly in the Panel documentation by using the green *run* button, in a notebook cell, or in a file named `app.py` served with `panel serve app.py --autoreload`.
:::

## Install the Dependencies

Please ensure that [hvPlot](https://hvplot.holoviz.org) and [Pandas](https://pandas.pydata.org) are installed.

::::{tab-set}

:::{tab-item} conda
:sync: conda

``` bash
conda install -y -c conda-forge hvplot pandas
```

:::

:::{tab-item} pip
:sync: pip

``` bash
pip install hvplot pandas
```

:::

::::

## Layout in a Column

Run the following code:

```{pyodide}
import pandas as pd
import panel as pn

pn.extension(design="bootstrap")

button = pn.widgets.Button(name="Refresh", icon="refresh", button_type="primary")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)

pn.Column("# Orders", data, button).servable()
```

:::{note}
To understand in detail how a layout like `Column` works, please refer to its *reference guide*.
:::

Click [this link](../../reference/layouts/Column.ipynb) to access the `Column` Reference Guide, and take a few minutes to familiarize yourself with its organization and content.

It should look like

[![Column reference guide](../../_static/images/layout_column_reference.png)](../../reference/layouts/Column.ipynb)

## Layout in a Row

Run the following code:

```{pyodide}
import pandas as pd
import panel as pn
import hvplot.pandas

pn.extension(design="bootstrap")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)
plot = data.hvplot(x="Day", y="Orders", kind="bar", color="goldenrod", title="Orders")

pn.Row(plot, data).servable()
```

Click [this link](../../reference/index.md#layouts) to access the Layouts section of the [Component Gallery](../../reference/index.md).

Open the [`Row`](../../reference/layouts/Row.ipynb) reference guide and take a few minutes to familiarize yourself with its organization and content.

It should look like

[![Layout Section and Row reference guide](../../_static/images/layout_section_row_guide.png)](../../reference/layouts/Row.ipynb)

## Works like a list

:::{note}
`Column`, `Row`, and many other layouts are *list-like*.
:::

Run the code below:

```{pyodide}
import pandas as pd
import panel as pn

pn.extension(design="bootstrap")

button = pn.widgets.Button(name="Refresh", icon="refresh", button_type="primary")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)

component = pn.Column("# Orders", data, button)
pn.Column(component[0], component[2], component[1]).servable()
```

:::{note}
We are utilizing the *list-like* properties of the `Column` layout to rearrange its elements. More specifically, we are using *list-indexing* as in `component[2]`. The `Column` layout implements all the methods you would expect from a *list-like* object, including `.append` and `.remove`.
:::

## Displays using `pn.panel`

Run the code below:

```{pyodide}
import pandas as pd
import panel as pn

pn.extension(design="bootstrap")

button = pn.widgets.Button(name="Refresh", icon="refresh", button_type="primary")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)

component = pn.Column("# Orders", data, button)
print(component)
component.servable()
```

:::{note}
The `print` statement will output something like:

```bash
Column(design=<class 'panel.theme.bootst...)
    [0] Markdown(str, design=<class 'panel.theme.bootst...)
    [1] DataFrame(DataFrame, design=<class 'panel.theme.bootst...)
    [2] Button(button_type='primary', design=<class 'panel.theme.bootst..., icon='refresh', name='Refresh')
```

Under the hood, the `Column` layout has used `pn.panel` to convert the string to a [`Markdown`](../../reference/panes/Markdown.ipynb) pane and the DataFrame to a [`DataFrame`](../../reference/panes/DataFrame.ipynb) pane.

You can customize how the objects are displayed using `pn.panel` or specific *Panes*.
::::

Run the code below:

```{pyodide}
import pandas as pd
import panel as pn

pn.extension(design="bootstrap")

button = pn.widgets.Button(name="Refresh", icon="refresh", button_type="primary")

data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)

pn.Column(
    pn.pane.Str("# Orders"), pn.panel(data, sizing_mode="stretch_width"), button
).servable()
```

## Combine Layouts

:::{note}
To create more complex arrangements of objects, we can combine and nest *layouts*.
:::

Let's run the code below:

```{pyodide}
import pandas as pd
import panel as pn
import hvplot.pandas

pn.extension(design="bootstrap")

button = pn.widgets.Button(name="Refresh", icon="refresh", button_type="primary")
data = pd.DataFrame(
    [
        ("Monday", 7),
        ("Tuesday", 4),
        ("Wednesday", 9),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 4),
        ("Sunday", 4),
    ],
    columns=["Day", "Orders"],
)
plot = data.hvplot(x="Day", y="Orders", kind="bar", color="goldenrod", title="Orders")

pn.Column("# Orders", button, pn.Row(plot, pn.panel(data, width=400))).servable()
```

## Recap

In this guide, we have learned:

- *Layouts* are available in the `pn` namespace.
- Arrange Python objects, including Panel components, using [`pn.Column`](../../reference/layouts/Column.ipynb) and [`pn.Row`](../../reference/layouts/Row.ipynb).
- Layouts like [`Column`](../../reference/layouts/Column.ipynb) and [`Row`](../../reference/layouts/Row.ipynb) behave like lists.
- A *layout* will automatically use `pn.panel` to determine how to best display Python objects.
- Create complex arrangements by combining and nesting *layouts*.
- Explore all available *layouts* and their *reference guides* in the [Layouts Section](../../reference/index.md#layouts) of the [Component Gallery](../../reference/index.md).

## References

### Tutorials

- [Display objects with `pn.panel`](pn_panel.md)
- [Display objects with Panes](panes.md)

### How-to

- [Align Components](../../how_to/layout/align.md)
- [Control Size](../../how_to/layout/size.md)
- [Customize Spacing](../../how_to/layout/spacing.md)
- [Migrate from Streamlit | Layout Objects](../../how_to/streamlit_migration/layouts.md)

### Explanation

- [Components Overview](../../explanation/components/components_overview.md)

### Component Gallery

- [Layouts](../../reference/index.md#layouts)