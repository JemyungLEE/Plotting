from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

fig = make_subplots(rows=2, cols=1, row_heights=[0.4,0.35], specs=[[{}],[{}]], vertical_spacing= 0.14)

xval = ["Low-exp.hhs<br>(bottom 20%)",'fd1','el1','gs1','oe1','mc1','pu1','pr1','ed1','cg1','dg1','os1',"Middle-exp.hhs<br>(middle 20%)",'fd2','el2','gs2','oe2','mc2','pu2','pr2','ed2','cg2','dg2','os2',"High-exp.hhs<br>(top 20%)"]

yval = [0.195271655625106,0.0376811910885905,0.0845009348467051,0.00862290981022781,0.0008753035152995,0.0129345952880827,0.012444905891059,0.0061778300357778,0.00262391538716966,0.0256773129526246,0.00748455643827778,0.0134476070302796,0.407742717909,0.096317745427555,0.34501726564858,0.0258923075296434,-0.0046059011001416,0.0623765112142019,0.0825983795579077,0.0390433159804647,0.0164634097566139,0.0731715526021632,0.0978402499440251,0.0849015576958329,1.326759112]
bval = []
for i in range(0,12):
    bval.append(sum(yval[:i]))
bval.append(0)
for i in range(1,12):
    bval.append(sum(yval[:i+12])-yval[12])
bval.append(0)

labels=["Low-exp.hhs<br>(low 20%)",'Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services',"Middle-exp.hhs<br>(middle 20%)",'Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services',"High-exp.hhs<br>(top 20%)"]

fig.add_trace(go.Bar(
        orientation = "v",
        x=xval, y = yval, base = bval,
        marker={'color':['#ffdd71','#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#ffb977','#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#ff9896']},
        marker_line_color='grey',)
        , row=1, col=1
)

ngroup = 10
ncategory = 11
xvals = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]
xvals = ["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"]
xvals = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
xlabels = ['<&#36;1.59','&#36;1.59<br> –1.92','&#36;1.92<br> –2.23','&#36;2.23<br> –2.55','&#36;2.55<br> –2.91'
              ,'&#36;2.91<br> –3.37','&#36;3.37<br> –3.98','&#36;3.98<br> –4.93','&#36;4.93<br> –6.86','>&#36;6.86']
yvals = np.zeros((ncategory, ngroup))
yvals[0,:]=[53.8066049450591,67.5851466739485,75.7955084842472,83.3746031645289,91.2526731283751,100,110.674146162033,124.192903103187,146.763452897857,223.079105753026]
yvals[1,:]=[26.895946280702,41.9589053905245,55.4598497311177,69.7014651357357,82.0118111265841,100,123.626066570094,156.125226800333,217.615678393869,426.462649029623]
yvals[2,:]=[9.00277938539065,21.4791963637218,34.4746149300646,54.4186779618532,74.7816815021447,100,139.528041778838,187.945097026801,255.74814189018,352.352312839605]
yvals[3,:]=[89.9252781902561,98.7804197012262,101.665336445787,100.604446130005,99.9650573131365,100,94.9871263587214,85.6216764749789,74.7811935077745,65.9351125783837]
yvals[4,:]=[27.852480842543,40.4749159974339,53.679556434337,67.9264747038038,82.8669126791331,100,124.939162760074,160.799907745308,224.697191192707,510.594093717834]
yvals[5,:]=[5.01880631264784,14.0313341668937,27.7118720421707,41.8173230842615,66.5633803457105,100,145.383321975545,217.843696603088,341.479743827633,804.254762024881]
yvals[6,:]=[24.2029900125074,39.0349881612968,51.4093901798824,62.9217219473948,82.6843326963592,100,130.626877496749,174.763262592456,262.609911401109,675.053633137284]
yvals[7,:]=[22.5951705481542,38.7693019551753,49.7406077394472,62.1042159707104,79.1793218774671,100,133.8919214921,190.193828891246,282.941307333864,635.530413057679]
yvals[8,:]=[46.7646678546419,60.5098913650157,69.7815712684415,79.2523021281812,88.6906810097945,100,113.467105745811,132.012490327528,162.620073275699,258.100039162094]
yvals[9,:]=[26.6214515145973,37.7930702085975,49.2547547881945,61.1244128751351,77.4522583051642,100,132.180209182993,186.117130683665,314.228300876388,1341.1086372124]
yvals[10,:]=[31.0756495205203,46.5502216686801,57.5489498468329,70.7948205823053,83.8279928220739,100,126.10419824991,161.552899151497,237.071287914009,617.346794647729]
xtvals = [0,10,20,30,40,50,60,70,80,90,100]
ytvals = [300,600,900,1200,1500]

