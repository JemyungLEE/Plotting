import plotly.graph_objects as go
import numpy as np
import statsmodels.nonparametric.kernel_regression as kr
from scipy import stats
from scipy.optimize import curve_fit
import csv

# X: population density
# Y: CF per capita
# Color: poverty ratio
# Size: overall CF

# regmode="linear"
regmode="exponential"
# regmode="kernel"

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

            if povr[cnt-1]<0.2:
                lowpovdens.append(dens[cnt-1])
                lowpovcfpc.append(cfpc[cnt-1])
            elif 0.2<=povr[cnt-1]<0.5:
                midpovdens.append(dens[cnt-1])
                midpovcfpc.append(cfpc[cnt-1])
            elif 0.5<=povr[cnt-1]<0.8:
                highpovdens.append(dens[cnt-1])
                highpovcfpc.append(cfpc[cnt-1])
            elif 0.8<=povr[cnt-1]<=1.0:
                highpovdens.append(dens[cnt-1])
                highpovcfpc.append(cfpc[cnt-1])
            else: print("poverty ratio is not in the ragnges: ",povr[cnt-1])

            cnt += 1

# topn = 50
# tmporder = (-cfov).argsort()[:topn]
# for i in range(ndistrict):
#     if i in tmporder:
#         topdis.append(districts[i])
#         print(districts[i])
#     else:
#         topdis.append("")

dislist = ['New Delhi','Gurgaon','North West (Delhi)','East (Delhi)','West (Delhi)','Chennai','Kolkata','Mumbai (Suburban)','Leh (Ladakh)','Upper Siang','South Andamans','Bijapur']
for i in range(ndistrict):
    if districts[i] in dislist:
        topdis.append(districts[i])
    else:
        topdis.append("")

# rearrange by ascending order
lowsortidx = np.argsort(lowpovdens)
lowpovdens = np.array(lowpovdens)[lowsortidx]
lowpovcfpc = np.array(lowpovcfpc)[lowsortidx]
midsortidx = np.argsort(midpovdens)
midpovdens = np.array(midpovdens)[midsortidx]
midpovcfpc = np.array(midpovcfpc)[midsortidx]
highsortidx = np.argsort(highpovdens)
highpovdens = np.array(highpovdens)[highsortidx]
highpovcfpc = np.array(highpovcfpc)[highsortidx]


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

elif regmode=="linear":   # linear regression, reg = [slope, intercept, r_value, p_value, std_err]
    lowreg = stats.linregress(lowpovdens,lowpovcfpc)
    midreg = stats.linregress(midpovdens,midpovcfpc)
    highreg = stats.linregress(highpovdens,highpovcfpc)
    lowline = lowreg[0]*lowxvals+lowreg[1]
    midline = midreg[0]*midxvals+midreg[1]
    highline = highreg[0]*highxvals+highreg[1]
elif regmode=="kernel": # Kernel regression
    lowreg = kr.KernelReg(lowpovdens, lowpovcfpc, 'o')
    midreg = kr.KernelReg(midpovdens, midpovcfpc, 'o')
    highreg = kr.KernelReg(highpovdens, highpovcfpc, 'o')
    lowline = lowreg.fit()[0]
    # lowline = lowreg.fit(lowxvals)[0]
    midline = midreg.fit(midxvals)[0]
    highline = highreg.fit(highxvals)[0]

# f = open('/Users/leejmacbook/Desktop/test1.csv', 'w')
# with f:
#     writer = csv.writer(f)
#     writer.writerow(['PopDens','CFperCap'])
#     for i in range(len(lowline)):
#         writer.writerow([lowpovdens[i],lowline[i]])

