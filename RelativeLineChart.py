import plotly.graph_objects as go
#import plotly.offline as po
import numpy as np
import csv

ngroup = 10
ncategory = 11
cats = []
xvals = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]
xvals = ["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"]
xvals = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

xlabels = ['<&#36;1.56','&#36;1.56<br> –1.88','&#36;1.88<br> –2.19','&#36;2.19<br> –2.50','&#36;2.50<br> –2.86'
              ,'&#36;2.86<br> –3.31','&#36;3.31<br> –3.91','&#36;3.91<br> –4.84','&#36;4.84<br> –6.73','>&#36;6.73']
# xlabels = ['<&#36;1.59','&#36;1.59<br> –1.92','&#36;1.92<br> –2.23','&#36;2.23<br> –2.55','&#36;2.55<br> –2.91'
#               ,'&#36;2.91<br> –3.37','&#36;3.37<br> –3.98','&#36;3.98<br> –4.93','&#36;4.93<br> –6.86','>&#36;6.86']
yvals = np.zeros((ncategory, ngroup))

with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_hhs_emission_inc_perCap_relative10.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cnt = 0
    for row in reader:
        if cnt == 0:
            cats = row[2:ncategory+2]
            cnt += 1
        elif cnt > 0:
            yvals[:,cnt-1]=row[2:ncategory+2]
            cnt += 1


# yvals[0,:]=[53.8066049450591,67.5851466739485,75.7955084842472,83.3746031645289,91.2526731283751,100,110.674146162033,124.192903103187,146.763452897857,223.079105753026]
# yvals[1,:]=[26.895946280702,41.9589053905245,55.4598497311177,69.7014651357357,82.0118111265841,100,123.626066570094,156.125226800333,217.615678393869,426.462649029623]
# yvals[2,:]=[9.00277938539065,21.4791963637218,34.4746149300646,54.4186779618532,74.7816815021447,100,139.528041778838,187.945097026801,255.74814189018,352.352312839605]
# yvals[3,:]=[89.9252781902561,98.7804197012262,101.665336445787,100.604446130005,99.9650573131365,100,94.9871263587214,85.6216764749789,74.7811935077745,65.9351125783837]
# yvals[4,:]=[27.852480842543,40.4749159974339,53.679556434337,67.9264747038038,82.8669126791331,100,124.939162760074,160.799907745308,224.697191192707,510.594093717834]
# yvals[5,:]=[5.01880631264784,14.0313341668937,27.7118720421707,41.8173230842615,66.5633803457105,100,145.383321975545,217.843696603088,341.479743827633,804.254762024881]
# yvals[6,:]=[24.2029900125074,39.0349881612968,51.4093901798824,62.9217219473948,82.6843326963592,100,130.626877496749,174.763262592456,262.609911401109,675.053633137284]
# yvals[7,:]=[22.5951705481542,38.7693019551753,49.7406077394472,62.1042159707104,79.1793218774671,100,133.8919214921,190.193828891246,282.941307333864,635.530413057679]
# yvals[8,:]=[46.7646678546419,60.5098913650157,69.7815712684415,79.2523021281812,88.6906810097945,100,113.467105745811,132.012490327528,162.620073275699,258.100039162094]
# yvals[9,:]=[26.6214515145973,37.7930702085975,49.2547547881945,61.1244128751351,77.4522583051642,100,132.180209182993,186.117130683665,314.228300876388,1341.1086372124]
# yvals[10,:]=[31.0756495205203,46.5502216686801,57.5489498468329,70.7948205823053,83.8279928220739,100,126.10419824991,161.552899151497,237.071287914009,617.346794647729]
# cats=['Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods','Durable goods','Other services']

xtvals = [0,10,20,30,40,50,60,70,80,90,100]
ytvals = [300,600,900,1200,1500]

# ngroup = 5
# ncategory = 11
# xvals = ["0%","20%","40%","60%","80%","100%"]
# yvals = np.zeros((ncategory, ngroup))
#
# yvals[0,:]=[63.4718203082092,83.2247180700128,100,122.80268690535,193.370506898631]
# yvals[1,:]=[37.82973719256,68.7649008947021,100,153.694674652571,353.841145277136]
# yvals[2,:]=[17.4399479201243,50.8589130956836,100,187.353507912564,347.905904753863]
# yvals[3,:]=[94.3693803207538,101.152574859704,100,90.321210951627,70.3713318616769]
# yvals[4,:]=[37.3644055318957,66.4991907658538,100,156.250000457925,402.057372011291]
# yvals[5,:]=[11.4370870820001,41.7426856187616,100,218.059118986452,687.803006305606]
# yvals[6,:]=[34.6158657405133,62.5834694276323,100,167.161936668069,513.221697459805]
# yvals[7,:]=[34.2473681750661,62.4200121491264,100,180.864102400695,512.556184396378]
# yvals[8,:]=[56.8519368846317,78.9827647133577,100,130.093664061765,222.957210349572]
# yvals[9,:]=[36.2994177312061,62.2015453531428,100,179.362615882501,932.712124246179]
# yvals[10,:]=[42.2273076204715,69.8167799129238,100,156.476581287554,464.748283040973]
# xtvals = [0,20,40,60,80,100]
# ytvals = [200,400,600,800,1000]


colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b']  # reversed TAbleau colormap

fig = go.Figure()

for i in range(ncategory):
    fig.add_trace(go.Scatter(x=xvals, y=np.hstack((yvals[i,:],yvals[i,-1])), name=cats[i],line_shape='hv',line_color=colors[i]))

fig.update_traces(mode='lines')

cat_y_pos = yvals[:,-1]
cat_y_pos[6] += 5
cat_y_pos[7] += 5
cat_y_pos[10] -= 18

fig.update_layout(
    showlegend=False,
    legend=dict(x=0.045,y=0.96,traceorder='reversed'),
    font=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
    width=850, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=18,
    uniformtext_mode='show',
    margin=dict(l=100, r=180, t=30, b=110),

    annotations=[
        dict(
            x=0.5,y=-0.16,xref="paper",yref="paper",showarrow=False,
            text="Household expenditure level (PPP in USD/day/person)",textangle=0,align='center',
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        )
    ]+[
        dict(
            x=xpos,y=ypos,
            xref='paper',
            yref='y',
            align='left',
            textangle=0,
            text=cats[xidx],
            showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=16, color='black'),
        ) for xidx, xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                [1.074, 1.132, 1.058, 1.161, 1.193, 1.2, 1.16, 1.128, 1.228, 1.178, 1.175], cat_y_pos)
    ]+[
        dict(
            x=xpos,y=ypos,
            xref='x',
            yref='paper',
            align='center',
            textangle=0,
            text=xlabels[xidx],
            showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=14, color='black'),
        ) for xidx, xpos, ypos in zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                   ,[0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95]
                                      ,[-0.083,-0.11,-0.11,-0.11,-0.11,-0.11,-0.11,-0.11,-0.11,-0.083])
    ]
)

fig.update_xaxes(title="",ticks="outside", showline=True, linewidth=2, linecolor='black',
                 mirror="allticks", showticklabels=True, tickvals=xvals, tickformat=",%")
fig.update_yaxes(title="Relative household consumption CF per capita (50-60%=100)",range=[0,1500],ticks="outside", showline=True,
                 linewidth=2, linecolor='black', mirror="allticks",tickvals=ytvals,tickformat=",d")


fig.show()
#fig.write_image("/Users/leejmacbook/Desktop/test.png")