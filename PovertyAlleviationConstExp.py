from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import csv

hhcf = []
hhsize = []
hhmpce = []
hhwgh = []
hhpopwgh = []

with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_hhs_emission_cat.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cnt = 0
    for row in reader:
        if cnt > 0:
            hhcf.append(float(row[12]))
            hhsize.append(float(row[13]))
            hhmpce.append(float(row[14]))
            hhwgh.append(float(row[15]))
            hhpopwgh.append(float(row[13])*float(row[15]))
        cnt += 1
nh = len(hhcf)
totpop = sum(hhpopwgh)
ordidx = np.argsort(hhmpce)
hhsize = np.array(hhsize)[ordidx]
hhwgh = np.array(hhwgh)[ordidx]
hhcf = np.array(hhcf)[ordidx]
hhpopwgh = np.array(hhpopwgh)[ordidx]
hhmpce = np.array(hhmpce)[ordidx]

span = 0.1; min = 1.0; max = 7.0
ngr = int((max-min)/span)+2
pctavg = np.zeros(ngr)
thrmpce = np.arange(start=1, stop=7.01, step=0.1)  # threshold mpce
stctmpce = np.zeros(ngr)
cumpop = 0
stctpop = np.zeros(ngr)
expTick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expTag = ['','$1','$2','$3','$4','$5','$6','$7','>$7']
popTick = [0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.19, 1.2]
popTickExp = np.zeros(len(popTick))
expidx = 0
povline = 1.9

cnt = 0
for i in range(ngr-1):
    avgcf = 0
    grpop = 0
    stctsize = 0
    while hhmpce[cnt]<thrmpce[i] and cnt<nh:
        cumpop += hhpopwgh[cnt]
        grpop += hhpopwgh[cnt]
        avgcf += hhcf[cnt]*hhwgh[cnt]
        stctsize += hhsize[cnt]
        stctmpce[i] += hhmpce[cnt]*hhpopwgh[cnt]
        if cumpop<=popTick[expidx]*(10**9) and cumpop + hhpopwgh[cnt+1]>  popTick[expidx]*(10**9):
            popTickExp[expidx] = hhmpce[cnt]
            expidx += 1
        cnt += 1
    pctavg[i] = avgcf/grpop
    stctmpce[i] /= grpop
while cnt<nh:   # for over-$10-group
    cumpop += hhpopwgh[cnt]
    grpop += hhpopwgh[cnt]
    avgcf += hhcf[cnt] * hhwgh[cnt]
    stctsize += hhsize[cnt]
    stctmpce[ngr-1] += hhmpce[cnt] * hhpopwgh[cnt]
    cnt += 1
pctavg[ngr-1] = avgcf / grpop
stctmpce[ngr-1] /= grpop

    # print(i,"\t",stctmpce[i],"\t",cumpop)
    # print(i,"\t",avgcf,"\t",stctsize,"\t",grpop,"\t",cumpop,"\t",pctavg[i])
# print(stctpop[-1],"\t",totpop,"\t",cumpop)

# xvals = [(i+1)/ngr for i in range(ngr)]
# xvals = np.append(thrmpce[0]-0.1, thrmpce)
xvals = np.append(thrmpce, thrmpce[-1]+1)
# xvals = np.append(np.append(thrmpce[0]-0.1, thrmpce), thrmpce[-1]+1)

fig = make_subplots(rows=2, cols=1, row_heights=[0.85,0.15], specs=[[{}],[{}]], vertical_spacing = 0.05)

xvalsFirst = np.array([])
yvalsFirst = np.array([])
xvalsSecond = np.array([])
yvalsSecond = np.array([])
xvalsThird = np.array([])
yvalsThird = np.array([])
for i in range(ngr-1):
    if xvals[i] <= 1.91:
        xvalsFirst = np.append(xvalsFirst, xvals[i])
        yvalsFirst = np.append(yvalsFirst, pctavg[i])
    elif xvals[i]  <= 3.01:
        xvalsSecond = np.append(xvalsSecond, xvals[i])
        yvalsSecond = np.append(yvalsSecond, pctavg[i])
    elif xvals[i]  <= 5.01:
        xvalsThird = np.append(xvalsThird, xvals[i])
        yvalsThird = np.append(yvalsThird, pctavg[i])

