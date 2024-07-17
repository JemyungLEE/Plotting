import plotly.graph_objects as go
import numpy as np
import statsmodels.nonparametric.kernel_regression as kr
from scipy import stats
from scipy.optimize import curve_fit
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
cnt = 0
stctpop = [(i+1)/ngr*totpop for i in range(ngr)]
firstCF = 0
secondCF = 0
thirdCF = 0
for i in range(ngr):
    avgcf = 0
    grpop = 0
    stctsize = 0
    while cumpop<stctpop[i] and cnt<nh:
        cumpop += hhpopwgh[cnt]
        grpop += hhpopwgh[cnt]
        avgcf += hhcf[cnt]*hhwgh[cnt]
        stctsize += hhsize[cnt]
        stctmpce[i] += hhmpce[cnt]*hhpopwgh[cnt]
        cnt += 1
    pctavg[i] = avgcf/grpop
    stctmpce[i] /= grpop
    if stctmpce[i]<1.9: firstCF = pctavg[i]
    if stctmpce[i]<3.0: secondCF = pctavg[i]
    if stctmpce[i]<5.0: thirdCF = pctavg[i]
    # print(i,"\t",stctmpce[i])
    # print(i,"\t",avgcf,"\t",stctsize,"\t",grpop,"\t",cumpop,"\t",pctavg[i])

xvals = [(i+1)/ngr for i in range(ngr)]

allevFirst = np.zeros(ngr)
allevSecond = np.zeros(ngr)
allevThird = np.zeros(ngr)

for i in range(ngr):
    if stctmpce[i] < 1.9:
        allevFirst[i] = firstCF - pctavg[i]
        allevSecond[i] = secondCF - pctavg[i]
        allevThird[i] = thirdCF - pctavg[i]
    elif  stctmpce[i] < 3.0:
        allevFirst[i] = 0
        allevSecond[i] = secondCF - pctavg[i]
        allevThird[i] = thirdCF - pctavg[i]
    elif  stctmpce[i] < 5.0:
        allevFirst[i] = 0
        allevSecond[i] = 0
        allevThird[i] = thirdCF - pctavg[i]

fig = go.Figure()

fig.add_trace(go.Bar(
        orientation = "v",
        x=xvals, y = allevThird, base = pctavg,marker_line_width=0.0,
        marker_color = 'gold',
     #   marker={'color':['#ffdd71','#2ca02c','#98df8a']},
))
fig.add_trace(go.Bar(
        orientation = "v",
        x=xvals, y = allevSecond, base = pctavg,marker_line_width=0.0,
        marker_color = 'coral',
     #   marker={'color':['#ffdd71','#2ca02c','#98df8a']},
))
fig.add_trace(go.Bar(
        orientation = "v",
        x=xvals, y = allevFirst, base = pctavg,marker_line_width=0.0,
        marker_color = 'darkorchid',
     #   marker={'color':['#ffdd71','#2ca02c','#98df8a']},
))

fig.add_trace(go.Scatter(
    x=xvals, y=pctavg,
    mode='lines', showlegend=False,
    text='',
    textposition="middle left",
    textfont=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
    line_color = 'blue',
))

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
                    x=0.23, y=0.10, xref='x', yref='y', showarrow=False,
                    text='Scenario 1: 13.3Mt/CO<sub>2</sub>/yr (1.97%▲)',textangle=0,align='left',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=0.52, y=0.25, xref='x', yref='y', showarrow=False,
                    text='Scenario 2: 82.3Mt/CO<sub>2</sub>/yr (12.19%▲)',textangle=0,align='left',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]+[
                dict(
                    x=0.65, y=0.9, xref='x', yref='y', showarrow=False,
                    text='Scenario 3<br>333.1Mt/CO<sub>2</sub>/yr (49.36%▲)',textangle=0,align='center',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                )
        ]
)

fig.update_xaxes(title="Household expenditure-level (%)",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True,tickvals=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
fig.update_yaxes(title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",range=[0,3.5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",tickvals=[1.0,2.0,3.0])


fig.show()