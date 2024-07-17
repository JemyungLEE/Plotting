from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing = 0.03)

yvallm = [0.195271655625106,0.0376811910885905,0.0845009348467051,0.00862290981022781,0.0008753035152995,0.0061778300357778,0.0129345952880827,0.012444905891059,0.00262391538716966,0.0256773129526246,0.00748455643827778,0.0134476070302796,0.407742717909]
bvallm = []
for i in range(0,12):
    bvallm.append(sum(yvallm[:i]))
bvallm.append(0)
labelslm=["Low-expenditure hhs.\n(bottom 20%)",'Food','Electricity','Gas','Other energy','Medical care','Public transport','Private transport','Education','Consumable goods','Durable goods','Other services',"Middle-expenditure hhs.(middle 20%)"]

yvalmh = [0.4077427179092,0.096317745427555,0.34501726564858,0.0258923075296434,-0.0046059011001416,0.0390433159804647,0.0623765112142019,0.0825983795579077,0.0164634097566139,0.0731715526021632,0.0978402499440251,0.0849015576958329,1.326759112]
bvalmh = []
for i in range(0,12):
    bvalmh.append(sum(yvalmh[:i]))
bvalmh.append(0)

labelsmh=["Middle-expenditure hhs.(middle 20%)",'Food','Electricity','Gas','Other energy','Medical care','Public transport','Private transport','Education','Consumable goods','Durable goods','Other services',"High-expenditure hhs.(top 20%)"]


fig.add_trace(
    go.Bar(
        orientation = "v",
        y = yvallm, base = bvallm,
        #text = ['','Food','Electricity','Gas','Other energy','Medical care','Public transport','Private transport','Education','Consumable goods','Durable goods','Other services',''],
        # text=labelslm,
        # textposition='outside',
        # textangle=-90,
        marker={'color':["#9edae5","#17becf","#dbdb8d","#bcbd22","#c7c7c7","#7f7f7f","#f7b6d2","#e377c2","#c49c94","#8c564b","#c5b0d5","#9467bd","#ff9896"]},
        marker_line_color='grey',


    ),
    row=1, col=1
)
fig.add_trace(
    go.Bar(
        orientation = "v",
        y = yvalmh, base = bvalmh,
        # text=labelsmh,
        # textposition='outside',
        # textangle=270,
        marker={'color':["#9edae5","#17becf","#dbdb8d","#bcbd22","#c7c7c7","#7f7f7f","#f7b6d2","#e377c2","#c49c94","#8c564b","#c5b0d5","#9467bd","#ff9896"]},
        marker_line_color='grey',
    ),
    row=1, col=2
)

fig.update_layout(
    showlegend=False,
    bargap=0.0,
    font=dict(
        family="Arial",
        size=16,
        color='black'
    ),
    width=2000, height=1000,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    uniformtext_minsize=16,
    uniformtext_mode='show',

    annotations=[
        dict(
            x=-0.042,
            y=0.75,
            showarrow=False,
            text="Household consumption CF per capita (tCO₂/yr/capita)",
            textangle=-90,
            xref="paper",
            yref="y"
        )
    ]+[
        dict(
            x=xpos,
            y=ypos,
            xref='x1',
            yref='y1',
            align='right',
            textangle=270,
            text=labelslm[xpos],
            showarrow=False,
        ) for xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                [0.44, 0.15, 0.155, 0.28, 0.23,
                                 0.234, 0.218, 0.225, 0.28, 0.22,
                                 0.275, 0.29,0.66])
    ]+[
        dict(
            x=xpos,
            y=ypos,
            xref='x2',
            yref='y2',
            align='left',
            textangle=270,
            text=labelsmh[xpos],
            showarrow=False,
        ) for xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                [0.66, 0.36, 0.43, 0.81, 0.775,
                                 0.775, 0.795, 0.85, 0.978, 0.935,
                                 1.035, 1.135, 1.1])
    ],
)

fig.update_xaxes(ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True, showticklabels=False)
fig.update_yaxes(range=[0,1.5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True,tickvals=[0.3,0.6,0.9,1.2,1.5])
#fig.update_xaxes(title="Consumption categories", ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True, showticklabels=False)
#fig.update_yaxes(title="Household consumption CF per capita (tCO₂/yr/capita)",range=[0,1.5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=True,tickvals=[0.3,0.6,0.9,1.2,1.5])

fig.show()
#fig.write_image("/Users/leejmacbook/Desktop/test.png")