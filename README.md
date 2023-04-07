<h1 align="center" style="color:MediumSeaGreen;"> <b> DONUT CHART FOR PYTHON  </b></h1>

This module provides a simple function to create a well-designed donut chart in Python. The function uses Plotly under the hood to create a chart that provides a quick and easy way to view the proportionality of data features.

# Usage :doughnut:
To use the module, simply import the donut() function and provide the necessary arguments:

``` python
import pandas as pd
from donutchart import donut


# Create a sample dataset
data = pd.Series([30, 50, 20])
title = "Example Donut Chart"

# Create the donut chart
donut(data=data, title=title)

```
The `donut()` function takes the following arguments:

- `data`: The data to be charted. This should be in a pandas Series format.
- `title`: The title of the chart.
- `hole`: The size of the hole in the middle of the chart. This ranges from 0 to 1 and defaults to 0.5.
- `legend`: Whether to include a legend. Defaults to True.

:warning: Note that the donut() function is not suitable for use with data that has more than three categories.

# License 
This module is licensed under the MIT License. See the LICENSE file for details.