xvalsFirst = np.append(xvalsFirst, [xvalsFirst[0], xvalsFirst[0]])
yvalsFirst = np.append(yvalsFirst, [yvalsFirst[-1], yvalsFirst[0]])
xvalsSecond = np.append(xvalsSecond, [xvalsSecond[0], xvalsSecond[0]])
yvalsSecond = np.append(yvalsSecond, [yvalsSecond[-1], yvalsSecond[0]])
xvalsThird = np.append(xvalsThird, [xvalsThird[0], xvalsThird[0]])
yvalsThird = np.append(yvalsThird, [yvalsThird[-1], yvalsThird[0]])

fig.add_trace(go.Scatter(x=xvalsFirst, y=yvalsFirst, mode='none', fill='toself', fillcolor='darkorchid'), row=1, col=1)
fig.add_trace(go.Scatter(x=xvalsSecond, y=yvalsSecond, mode='none', fill='toself', fillcolor='coral'), row=1, col=1)
fig.add_trace(go.Scatter(x=xvalsThird, y=yvalsThird, mode='none', fill='toself', fillcolor='gold'), row=1, col=1)

fig.add_trace(go.Bar(orientation = "v", x=[povline], y = [1.0], base = [0], width=0.0034, marker_line_width=0.0, marker_color = 'firebrick',
                     text='$1.9 ', textposition='outside',textfont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='firebrick')), row=1, col=1)

fig.add_trace(go.Scatter(x=xvals, y=pctavg, mode='lines', showlegend=False, line_width=2, line_color = 'blue',), row=1, col=1)

fig.add_trace(go.Scatter(x=xvals, y=[]), row=2, col=1)

fig.update_layout(
    barmode='stack',
    showlegend=False,
    bargap=0.0,
    bargroupgap=0.0,
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1000, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=15,
    uniformtext_mode='show',
    margin=dict(l=100, r=150, t=50, b=100),
    annotations=[
                dict(
                    x=1.2, y=0.42, xref='x', yref='y', showarrow=False,
                    text='Scenario 1<br>13.3Mt/CO<sub>2</sub>/yr<br>(1.97%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=2.5, y=0.62, xref='x', yref='y', showarrow=False,
                    text='Scenario 2<br>36.2Mt/CO<sub>2</sub>/yr<br>(5.36%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=3.8, y=0.95, xref='x', yref='y', showarrow=False,
                    text='Scenario 3<br>69.9Mt/CO<sub>2</sub>/yr<br>(10.36%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=1.15, y=0.143, xref='paper', yref='paper', showarrow=False,
                    text='Cumulative<br>population<br>(billions)',textangle=0,align='right',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]
        # ]+[
        #         dict(
        #             x=1.06, y=0.04685, xref='paper', yref='paper', showarrow=False,
        #             text='>$10',textangle=0,align='right',
        #             font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        #         )
        # ],
        #         dict(
        #             x=-0.043, y=0.08, xref='paper', yref='paper', showarrow=False,
        #             text='<$1',textangle=0,align='right',
        #             font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        #         )
        # ]+[
        #         dict(
        #             x=1.072, y=0.08, xref='paper', yref='paper', showarrow=False,
        #             text='>$10',textangle=0,align='right',
        #             font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        #         )
        # ],

)
startXpos = xvals[0]
endXpos = xvals[-1]

# startingXpos = 0
# popTickExp = np.append(np.append(0,popTickExp),1.199)
# expTickPop = np.append(np.append(startingXpos,expTickPop),1.199)

expTick = np.append(np.append(startXpos, expTick), endXpos)

fig.update_xaxes(
    title="Household daily expenditure per person (PPP USD/day/capita)", titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=False,
    showticklabels=True, tickvals=expTick, ticktext=expTag, tickangle=0,
    anchor="free", side="bottom", position=0.1,
    range=[startXpos, endXpos],
    row=2, col=1,
)
fig.update_xaxes(
    # title="Cumulative population (Billion persons)", titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",
    showticklabels=True, tickvals=popTickExp, tickformat='.1f', ticktext=['0.2', '0.4', '0.6', '0.8', '1.0', '1.2'],
    range=[startXpos, endXpos],
    row=1, col=1,
)

fig.update_yaxes(
    title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",
    titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    range=[0, 3.0], ticks="outside", tickformat='.1f', tickvals=[1.0, 2.0, 3.0],
    showline=True, linewidth=2, linecolor='black', mirror="allticks",
    row=1, col=1,
)
fig.update_yaxes(
    range=[0,0],showline=False,zeroline=False, visible=False,
    row=2, col=1,
)

fig.show()