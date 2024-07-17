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
povr = np.zeros(ndistrict)  # poverty ratio

lowpovdens = []   # population density of poverty rate 0-20%, [district]
midpovdens = []   # population density of poverty rate 20-50%, [district]
highpovdens = []  # population density of poverty rate 50-80%, [district]

lowpovcfpc = []   # CF per capita of poverty rate 0-20%, [district]
midpovcfpc = []   # CF per capita of poverty rate 20-50%, [district]
highpovcfpc = []  # CF per capita of poverty rate 50-80%, [district]

lowpovcfov = []   # Overall CF of poverty rate 0-20%, [district]
midpovcfov = []   # Overall CF of poverty rate 20-50%, [district]
highpovcfov = []  # Overall CF of poverty rate 50-80%, [district]

lowpovpovr = []   # Poverty rate of poverty rate 0-20%, [district]
midpovpovr = []   # Poverty rate of poverty rate 20-50%, [district]
highpovpovr = []  # Poverty rate of poverty rate 50-80%, [district]

lowdistrict = []  # district list of poverty rate 0-20%, [district]
middistrict = []  # district list of poverty rate 20-50%, [district]
highdistrict = []  # district list of poverty rate 50-80%, [district]

lowthr = 0.06
midthr = 0.26
highthr = 0.5
limitthr = 1.0

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
            povr[cnt-1] = row[ncategory+8]

            if povr[cnt-1]<lowthr:
                lowpovdens.append(dens[cnt-1])
                lowpovcfpc.append(cfpc[cnt-1])
                lowpovcfov.append(cfov[cnt-1])
                lowpovpovr.append(povr[cnt-1])
                lowdistrict.append(row[0])
            elif lowthr<=povr[cnt - 1]<midthr:
                midpovdens.append(dens[cnt-1])
                midpovcfpc.append(cfpc[cnt-1])
                midpovcfov.append(cfov[cnt-1])
                midpovpovr.append(povr[cnt-1])
                middistrict.append(row[0])
            elif midthr<=povr[cnt-1]<highthr:
                highpovdens.append(dens[cnt-1])
                highpovcfpc.append(cfpc[cnt-1])
                highpovcfov.append(cfov[cnt-1])
                highpovpovr.append(povr[cnt-1])
                highdistrict.append(row[0])
            elif highthr<=povr[cnt-1]<=limitthr:
                highpovdens.append(dens[cnt-1])
                highpovcfpc.append(cfpc[cnt-1])
                highpovcfov.append(cfov[cnt-1])
                highpovpovr.append(povr[cnt-1])
                highdistrict.append(row[0])
            else: print("poverty ratio is not in the ragnges: ",povr[cnt-1])

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
if expmode == "middle": dislist += ['Gautam Buddha Nagar', 'Kodagu', 'Upper Subansiri', 'Nagpur']
if expmode == "high": dislist += ['Narayanpur', 'Kanpur Nagar']
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
lowsortidx = np.argsort(lowpovdens)
lowpovdens = np.array(lowpovdens)[lowsortidx]
lowpovcfpc = np.array(lowpovcfpc)[lowsortidx]
lowpovcfov = np.array(lowpovcfov)[lowsortidx]
lowpovpovr = np.array(lowpovpovr)[lowsortidx]
lowdistrict = np.array(lowdistrict)[lowsortidx]
midsortidx = np.argsort(midpovdens)
midpovdens = np.array(midpovdens)[midsortidx]
midpovcfpc = np.array(midpovcfpc)[midsortidx]
midpovcfov = np.array(midpovcfov)[midsortidx]
midpovpovr = np.array(midpovpovr)[midsortidx]
middistrict = np.array(middistrict)[midsortidx]
highsortidx = np.argsort(highpovdens)
highpovdens = np.array(highpovdens)[highsortidx]
highpovcfpc = np.array(highpovcfpc)[highsortidx]
highpovcfov = np.array(highpovcfov)[highsortidx]
highpovpovr = np.array(highpovpovr)[highsortidx]
highdistrict = np.array(highdistrict)[highsortidx]

lowxvals = np.array([i for i in range(1,4*10**4,5)])
midxvals = np.array([i for i in range(1,5*10**3,5)])
highxvals = np.array([i for i in range(1,4*10**3,5)])

