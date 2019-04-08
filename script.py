#https://plot.ly/python/bar-charts/
#https://plot.ly/python/subplots/

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import iplot, init_notebook_mode

import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)

plotly.tools.set_credentials_file(username='cdvu', api_key='d1Ip8twrCBnED72ibDBX')

data = pd.read_csv('antibiotics_data.csv')
posData = data.loc[data["Gram Staining "] == 'positive']
negData = data.loc[data["Gram Staining "] == 'negative']

bacteria = data["Bacteria "]

trace1 = go.Bar(
    x=bacteria,
    y=negData["Penicilin"],
    name='Negative Penicilin',
    text=negData["Penicilin"],
    textposition = 'auto',
    marker=dict(
        color='rgb(234, 177, 202)',
    )
)

    
trace2 = go.Bar(
    x=bacteria,
    y=negData["Streptomycin "],
    name='Negative Streptomycin',
    text=negData["Streptomycin "],
    textposition = 'auto',
    marker=dict(
        color='rgb(243, 208, 208)',
    )
)

    
trace3 = go.Bar(
    x=bacteria,
    y=negData["Neomycin"],
    text=negData["Neomycin"],
    name='Negative Neomycin',
    textposition = 'auto',
    marker=dict(
        color='rgb(234, 177, 177)',
    )
)


trace4 = go.Bar(
    x=bacteria,
    y=posData["Penicilin"],
    name='Positive Penicilin',
    text=posData["Penicilin"],
    textposition = 'auto',
    marker=dict(
        color='rgb(198, 201, 222)',
    )
)

    
trace5 = go.Bar(
    x=bacteria,
    y=posData["Streptomycin "],
    name='Positive Streptomycin',
    text=posData["Streptomycin "],
    textposition = 'auto',
    marker=dict(
        color='rgb(103, 131, 168)',
    )
)

    
trace6 = go.Bar(
    x=bacteria,
    y=posData["Neomycin"],
    text=posData["Neomycin"],
    name='Positive Neomycin',
    textposition = 'auto',
    marker=dict(
        color='rgb(198, 222, 222)',
    )
)



fig = tools.make_subplots(rows=1, cols=2, shared_yaxes=True)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace3, 1, 1)

fig.append_trace(trace4, 1, 2)
fig.append_trace(trace5, 1, 2)
fig.append_trace(trace6, 1, 2)
    
layout = go.Layout(
    title=go.layout.Title(
        text="Antibiotics Data"
    ),
    yaxis=dict(type='log', autorange=True)
)

fig['layout'].update(layout)

py.iplot(fig, filename='multiple-subplots-shared-yaxes')