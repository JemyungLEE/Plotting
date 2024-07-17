import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    name = "20", orientation = "v",
    x = ["Sales", " ", "  ", "Profit before tax"],
    y = [10,2,3,4],
    base=[0,10,12,15],
    text = ["","Bb","Cc",""],
    textposition='outside',
    textangle=270,
    marker={'color':["#17becf", "#bcbd22", "#7f7f7f", "#e377c2"]},
    marker_line_color='grey'
))

fig.update_layout(
        showlegend = False,
        bargap=0.0,
        font=dict(
            family="Arial",
            size=18,
            color='black'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        annotations=[
            dict(
                x=xpos,
                y=ypos,
                xref='x',
                yref='y',
                text="Aaweefsfdsfs ",
                textangle=270,
                align="right",
                showarrow=False,
            ) for xpos, ypos in zip([1,2], [8.5,10.5])
        ],
)

fig.update_xaxes(title="Xaxis", ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(title="Yaxis",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True)

fig.show()