if regmode=="exponential":
    loglowpovdens = np.log10(lowpovdens)
    logmidpovdens = np.log10(midpovdens)
    loghighpovdens = np.log10(highpovdens)

    lowreg = stats.linregress(loglowpovdens,lowpovcfpc)
    midreg = stats.linregress(logmidpovdens,midpovcfpc)
    highreg = stats.linregress(loghighpovdens,highpovcfpc)

    lowline = lowreg[0]*np.log10(lowxvals)+lowreg[1]
    midline = midreg[0]*np.log10(midxvals)+midreg[1]
    highline = highreg[0]*np.log10(highxvals)+highreg[1]

# max overall CF = 16432009 tCO2/yr
# max poverty ratio = 0.784403432

if expmode == "all":
    xvals = dens
    yvals = cfpc
    sizes = cfov
    colors = povr
    dists = topdis
elif expmode == "low":
    xvals = lowpovdens
    yvals = lowpovcfpc
    sizes = lowpovcfov
    colors = lowpovpovr
    dists = lowdistrict
elif expmode == "middle":
    xvals = midpovdens
    yvals = midpovcfpc
    sizes = midpovcfov
    colors = midpovpovr
    dists = middistrict
elif expmode == "high":
    xvals = highpovdens
    yvals = highpovcfpc
    sizes = highpovcfov
    colors = highpovpovr
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
        color = colors, cmin=0.0, cmax=0.8,
        line=dict(width=1, color='grey'),
        showscale=True,
        reversescale=True,
        colorbar=dict(x=1.02, y=0.5/1.125, len=0.926, thickness=22, ticks='outside', tickvals=[0.0, 0.2, 0.4, 0.6, 0.8], tickformat='%',)
    )
))

# regresssion lines
if expmode == "all" or expmode == "low":
    fig.add_trace(go.Scatter(
        x=lowxvals, y=lowline, mode='lines', showlegend=False, name='Linear regression: low poverty',
        marker=go.scatter.Marker(color='gold'),
    ))
if expmode == "all" or expmode == "middle":
    fig.add_trace(go.Scatter(
        x=midxvals, y=midline, mode='lines', showlegend=False, name='Linear regression: middle poverty',
        marker=go.scatter.Marker(color='coral'),
    ))
if expmode == "all" or expmode == "high":
    fig.add_trace(go.Scatter(
        x=highxvals, y=highline, mode='lines', showlegend=False, name='Linear regression: high poverty',
        marker=go.scatter.Marker(color='darkorchid'),
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
                text='Poverty ratio (%, people living on less than PPP $1.9 a day)',textangle=90,align='center',
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

if expmode == "all" or expmode == "low":
    annot +=[
                dict(
                    x=4.62, y=1.35, xref='x', yref='y', showarrow=False,
                    text='<b>Poverty rate<' + str(int(lowthr * 100)) + '%</b>', textangle=0, align='right', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]+[
                dict(
                    x=4.72, y=1.285, xref='x', yref='y', showarrow=False,
                    text='R<sup>2</sup>='+str(round(lowreg[2]**2,2)),
                    textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]+[
                dict(
                    x=4.82, y=1.16, xref='x', yref='y', showarrow=False,
                    text='y='+str(round(lowreg[0],3))+'<br>log<sub>10</sub>(x)<br>+'+str(round(lowreg[1],3)),
                    textangle=0, align='right', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]
if expmode == "all" or expmode == "middle":
    annot +=[
                dict(
                    x=4.15, y=0.51, xref='x', yref='y', showarrow=False,
                    # x=4.15, y=0.428, xref='x', yref='y', showarrow=False,
                    text='<b>Poverty rate=' + str(int(lowthr * 100)) + '%–' + str(int(midthr * 100)) + '%</b>' + '<br>R<sup>2</sup>=' + str(
                        round(midreg[2] ** 2, 2)) + '<br>y=' + str(round(midreg[0], 3)) + ' log<sub>10</sub>(x)+' + str(
                        round(midreg[1], 3)),
                    textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]
if expmode == "all" or expmode == "high":
    annot +=[
                dict(
                    x=4.05, y=0.18, xref='x', yref='y', showarrow=False,
                    # x=4.05, y=0.125, xref='x', yref='y', showarrow=False,
                    text='<b>Poverty rate>' + str(int(midthr * 100)) + '%</b>' + '<br>R<sup>2</sup>='
                         + str(round(highreg[2] ** 2, 2)) + '<br>y=' +str(round(highreg[0],3))+ ' log<sub>10</sub>(x)+' + str(round(highreg[1], 3)),
                    textangle=0, align='left',
                    font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                )
            ]

if regmode == "exponential":
    fig.update_layout(
        annotations= annot
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