import plotly.graph_objects as go
import numpy as np
import csv

xval = ["Low-exp.hhs<br>(bottom 20%)",'fd1','el1','gs1','oe1','mc1','pu1','pr1','ed1','cg1','dg1','os1',"Middle-exp.hhs<br>(middle 20%)",'fd2','el2','gs2','oe2','mc2','pu2','pr2','ed2','cg2','dg2','os2',"High-exp.hhs<br>(top 20%)"]

ngroup = 5
ncategory = 11
yvals = np.zeros((ngroup,ncategory))
with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_hhs_emission_inc_perCap.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cnt = 0
    for row in reader:
        if cnt == 0:
            cats = row[2:ncategory+2]
            cnt += 1
        elif cnt > 0:
            yvals[cnt-1,:]=row[2:ncategory+2]
            cnt += 1

yval = np.zeros(2*ncategory+3)
yval[0] = sum(yvals[0,:])
yval[1:ncategory+1] = [yvals[2,i] - yvals[0,i] for i in range(ncategory)]
yval[ncategory+1] = sum(yvals[2,:])

print(yval)

yval[ncategory+2:-1] = [yvals[-1,i] - yvals[2,i] for i in range(ncategory)]
yval[-1] = sum(yvals[-1,:])

print(yval)

# yval = [0.195271655625106,0.0376811910885905,0.0845009348467051,0.00862290981022781,0.0008753035152995,0.0129345952880827,0.012444905891059,0.0061778300357778,0.00262391538716966,0.0256773129526246,0.00748455643827778,0.0134476070302796,0.407742717909,0.096317745427555,0.34501726564858,0.0258923075296434,-0.0046059011001416,0.0623765112142019,0.0825983795579077,0.0390433159804647,0.0164634097566139,0.0731715526021632,0.0978402499440251,0.0849015576958329,1.326759112]
bval = []
for i in range(0,12):
    bval.append(sum(yval[:i]))
bval.append(0)
for i in range(1,12):
    bval.append(sum(yval[:i+12])-yval[12])
bval.append(0)

labels=["Low-exp.hhs<br>(low 20%)",'Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services',"Middle-exp.hhs<br>(middle 20%)",'Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services',"High-exp.hhs<br>(top 20%)"]

fig = go.Figure(go.Bar(
        orientation = "v",
        x=xval, y = yval, base = bval,
        marker={'color':['#ffdd71','#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#ffb977','#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#ff9896']},
        marker_line_color='grey',
))

fig.update_layout(
    showlegend=False,
    bargap=0.0,
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1200, height=1000,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=18,
    uniformtext_mode='show',

    annotations=[
        dict(
            x=-0.08,
            y=0.75,
            showarrow=False,
            text="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",
            textangle=-90,
            xref="paper",
            yref="y"
        )
    ]+[
        dict(
            x=xpos,
            y=ypos,
            xref='x',
            yref='y',
            align='left',
            textangle=270,
            text=labels[xpos],
            showarrow=False,
        ) for xpos, ypos in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                                [0.14, 0.125, 0.27, 0.18, 0.16, 0.155, 0.22, 0.25, 0.16, 0.23, 0.24,
                                 0.35, 0.398, 0.798, 0.722, 0.7, 0.75, 0.88, 0.945, 0.87, 0.985, 1.08])
        # dict(
        #     x=xpos,
        #     y=ypos,
        #     xref='x',
        #     yref='y',
        #     align='left',
        #     textangle=270,
        #     text=labels[xpos],
        #     showarrow=False,
        # ) for xpos, ypos in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        #                         [0.145, 0.15, 0.275, 0.225, 0.21, 0.215, 0.255, 0.28, 0.215, 0.275, 0.285,
        #                          0.36, 0.42, 0.81, 0.77, 0.755, 0.805, 0.92, 0.972, 0.93, 1.03, 1.13])
    ],
)

fig.update_xaxes(ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True,tickvals=[0,12,24],tickangle=0)
fig.update_yaxes(range=[0,1.5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",tickvals=[0.3,0.6,0.9,1.2,1.5],showticklabels=True)

fig.show()
#fig.write_image("/Users/leejmacbook/Desktop/test.png")