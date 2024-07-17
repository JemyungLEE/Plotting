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

ngr = 100
pctavg = np.zeros(ngr)
stctmpce = np.zeros(ngr)
cumpop = 0
nextcumpop = hhpopwgh[0]
cnt = 0
stctpop = np.array([i/ngr*totpop for i in range(ngr+1)])
# stctpop = np.array([(i+1)/ngr*totpop for i in range(ngr)])
expTick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expTag = ['','$1','$2','$3','$4','$5','','','','','$10','']
expTickPop = np.zeros(len(expTick))
expidx = 0
povline = 1.9
povpop = 0

idxFirst = 0; idxSecond = 0; idxThird = 0
popFirst = np.zeros(2); popSecond = np.zeros(2); popThird = np.zeros(2)
avgcfFirst = np.zeros(2); avgcfSecond = np.zeros(2); avgcfThird = np.zeros(2)

for i in range(ngr):
    avgcf = 0
    grpop = 0
    stctsize = 0
    while nextcumpop<stctpop[i+1] and cnt<nh:
        cumpop += hhpopwgh[cnt]
        grpop += hhpopwgh[cnt]
        avgcf += hhcf[cnt]*hhwgh[cnt]
        stctsize += hhsize[cnt]
        stctmpce[i] += hhmpce[cnt]*hhpopwgh[cnt]
        if expidx<len(expTick) and hhmpce[cnt]<=expTick[expidx]:
            expTickPop[expidx] = cumpop
            if hhmpce[cnt+1]>expTick[expidx]: expidx += 1
        if hhmpce[cnt-1]<povline and hhmpce[cnt]>=povline: povpop = cumpop

        if cnt+1<nh and hhmpce[cnt]<1.9 and hhmpce[cnt+1]>=1.9:
            idxFirst = i
            popFirst[0] = cumpop
            popFirst[1] = cumpop + hhpopwgh[cnt+1]
        elif cnt+1<nh and hhmpce[cnt]<3.0 and hhmpce[cnt+1]>=3.0:
            idxSecond = i
            popSecond[0] = cumpop
            popSecond[1] = cumpop + hhpopwgh[cnt+1]
        elif cnt+1<nh and hhmpce[cnt]<5.0 and hhmpce[cnt+1]>=5.0:
            idxThird = i
            popThird[0] = cumpop
            popThird[1] = cumpop + hhpopwgh[cnt+1]

        cnt += 1

        if cnt<nh: nextcumpop += hhpopwgh[cnt]
    pctavg[i] = avgcf/grpop
    stctmpce[i] /= grpop

    # print(i,"\t",stctmpce[i],"\t",cumpop)
    # print(i,"\t",avgcf,"\t",stctsize,"\t",grpop,"\t",cumpop,"\t",pctavg[i])
# print(stctpop[-1],"\t",totpop,"\t",cumpop)

# xvals = [(i+1)/ngr for i in range(ngr)]
xvals = [(stctpop[i]+stctpop[i+1])/2/(10**9) for i in range(ngr)]
expTickPop /= 10**9
povpop /= 10**9
popFirst /= 10**9
popSecond /= 10**9
popThird /= 10**9

if popFirst[0] <= xvals[idxFirst]:
    avgcfFirst[0] = pctavg[idxFirst-1]
    if pctavg[idxFirst]>pctavg[idxFirst-1]: avgcfFirst[0] += (pctavg[idxFirst]-pctavg[idxFirst-1])/(xvals[idxFirst]-xvals[idxFirst-1])*(popFirst[0]-xvals[idxFirst-1])
elif popFirst[0] > xvals[idxFirst]:
    avgcfFirst[0] = pctavg[idxFirst]
    if pctavg[idxFirst+1]>pctavg[idxFirst]: avgcfFirst[0] += (pctavg[idxFirst+1]-pctavg[idxFirst])/(xvals[idxFirst+1]-xvals[idxFirst])*(popFirst[0]-xvals[idxFirst])
if popFirst[1] <= xvals[idxFirst]:
    avgcfFirst[1] = pctavg[idxFirst-1]
    if pctavg[idxFirst]>pctavg[idxFirst-1]: avgcfFirst[1] += (pctavg[idxFirst]-pctavg[idxFirst-1])/(xvals[idxFirst]-xvals[idxFirst-1])*(popFirst[1]-xvals[idxFirst-1])