# max overall CF = 16432009 tCO2/yr
# max poverty ratio = 0.784403432

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dens, y=cfpc,
    mode='markers+text', showlegend=False,
    text=topdis,
    textposition="middle left",
    textfont=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
    marker=dict(
        size = cfov,
        sizemode = 'area',
        sizeref = 2. * 20000000 / (50. ** 2),
        sizemin = 4,
        color = povr, cmin=0.0, cmax=0.8,
        line=dict(width=1, color='grey'),
        showscale=True,
        reversescale=True,
        colorbar=dict(x=1.02, y=0.5/1.125, len=0.926, thickness=22, ticks='outside', tickvals=[0.0, 0.2, 0.4, 0.6, 0.8], tickformat='%',)
    )
))

# regresssion lines
fig.add_trace(go.Scatter(
    x=lowxvals, y=lowline, mode='lines', showlegend=False, name='Linear regression: low poverty',
    marker=go.scatter.Marker(color='gold'),
))
fig.add_trace(go.Scatter(
    x=midxvals, y=midline, mode='lines', showlegend=False, name='Linear regression: low poverty',
    marker=go.scatter.Marker(color='coral'),
))
fig.add_trace(go.Scatter(
    x=highxvals, y=highline, mode='lines', showlegend=False, name='Linear regression: low poverty',
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

if regmode == "linear":
    fig.update_layout(
        annotations=[
            dict(
                x=0.7, y=2.08, xref='x', yref='y', showarrow=False,
                text="Overall CF (MtCO<sub>2</sub>)",textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
        ]+[
            dict(
                x=1.165, y=1, xref='paper', yref='y', showarrow=False,
                text='Poverty ratio (%, people living on less than PPP $1.9 a day)',textangle=90,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            )
        ]+[
            dict(
                x=0.8,
                y=ypos,
                xref='x',
                yref='y',
                align='left',
                textangle=0,
                text=units,
                showarrow=False,
                font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            ) for units, ypos in zip(['1','5','10','20']
                                    , [1.35, 1.5, 1.68, 1.9])
        ]+[
            dict(
                x=4.66, y=1.35, xref='x', yref='y', showarrow=False,
                text='<b>Poverty rate<br><20%</b>', textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]+[
            dict(
                x=4.53, y=1.27, xref='x', yref='y', showarrow=False,
                text='R<sup>2</sup>='+str(round(lowreg[2]**2,2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]+[
            dict(
                x=4.6, y=1.21, xref='x', yref='y', showarrow=False,
                text='y='+'0.000028'+'x+'+str(round(lowreg[1],2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=10, color='black'),
            )
        ]+[
            dict(
                x=4.05, y=0.33, xref='x', yref='y', showarrow=False,
                text='<b>Poverty rate=20%–50%</b>' + '<br>R<sup>2</sup>=' + str(
                    round(midreg[2] ** 2, 2)) + '<br>y=' + '-0.000032' + 'x+' + str(round(midreg[1], 2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ] + [
                        dict(
                            x=3.15, y=0.09, xref='x', yref='y', showarrow=False,
                            text='<b>Poverty rate>50%</b>' + '<br>R<sup>2</sup>=' + str(
                                round(highreg[2] ** 2, 2)) + '<br>y=' + '-0.000034' + 'x+' + str(round(highreg[1], 2)),
                            textangle=0, align='left',
                            font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
                        )
        ]
        # ]+[
        #     dict(
        #         x=4.6, y=1.21, xref='x', yref='y', showarrow=False,
        #         text='y='+'2.8e-5'+'x+'+str(round(lowreg[1],2)),
        #         textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
        #     )
        # ]+[
        #     dict(
        #         x=4.05, y=0.33, xref='x', yref='y', showarrow=False,
        #         text='Poverty rate=20%–50%'+'<br>R<sup>2</sup>='+str(round(midreg[2]**2,2))+'<br>y='+'-3.2e-5'+'x+'+str(round(midreg[1],2)),
        #         textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
        #     )
        # ]+[
        #     dict(
        #         x=3.15, y=0.09, xref='x', yref='y', showarrow=False,
        #         text='Poverty rate>50%'+'<br>R<sup>2</sup>='+str(round(highreg[2]**2,2))+'<br>y='+'-3.4e-5'+'x+'+str(round(highreg[1],2)),
        #         textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
        #     )
        # ]
    )
elif regmode == "exponential":
    fig.update_layout(
        annotations=[
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
        ]+[

            # LinregressResult(slope=0.19608164013149165, intercept=0.1647457974524743, rvalue=0.47648163844667585,
            #                  pvalue=2.9593850596597194e-22, stderr=0.018911684030331125)
            dict(
                x=4.62, y=1.35, xref='x', yref='y', showarrow=False,
                text='<b>Poverty rate<20%</b>', textangle=0, align='right', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
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
        ]+[
            # LinregressResult(slope=-0.03851698910148349, intercept=0.4708586233667753, rvalue=-0.17281178363845584,
            #                  pvalue=0.011331924522525834, stderr=0.01507743196639752)
            dict(
                x=4.15, y=0.428, xref='x', yref='y', showarrow=False,
                text='<b>Poverty rate=20%–50%</b>' + '<br>R<sup>2</sup>=' + str(
                    round(midreg[2] ** 2, 2)) + '<br>y=' +str(round(midreg[0],3))+ ' log<sub>10</sub>(x)+' + str(round(midreg[1], 3)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
            )
        ] + [
            # LinregressResult(slope=-0.052875887708827826, intercept=0.4210152405857929, rvalue=-0.30339806962431964,
            #                  pvalue=0.053812435603929544, stderr=0.02659153626236019)
                        dict(
                            x=4.05, y=0.125, xref='x', yref='y', showarrow=False,
                            text='<b>Poverty rate>50%</b>' + '<br>R<sup>2</sup>=' + str(
                                round(highreg[2] ** 2, 2)) + '<br>y=' +str(round(highreg[0],3))+ ' log<sub>10</sub>(x)+' + str(round(highreg[1], 3)),
                            textangle=0, align='left',
                            font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
                        )
        ]
    )
elif regmode == "kernel":
    fig.update_layout(
        annotations=[
            dict(
                x=0.7, y=2.08, xref='x', yref='y', showarrow=False,
                text="Overall CF (MtCO<sub>2</sub>)",textangle=0,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
            )
        ]+[
            dict(
                x=1.165, y=1, xref='paper', yref='y', showarrow=False,
                text='Poverty ratio (%, people living on less than PPP $1.9 a day)',textangle=90,align='center',
                font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
            )
        ]+[
            dict(
                x=0.8, y=ypos, xref='x', yref='y', align='left', textangle=0, text=units, showarrow=False,
                font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
            ) for units, ypos in zip(['1','5','10','20'], [1.35, 1.5, 1.68, 1.9])
        ]+[
            dict(
                x=4.66, y=1.35, xref='x', yref='y', showarrow=False,
                text='Poverty rate<br><20%', textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]+[
            dict(
                x=4.53, y=1.27, xref='x', yref='y', showarrow=False,
                text='R<sup>2</sup>='+str(round(lowreg.r_squared(),2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]+[
            dict(
                x=4.05, y=0.33, xref='x', yref='y', showarrow=False,
                text='Poverty rate=20%–50%'+'<br>R<sup>2</sup>='+str(round(midreg.r_squared(),2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]+[
            dict(
                x=3.15, y=0.09, xref='x', yref='y', showarrow=False,
                text='Poverty rate>50%'+'<br>R<sup>2</sup>='+str(round(highreg.r_squared(),2)),
                textangle=0, align='left', font=dict(family='/Library/Fonts/SF Pro Display', size=12, color='black'),
            )
        ]
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

# For read data checking
# f = open('/Users/leejmacbook/Desktop/test.csv', 'w')
# with f:
#     writer = csv.writer(f)
#     writer.writerow(['District','CFperCapita','OverallCF','PopDens','Poverty'])
#     for i in range(len(cfpc)):
#         writer.writerow([districts[i],cfpc[i],cfov[i],dens[i],povr[i]])