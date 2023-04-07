# Library Importation
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Creating the donut 
def donut(data, title, hole=0.5, legend=True):
    """
    Create a donut chart in python for easy glance of the proportionality of the data features. 
    Warning: Do not use if the targeted columns has more than three categories in your data

    Args:
    data (panda Series): The data should be in a pandas series format.
    title (str): This is the title of the dount chart
    
    Kwargs:
    hole (float): The size of the hole in the middle of the donut chart.Ranges from 0 to 1. Default is 0.5
    

    Returns:
    Diagram: A well designed and accepted donut even accepted by Pie chart Haters! :)
    """
    # convert the data to a dict and then a list 
    df = data.value_counts().to_dict()
    new_df =  df.items()
    
    # Extracting the labels and Values
    labels = [i[0] for i in new_df]
    values = [i[1] for i in new_df ]
    
    # Creating a donut chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=hole, showlegend=legend, sort=True,
                            hoverinfo='label+percent+value', direction='clockwise', textinfo='label+percent')])
    fig.update_layout(title={'text': title,'x': 0.49,'y': 0.9,'xanchor': 'center', 'yanchor': 'top'},
                legend={'x':1.05, 'y':0.6, 'xanchor':'right','yanchor':'top'})
    fig.show()