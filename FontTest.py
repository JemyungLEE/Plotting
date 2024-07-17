import plotly.graph_objs as go

data = [
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    )
]
layout = go.Layout(width=500, height=300,
    title='Font Test',
    font=dict(family='/Library/Fonts/SF Pro Display', size=18),
)
fig = go.FigureWidget(data=data, layout=layout)
fig.show()