elif popFirst[1] > xvals[idxFirst]:
    avgcfFirst[1] = pctavg[idxFirst]
    if pctavg[idxFirst+1]>pctavg[idxFirst]: avgcfFirst[1] += (pctavg[idxFirst+1]-pctavg[idxFirst])/(xvals[idxFirst+1]-xvals[idxFirst])*(popFirst[1]-xvals[idxFirst])

if popSecond[0] <= xvals[idxSecond]:
    avgcfSecond[0] = pctavg[idxSecond-1]
    if pctavg[idxSecond]>pctavg[idxSecond-1]: avgcfSecond[0] += (pctavg[idxSecond]-pctavg[idxSecond-1])/(xvals[idxSecond]-xvals[idxSecond-1])*(popSecond[0]-xvals[idxSecond-1])
elif popSecond[0] > xvals[idxSecond]:
    avgcfSecond[0] = pctavg[idxSecond]
    if pctavg[idxSecond+1] > pctavg[idxSecond]: avgcfSecond[0] += (pctavg[idxSecond+1]-pctavg[idxSecond])/(xvals[idxSecond+1]-xvals[idxSecond])*(popSecond[0]-xvals[idxSecond])
if popSecond[1] <= xvals[idxSecond]:
    avgcfSecond[1] = pctavg[idxSecond-1]
    if pctavg[idxSecond] > pctavg[idxSecond-1]: avgcfSecond[1] += (pctavg[idxSecond]-pctavg[idxSecond-1])/(xvals[idxSecond]-xvals[idxSecond-1])*(popSecond[1]-xvals[idxSecond-1])
elif popSecond[1] > xvals[idxSecond]:
    avgcfSecond[1] = pctavg[idxSecond]
    if pctavg[idxSecond+1] > pctavg[idxSecond]: avgcfSecond[1] += (pctavg[idxSecond+1]-pctavg[idxSecond])/(xvals[idxSecond+1]-xvals[idxSecond])*(popSecond[1]-xvals[idxSecond])

if popThird[0] <= xvals[idxThird]:
    avgcfThird[0] = pctavg[idxThird-1]
    if pctavg[idxThird]>pctavg[idxThird-1]: avgcfThird[0] += (pctavg[idxThird]-pctavg[idxThird-1])/(xvals[idxThird]-xvals[idxThird-1])*(popThird[0]-xvals[idxThird-1])
elif popThird[0] > xvals[idxThird]:
    avgcfThird[0] = pctavg[idxThird]
    if pctavg[idxThird+1] > pctavg[idxThird]: avgcfThird[0] += (pctavg[idxThird+1]-pctavg[idxThird])/(xvals[idxThird+1]-xvals[idxThird])*(popThird[0]-xvals[idxThird])
if popThird[1] <= xvals[idxThird]:
    avgcfThird[1] = pctavg[idxThird-1]
    if pctavg[idxThird] > pctavg[idxThird-1]: avgcfThird[1] += (pctavg[idxThird]-pctavg[idxThird-1])/(xvals[idxThird]-xvals[idxThird-1])*(popThird[1]-xvals[idxThird-1])
elif popThird[1] > xvals[idxThird]:
    avgcfThird[1] = pctavg[idxThird]
    if pctavg[idxThird+1] > pctavg[idxThird]: avgcfThird[1] += (pctavg[idxThird+1]-pctavg[idxThird])/(xvals[idxThird+1]-xvals[idxThird])*(popThird[1]-xvals[idxThird])

fig = make_subplots(rows=2, cols=1, row_heights=[0.85,0.15], specs=[[{}],[{}]], vertical_spacing = 0.05)

xvalsFirst = np.array([])
yvalsFirst = np.array([])
xvalsSecond = np.array([])
yvalsSecond = np.array([])
xvalsThird = np.array([])
yvalsThird = np.array([])
for i in range(ngr):
    if stctmpce[i] < 1.9:
        xvalsFirst = np.append(xvalsFirst, xvals[i])
        yvalsFirst = np.append(yvalsFirst, pctavg[i])
    elif stctmpce[i] < 3.0:
        xvalsSecond = np.append(xvalsSecond, xvals[i])
        yvalsSecond = np.append(yvalsSecond, pctavg[i])
    elif stctmpce[i] < 5.0:
        xvalsThird = np.append(xvalsThird, xvals[i])
        yvalsThird = np.append(yvalsThird, pctavg[i])
