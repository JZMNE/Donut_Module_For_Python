<h1 align="center" style="color:MediumSeaGreen;"> <b> DONUT CHART FOR PYTHON  </b></h1>

This module provides a simple function to create a well-designed donut chart in Python. The function uses Plotly under the hood to create a chart that provides a quick and easy way to view the proportionality of data features.

# Overview
A donut chart is a type of chart that displays data as a ring-shaped chart with a hole in the middle, similar to a pie chart. Some people find donut charts more visually appealing than pie charts,(as it is called the ["Forbidden Chart"](https://www.entrepreneur.com/growing-a-business/people-please-stop-using-pie-charts/239932) ) as they can provide a clearer view of the data being displayed. However, it's important to use donut charts carefully and avoid using too many segments, as this can make the chart difficult to read and interpret.

> As someone who loves donut charts, it's crucial to create a well-organized, visually appealing donut chart that presents the data in an easily understandable way. For instance, if you want to quickly grasp the proportion of different categories within a feature, you can simply use the module. 

# Usage :doughnut:
To use the module, simply import the donut() function and provide the necessary arguments:

``` python
import pandas as pd
from donutchart import donut

# Create a sample dataset
data = pd.Series(['Dog', 'Dog', 'Cat', 'Bunny','Bunny','Bunny', 'Cat', 'Dog', 'Dog', 'Dog', 'Dog', 'Bunny', 'Dog', 'Dog'])
title = 'Distribution of Dog, Cat and Bunny'

# Create the donut chart
donut(data=data, title=title, legend = False)

```
The `donut()` function takes the following arguments:

- `data`: The data to be charted. This should be in a pandas Series format.
- `title`: The title of the chart.
- `hole`: The size of the hole in the middle of the chart. This ranges from 0 to 1 and defaults to 0.5.
- `legend`: Whether to include a legend. Defaults to True.

:warning: Note that the donut() function is not suitable for use with data that has more than three categories.

# Visualization
![SampleViz]()

# License 
This module is licensed under the MIT License. Click the [LICENSE](https://opensource.org/licenses/MIT) for more details.

&copy; 2023 Jazmine N