cats=['Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services']
colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b']  # reversed TAbleau colormap


for i in range(ncategory):
    fig.add_trace(go.Scatter(x=xvals, y=np.hstack((yvals[i,:],yvals[i,-1])), name=cats[i],line_shape='hv',line_color=colors[i]),row=2, col=1)

fig.update_traces(mode='lines',row=2, col=1)

fig.update_layout(
    showlegend=False,
    bargap=0.0,
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1000, height=1200,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=18,
    uniformtext_mode='show',
    legend=dict(x=0.045, y=0.96, traceorder='reversed'),
    margin=dict(l=110, r=170, t=40, b=150),

    annotations=[
        dict(
            x=0.6, y=0.455,
            showarrow=False,
            text="(a) Carbon footprints in low, medium and high expenditure households",
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            textangle=0, align='right',
            xref="paper", yref="paper"
        )
    ] + [
        dict(
            x=-0.138, y=1.0,
            showarrow=False,
            text="Household consumption CF per capita<br>(tCO<sub>2</sub>/yr/capita)",
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            textangle=-90,align='right',
            xref="paper", yref="paper"
        )
    ]+[
        dict(
            x=-0.15, y=880,
            showarrow=False,
            text="Relative household consumption CF per capita<br>(50-60%=100)",
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
            textangle=-90,align='right',
            xref="paper", yref="y2"
        )
    ]+[
        dict(
            x=xpos, y=ypos, xref='x1', yref='y1', align='left',
            textangle=270, text=labels[xpos], showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
        ) for xpos, ypos in zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                                [0.14, 0.125, 0.27, 0.18, 0.16, 0.155, 0.22, 0.25, 0.16, 0.23, 0.24,
                                 0.35, 0.398, 0.798, 0.722, 0.7, 0.75, 0.88, 0.945, 0.87, 0.985, 1.08])
    ]+[
        dict(
            x=0.5, y=-0.16, xref="paper", yref="paper", showarrow=False,
            text="Household expenditure level (PPP in USD/day/person)", textangle=0, align='center',
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        )
    ]+[
        dict(
            x=xpos, y=ypos,
            xref='paper', yref='y2', align='left',
            textangle=0, text=cats[xidx], showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
        ) for xidx, xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                        [1.055, 1.1, 1.046, 1.122, 1.1465, 1.154, 1.123, 1.1, 1.172, 1.136, 1.135],
                                        [210, 426.462649029623, 352.352312839605, 65.9351125783837,
                                        510.594093717834, 804.254762024881, 680, 640, 258.100039162094, 1341.1086372124, 600])
    ]+[
        dict(
            x=xpos, y=ypos, xref='x2', yref='paper', align='center',
            textangle=0, text=xlabels[xidx], showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
        ) for xidx, xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                        , [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
                                        , [-0.083, -0.11, -0.11, -0.11, -0.11, -0.11, -0.11, -0.11, -0.11, -0.083])
    ]
)

fig.update_xaxes(ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True,tickvals=[0,12,24],tickangle=0,
                tickfont=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
                row=1, col=1)
fig.update_yaxes(range=[0,1.5],ticks="outside", showline=True, linewidth=2, linecolor='black',mirror="allticks",
                tickfont=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
                tickvals=[0.3,0.6,0.9,1.2,1.5],showticklabels=True,
                row=1, col=1)
fig.update_xaxes(title="",ticks="outside", showline=True, linewidth=2, linecolor='black',
                titlefont=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
                tickfont=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
                mirror="allticks", showticklabels=True, tickvals=xvals, tickformat=",%",
                row=2, col=1)
fig.update_yaxes(range=[0,1500],ticks="outside", showline=True,
                tickfont=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
                linewidth=2, linecolor='black', mirror="allticks",tickvals=ytvals,tickformat=",d",
                row=2, col=1)

fig.show()