import plotly.graph_objects as go
import numpy as np

ngroup = 5
ncategory = 4
xvals = ["Bottom 20%<br>(<&#36;1.92)", "Bottom 20–40%<br>(&#36;1.92–&#36;2.55)", "Middle 20%<br>(&#36;2.55–&#36;3.37)", "Top 20–40%<br>(&#36;3.37–&#36;4.93)", "Top 20%<br>(>&#36;4.93)"]
yvals = np.zeros((ngroup,ncategory))
yvals[0,:]=[0.195271656,0.103645081,0.108825981,0.919016394]
yvals[1,:]=[0.298916737,0,0.108825981,0.919016394]
yvals[2,:]=[0.407742718,0,0,0.919016394]
yvals[3,:]=[0.590022943,0,0,0.736736169]
yvals[4,:]=[1.326759112,0,0,0]

overallVals = ["46.7Mt/CO<sub>2</sub>/yr","71.5Mt/CO<sub>2</sub>/yr","97.6Mt/CO<sub>2</sub>/yr","141.2Mt/CO<sub>2</sub>/yr","317.6Mt/CO<sub>2</sub>/yr"]

#colors=['#9edae5','#17becf','#dbdb8d','#bcbd22','#c7c7c7','#7f7f7f','#f7b6d2','#e377c2','#c49c94','#8c564b','#c5b0d5']  # TAbleau colormap
colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b']  # reversed TAbleau colormap
#colors=['#17becf','#bcbd22','#7f7f7f','#e377c2','#8c564b','#9467bd','#d62728','#2ca02c','#ff7f0e','#1f77b4','#c5b0d5']
#colors=['#ffbb78','#aec7e8','#bcbd22','#dbdb8d','#e377c2','#c7c7c7','#7f7f7f','#c5b0d5','#c49c94','#8c564b','#f7b6d2']

fig = go.Figure()
for i in range(ncategory):
    fig.add_trace(go.Bar(x=xvals, y=yvals[:,i], marker_color=colors[i],marker_line_width=0.0))


# Change the bar mode
fig.update_layout(
    barmode='stack',
    showlegend=False,
    legend=dict(x=0.022,y=0.96),
    bargap=0.0,
    bargroupgap=0.0,
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1000, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=15,
    uniformtext_mode='show',
    margin=dict(l=100, r=50, t=50, b=50),
    annotations=[
            dict(
                x=xpos, y=ypos-0.05, xref='x', yref='y', showarrow=False,
                text=overallVals[xpos],textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            ) for xpos, ypos in zip([0, 1, 2, 3, 4], yvals[:,0])
    ]+[
            dict(
                x=0.025, y=0.245, xref='paper', yref='y', showarrow=False,
                text='Scenario 1<br>(22.7Mt/CO<sub>2</sub>/yr)',textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
    ]+[
            dict(
                x=0.125, y=0.35, xref='paper', yref='y', showarrow=False,
                text='Scenario 2<br>(47.0Mt/CO<sub>2</sub>/yr)',textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
    ]+[
            dict(
                x=0.4, y=0.85, xref='paper', yref='y', showarrow=False,
                text='Scenario 3<br>(507.5Mt/CO<sub>2</sub>/yr)',textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
    ]
)




fig.update_xaxes(title="Household expenditure level (PPP in USD/day/person)",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True)
fig.update_yaxes(title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",range=[0,1.326759112],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",tickvals=[0.3,0.6,0.9,1.2])

fig.show()