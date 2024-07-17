import plotly.graph_objects as go
import numpy as np
from scipy import stats
import csv

# X: population density
# Y: CF per capita
# Color: poverty ratio
# Size: overall CF

# expmode = "low"
# expmode = "middle"
# expmode = "high"
expmode = "all"
regmode="exponential"

ndistrict = 623
ncategory = 11
districts = []
categories = []
topdis = [] # store top N% districts
cfpc = np.zeros(ndistrict)  # CF per capita
dens = np.zeros(ndistrict)  # population density
cfov = np.zeros(ndistrict)  # overall CF
mexp = np.zeros(ndistrict)  # mean expenditure

lowexpdens = []   # population density of expenditure per capita <0.1, [district]
midexpdens = []   # population density of expenditure per capita >=0.1, <0.15, [district]
highexpdens = []  # population density of expenditure per capita >=0.15, [district]

lowexpcfpc = []   # CF per capita of expenditure per capita <0.1, [district]
midexpcfpc = []   # CF per capita of expenditure per capita >=0.1, <0.15, [district]
highexpcfpc = []  # CF per capita of expenditure per capita >=0.15, [district]

lowexpcfov = []   # Overall CF of poverty rate <0.1, [district]
midexpcfov = []   # Overall CF of poverty rate >=0.1, <0.15, [district]
highexpcfov = []  # Overall CF of poverty rate >=0.15, [district]

lowexppovr = []   # Poverty rate of poverty rate <0.1, [district]
midexppovr = []   # Poverty rate of poverty rate >=0.1, <0.15, [district]
highexppovr = []  # Poverty rate of poverty rate >=0.15, [district]

lowdistrict = []  # district list of poverty rate <0.1, [district]
middistrict = []  # district list of poverty rate >=0.1, <0.15, [district]
highdistrict = []  # district list of poverty rate >=0.15, [district]

lowthr = 3
midthr = 5
highthr = 7
limitthr = 15

with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_dist_status.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cnt = 0
    for row in reader:
        if cnt == 0:
            categories = row[1:ncategory+1]
            cnt += 1
        else:
            districts.append(row[0])
            cfpc[cnt-1] = row[ncategory+1]
            cfov[cnt-1] = row[ncategory+2]
            dens[cnt-1] = row[ncategory+7]
            mexp[cnt-1] = float(row[ncategory+3]) * 30 # a temporary version: fix the current CSV's district avg MPCE error.
            # mexp[cnt-1] = row[ncategory+3] # it is a correct version

            if mexp[cnt-1]<lowthr:
                lowexpdens.append(dens[cnt-1])
                lowexpcfpc.append(cfpc[cnt-1])
                lowexpcfov.append(cfov[cnt-1])
                lowexppovr.append(mexp[cnt-1])
                lowdistrict.append(row[0])
            elif lowthr<=mexp[cnt-1]<midthr:
                midexpdens.append(dens[cnt-1])
                midexpcfpc.append(cfpc[cnt-1])
                midexpcfov.append(cfov[cnt-1])
                midexppovr.append(mexp[cnt-1])
                middistrict.append(row[0])
            elif midthr<=mexp[cnt-1]<highthr:
                highexpdens.append(dens[cnt-1])
                highexpcfpc.append(cfpc[cnt-1])
                highexpcfov.append(cfov[cnt-1])
                highexppovr.append(mexp[cnt-1])
                highdistrict.append(row[0])
            elif highthr<=mexp[cnt-1]<=limitthr:
                highexpdens.append(dens[cnt-1])
                highexpcfpc.append(cfpc[cnt-1])
                highexpcfov.append(cfov[cnt-1])
                highexppovr.append(mexp[cnt-1])
                highdistrict.append(row[0])
            else: print("poverty ratio is not in the ragnges: ",mexp[cnt-1])

            cnt += 1

print("Low: ", len(lowdistrict), ", Middle: ", len(middistrict), ", High: ", len(highdistrict), "\n")

# topn = 50
# tmporder = (-cfov).argsort()[:topn]
# for i in range(ndistrict):
#     if i in tmporder:
#         topdis.append(districts[i])
#         print(districts[i])
#     else:
#         topdis.append("")

dislist = ['New Delhi','Gurgaon','North West (Delhi)','East (Delhi)','West (Delhi)','Chennai','Kolkata','Mumbai (Suburban)','Leh (Ladakh)','Upper Siang','South Andamans','Bijapur']
if expmode == "middle": dislist += ['Bikaner', 'North East (Delhi)', 'Anjaw', 'Tamenglong']
if expmode == "low": dislist += ['Kurungkumey', 'Vidisha', 'Ukhrul']
for i in range(ndistrict):
    if districts[i] in dislist:
        topdis.append(districts[i])
    else:
        topdis.append("")