xvalsFirst = np.append(xvalsFirst, popFirst[0])
yvalsFirst = np.append(yvalsFirst, avgcfFirst[0])
xvalsSecond = np.append(popFirst[1], xvalsSecond)
xvalsSecond = np.append(xvalsSecond, popSecond[0])
yvalsSecond = np.append(avgcfFirst[1], yvalsSecond)
yvalsSecond = np.append(yvalsSecond, avgcfSecond[0])
xvalsThird = np.append(popSecond[1], xvalsThird)
xvalsThird = np.append(xvalsThird, popThird[0])
yvalsThird = np.append(avgcfSecond[1], yvalsThird)
yvalsThird = np.append(yvalsThird, avgcfThird[0])

xvalsFirst = np.append(xvalsFirst, [xvalsFirst[0], xvalsFirst[0]])
yvalsFirst = np.append(yvalsFirst, [yvalsFirst[-1], yvalsFirst[0]])
xvalsSecond = np.append(xvalsSecond, [xvalsSecond[0], xvalsSecond[0]])
yvalsSecond = np.append(yvalsSecond, [yvalsSecond[-1], yvalsSecond[0]])
xvalsThird = np.append(xvalsThird, [xvalsThird[0], xvalsThird[0]])
yvalsThird = np.append(yvalsThird, [yvalsThird[-1], yvalsThird[0]])

fig.add_trace(go.Scatter(x=xvalsFirst, y=yvalsFirst, mode='none', fill='toself', fillcolor='darkorchid'), row=1, col=1)
fig.add_trace(go.Scatter(x=xvalsSecond, y=yvalsSecond, mode='none', fill='toself', fillcolor='coral'), row=1, col=1)
fig.add_trace(go.Scatter(x=xvalsThird, y=yvalsThird, mode='none', fill='toself', fillcolor='gold'), row=1, col=1)

fig.add_trace(go.Scatter(x=xvals, y=pctavg, mode='lines', showlegend=False, line_width=2, line_color = 'blue',), row=1, col=1)

fig.add_trace(go.Scatter(x=[povpop,povpop], y = [0.0,1.0], mode='lines+text', line_width=2, line_color = 'firebrick',
                         text=['','$1.9 '], textposition='top center', textfont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='firebrick')), row=1, col=1)

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
                    x=0.117, y=0.55, xref='x', yref='y', showarrow=False,
                    text='<b>Scenario 1</b><br>13.3Mt/CO<sub>2</sub>/yr<br>(1.97%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=0.4, y=0.72, xref='x', yref='y', showarrow=False,
                    text='<b>Scenario 2</b><br>36.2Mt/CO<sub>2</sub>/yr<br>(5.36%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=0.8, y=1.05, xref='x', yref='y', showarrow=False,
                    text='<b>Scenario 3</b><br>69.9Mt/CO<sub>2</sub>/yr<br>(10.36%▲)',textangle=0,align='center',
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
startingXpos = xvals[0]
# startingXpos = 0
expTickPop = np.append(np.append(0,expTickPop),1.199)
# expTickPop = np.append(np.append(startingXpos,expTickPop),1.199)

fig.update_xaxes(
    title="Household daily expenditure per person (PPP USD/day/capita)", titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    ticks="outside", showline=True, linewidth=2, linecolor='black', mirror=False,
    showticklabels=True, tickvals=expTickPop, tickformat='.3f', ticktext=expTag, tickangle=0,
    anchor="free", side="bottom", position=0.1,
    range=[startingXpos,1.2],
    row=2, col=1,
)
fig.update_xaxes(
    # title="Cumulative population (Billion persons)", titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",
    showticklabels=True, tickvals=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], tickformat='.1f',
    range=[startingXpos, 1.2],
    row=1, col=1,
)

fig.update_yaxes(
    title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",
    titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    range=[0, 4.2], ticks="outside", tickformat='.1f', tickvals=[1.0, 2.0, 3.0, 4.0],
    showline=True, linewidth=2, linecolor='black', mirror="allticks",
    row=1, col=1,
)
fig.update_yaxes(
    range=[0,0],showline=False,zeroline=False, visible=False,
    row=2, col=1,
)

fig.show()