for i in range(len(lowdistrict)):
    if not lowdistrict[i] in dislist: lowdistrict[i] = ""
for i in range(len(middistrict)):
    if not middistrict[i] in dislist: middistrict[i] = ""
for i in range(len(highdistrict)):
    if not highdistrict[i] in dislist: highdistrict[i] = ""

# rearrange by ascending order
lowsortidx = np.argsort(lowexpdens)
lowexpdens = np.array(lowexpdens)[lowsortidx]
lowexpcfpc = np.array(lowexpcfpc)[lowsortidx]
lowexpcfov = np.array(lowexpcfov)[lowsortidx]
lowexppovr = np.array(lowexppovr)[lowsortidx]
lowdistrict = np.array(lowdistrict)[lowsortidx]
midsortidx = np.argsort(midexpdens)
midexpdens = np.array(midexpdens)[midsortidx]
midexpcfpc = np.array(midexpcfpc)[midsortidx]
midexpcfov = np.array(midexpcfov)[midsortidx]
midexppovr = np.array(midexppovr)[midsortidx]
middistrict = np.array(middistrict)[midsortidx]
highsortidx = np.argsort(highexpdens)
highexpdens = np.array(highexpdens)[highsortidx]
highexpcfpc = np.array(highexpcfpc)[highsortidx]
highexpcfov = np.array(highexpcfov)[highsortidx]
highexppovr = np.array(highexppovr)[highsortidx]
highdistrict = np.array(highdistrict)[highsortidx]

lowxvals = np.array([i for i in range(1,4*10**3,5)])
midxvals = np.array([i for i in range(1,4*10**4,5)])
highxvals = np.array([i for i in range(1,4*10**4,5)])

if regmode=="exponential":
    loglowexpdens = np.log10(lowexpdens)
    logmidexpdens = np.log10(midexpdens)
    loghighexpdens = np.log10(highexpdens)

    lowreg = stats.linregress(loglowexpdens,lowexpcfpc)
    midreg = stats.linregress(logmidexpdens,midexpcfpc)
    highreg = stats.linregress(loghighexpdens,highexpcfpc)

    lowline = lowreg[0]*np.log10(lowxvals)+lowreg[1]
    midline = midreg[0]*np.log10(midxvals)+midreg[1]
    highline = highreg[0]*np.log10(highxvals)+highreg[1]

# max overall CF = 16432009 tCO2/yr
# max poverty ratio = 0.784403432

if expmode == "all":
    xvals = dens
    yvals = cfpc
    sizes = cfov
    colors = mexp
    dists = topdis
elif expmode == "low":
    xvals = lowexpdens
    yvals = lowexpcfpc
    sizes = lowexpcfov
    colors = lowexppovr
    dists = lowdistrict
elif expmode == "middle":
    xvals = midexpdens
    yvals = midexpcfpc
    sizes = midexpcfov
    colors = midexppovr
    dists = middistrict
elif expmode == "high":
    xvals = highexpdens
    yvals = highexpcfpc
    sizes = highexpcfov
    colors = highexppovr
    dists = highdistrict

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=xvals, y=yvals,
    mode='markers+text', showlegend=False,
    text=dists,
    textposition="middle left",
    textfont=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
    marker=dict(
        size = sizes,
        sizemode = 'area',
        sizeref = 2. * 20000000 / (50. ** 2),
        sizemin = 4,
        color = colors, cmin=0.0, cmax=6,
        line=dict(width=1, color='grey'),
        showscale=True,
        reversescale=False,
        colorbar=dict(x=1.02, y=0.5/1.125, len=0.926, thickness=22, ticks='outside', tickvals=[0, 1.5, 3, 4.5, 6], tickformat='.1f',)
    )
))

# regresssion lines
if expmode == "all" or expmode == "low":
    fig.add_trace(go.Scatter(
        x=lowxvals, y=lowline, mode='lines', showlegend=False, name='Linear regression: low expenditure',
        marker=go.scatter.Marker(color='darkorchid'),
    ))
if expmode == "all" or expmode == "middle":
    fig.add_trace(go.Scatter(
        x=midxvals, y=midline, mode='lines', showlegend=False, name='Linear regression: middle expenditure',
        marker=go.scatter.Marker(color='coral'),
    ))
if expmode == "all" or expmode == "high":
    fig.add_trace(go.Scatter(
        x=highxvals, y=highline, mode='lines', showlegend=False, name='Linear regression: high expenditure',
        marker=go.scatter.Marker(color='gold'),
    ))

# For scale legend
scaleDens =[3.2, 3.2, 3.2, 3.2]
# scaleCFpc = [1.45, 1.6, 1.78, 2.0]
scaleCFpc = [1.45, 1.6, 1.78, 2.0]
scaleCFov = [1000000, 5000000, 10000000, 20000000]
fig.add_trace(go.Scatter(
    x=scaleDens, y=scaleCFpc,
    mode='markers', showlegend=False,
    marker=dict(
        size=scaleCFov,
        sizemode='area',
        sizeref=2. * 20000000 / (50. ** 2),
        sizemin=4,
        color='white',
        line=dict(width=2,color='black'),
    )
))

fig.update_layout(
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1000, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=18,
    uniformtext_mode='show',
    xaxis_type="log",
  #  yaxis_type="log"
    margin=dict(l=100, r=150, t=50, b=50),
)

annot = [
            dict(
                x=0.735, y=2.15, xref='x', yref='y', showarrow=False,
                text="Overall CF (MtCO<sub>2</sub>)",textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
        ]+[
            dict(
                x=1.18, y=1, xref='paper', yref='y', showarrow=False,
                text='Average expenditure (PPP $/day/capita)',textangle=90,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
            )
        ]+[
            dict(
                x=0.85,
                y=ypos,
                xref='x',
                yref='y',
                align='left',
                textangle=0,
                text=units,
                showarrow=False,
                font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
            ) for units, ypos in zip(['1','5','10','20']
                                    , [1.45, 1.6, 1.78, 2.0])
        ]

if expmode == "all" or expmode == "high":
    annot +=[
                dict(
                    x=4.675, y=1.337, xref='x', yref='y', showarrow=False,
                    text='<b>Avg. exp.>'+str("{:.1f}".format(midthr))+'</b>', textangle=0, align='right',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ] + [
                dict(
                    x=4.72, y=1.265, xref='x', yref='y', showarrow=False,
                    text='R<sup>2</sup>=' + str(round(highreg[2] ** 2, 2)),
                    textangle=0, align='left',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ] + [
                dict(
                    x=4.8, y=1.125, xref='x', yref='y', showarrow=False,
                    text='y=' + str(round(highreg[0], 3)) + '<br>log<sub>10</sub>(x)<br>+' + str(round(highreg[1], 3)),
                    textangle=0, align='right',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]
if expmode == "all" or expmode == "middle":
    annot +=[
                dict(
                    x=4.25, y=0.52, xref='x', yref='y', showarrow=False,
                    text='<b>Avg. exp.='+str("{:.1f}".format(lowthr))+'–'+str("{:.1f}".format(midthr))+'</b>' + '<br>R<sup>2</sup>=' + str(
                        round(midreg[2] ** 2, 2)) + '<br>y=' + str(round(midreg[0], 3)) + ' log<sub>10</sub>(x)+' + str(
                        round(midreg[1], 3)),
                    textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]
if expmode == "all" or expmode == "low":
    annot +=[
                dict(
                    x=4.1, y=0.2, xref='x', yref='y', showarrow=False,
                    text='<b>Avg. exp.<'+str("{:.1f}".format(lowthr))+'</b>' + '<br>R<sup>2</sup>=' + str(round(lowreg[2] ** 2, 2))
                         + '<br>y=' + str(round(lowreg[0], 3)) + ' log<sub>10</sub>(x)+' + str(round(lowreg[1], 3)),
                    textangle=0, align='left',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]


if regmode == "exponential":
    fig.update_layout(
        annotations = annot
    )

fig.update_xaxes(title="Population density (persons/km<sup>2</sup>)",titlefont=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black')
                 # ,dtick='D1'
                 ,tickvals=[0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
                 ,ticktext=['0','','','','','','','','','','10','','','','','','','','','10<sup>2</sup>','','','','','','','','','10<sup>3</sup>','','','','','','','','','10<sup>4</sup>','','','','','','','','','10<sup>5</sup>']
                 # ,ticktext=['0','','','','','','','','','','10','','','','','','','','','100','','','','','','','','','1,000','','','','','','','','','10,000','','','','','','','','','100,000']
                 ,tickangle=0
                 ,tickfont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')
                 ,range=[0,5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True)
fig.update_yaxes(title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",titlefont=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black')
                 ,range=[0,2.25],tickvals=[0.0,0.5,1.0,1.5,2.0],tickformat=".1f",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks")


fig.show()