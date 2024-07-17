import plotly.graph_objects as go
import numpy as np
import csv

nrel = 9
nexp = 5
ncategory = 10
categories=[]
religions = []
yvals = np.zeros((nrel,nexp,ncategory))

with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_hhs_Energy_emission_incByRel_perCap_exp.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    cnt = 0
    relcnt = 0
    for row in reader:
        if cnt == 0:
            religions.append(row[0])
            cnt += 1
        elif cnt == 1:
            categories = row[1:ncategory+1]
            cnt += 1
        elif cnt<=nexp+1:
            yvals[relcnt,cnt-2,:]=row[1:ncategory+1]
            cnt += 1
        else:
            relcnt += 1
            cnt = 0
categories[0] += "                                  "

for i in range(len(categories)):
    if categories[i] in ["Petrol", "Diesel"]: categories[i] += " (excl. conveyance)"
    elif categories[i] in ["Biogas"]: categories[i] = "Gobar gas (biogas)"
    elif categories[i] in ["Wood"]: categories[i] = "Firewood and chips"

# set y-axis units
yvals /= 1000

expenditures = ["Bottom 20%<br>(<&#36;1.92)", "Low 20–40%<br>(&#36;1.92–&#36;2.55)", "Middle 20%<br>(&#36;2.55–&#36;3.37)", "High 20–40%<br>(&#36;3.37–&#36;4.93)", "Top 20%<br>(>&#36;4.93)"]
# expenditures = ["Bottom 20%<br>(<&#36;1.88)", "Low 20–40%<br>(&#36;1.88–&#36;2.50)", "Middle 20%<br>(&#36;2.50–&#36;3.31)", "High 20–40%<br>(&#36;3.31–&#36;4.84)", "Top 20%<br>(>&#36;4.84)"]

# colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#e377c2','#f7b6d2','#d62728','#ff9896','#1f77b4','#aec7e8','#8c564b','#c49c94','#9467bd','#c5b0d5','#7f7f7f','#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']
colors=['#1f77b4','#aec7e8','#8c564b','#c49c94','#9467bd','#c5b0d5','#ff7f0e','#ffbb78','#e377c2','#f7b6d2','#d62728','#ff9896','#2ca02c','#98df8a','#7f7f7f','#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']

fig = go.Figure()

relsel = [0, 1, 2, 3, 5]    # Hinduism, Islam, Christianity, Sikhism, Buddhism
legsel = [True, False, False, False, False]
religions = np.array(religions)
yvals = np.array(yvals)
religions = religions[relsel]
# plotting stacked-grouped-bars
cnt = 0
for i in range(nexp):
    fig.add_trace(go.Bar(xaxis='x' + str(2*cnt+1), yaxis='y' + str(2*cnt+1)))
    for j in range(ncategory):
        fig.add_trace(go.Bar(name=categories[j], x=religions, y=yvals[relsel,i,j], xaxis='x'+str(2*(cnt+1)), yaxis='y'+str(2*(cnt+1)),
                        marker_color=colors[j], marker_line_width=0.0, showlegend=legsel[i]))
    cnt += 1
fig.add_trace(go.Bar(xaxis='x'+str(2*cnt+1), yaxis='y'+str(2*cnt+1)))

fig.update_layout(
    barmode='stack',
    showlegend=True,
    legend=dict(x=0.022,y=0.96),
    bargap=0.0,
    bargroupgap=0.08,
    font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
    width=1200, height=1000,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=18,
    uniformtext_mode='show',
    margin=dict(l=100, r=100, t=100, b=100),

    xaxis=dict(domain=[0.0, 0.01], anchor='x1', showline=True, linewidth=2, linecolor='black', mirror=True, ticks="", showticklabels=False),
    xaxis2=dict(domain=[0.01, 0.19], anchor='x2', ticks="outside", showline=True, linewidth=2, linecolor='black',
                mirror="allticks", showticklabels=False, tickangle=-90,
                #title=dict(text=expenditures[0],font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')),
                ),
    xaxis3=dict(domain=[0.19, 0.21],anchor='x3',showline=True,linewidth=2,linecolor='black',mirror=True,ticks="",showticklabels=False,
                #ticklen=70, tickvals=[2.5]
                ),
    xaxis4=dict(domain=[0.21, 0.39], anchor='x4', ticks="outside", showline=True, linewidth=2,
                linecolor='black', mirror="allticks", showticklabels=False, tickangle=-90,
                #title=dict(text=expenditures[1],font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')),
                ),
    xaxis5=dict(domain=[0.39, 0.41],anchor='x5',showline=True,linewidth=2,linecolor='black',mirror=True,ticks="",showticklabels=False,
                #ticklen=70, tickvals=[2.5]
                ),
    xaxis6=dict(domain=[0.41, 0.59], anchor='x6', ticks="outside", showline=True, linewidth=2,
                linecolor='black', mirror="allticks", showticklabels=False, tickangle=-90,
                #title=dict(text=expenditures[2],font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')),
                ),
    xaxis7=dict(domain=[0.59, 0.61],anchor='x7',showline=True,linewidth=2,linecolor='black',mirror=True,ticks="",showticklabels=False,
                #ticklen=70, tickvals=[2.5]
                ),
    xaxis8=dict(domain=[0.61, 0.79], anchor='x8', ticks="outside", showline=True, linewidth=2,
                linecolor='black', mirror="allticks", showticklabels=False, tickangle=-90,
                #title=dict(text=expenditures[3],font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')),
                ),
    xaxis9=dict(domain=[0.79, 0.81],anchor='x9',showline=True,linewidth=2,linecolor='black',mirror=True,ticks="",showticklabels=False,
                #ticklen=70, tickvals=[2.5]
                ),
    xaxis10=dict(domain=[0.81, 0.99], anchor='x10', ticks="outside", showline=True, linewidth=2,
                linecolor='black', mirror="allticks", showticklabels=False, tickangle=-90,
                #title=dict(text=expenditures[4],font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black')),
                ),
    xaxis11=dict(domain=[0.99, 1.00], anchor='x1', showline=True, linewidth=2, linecolor='black', mirror=True, ticks="", showticklabels=False),

    yaxis=dict(anchor='y1', title="<br>Household energy expenditure per capita (Thousands INR/yr/capita)", range=[0, 4.5],
               ticks="outside", showline=True,
               linewidth=2, linecolor='black', mirror=False, tickvals=[1, 2, 3, 4],
               titlefont=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
               ),
    yaxis2=dict(anchor='y2', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis3=dict(anchor='y3', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis4=dict(anchor='y4', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis5=dict(anchor='y5', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis6=dict(anchor='y6', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis7=dict(anchor='y7', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis8=dict(anchor='y8', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis9=dict(anchor='y9', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis10=dict(anchor='y10', range=[0, 4.5], showline=False, showticklabels=False),
    yaxis11=dict(anchor='x11', range=[0, 4.5], showline=True, showticklabels=False,
                 linewidth=2, linecolor='black', tickvals=[1, 2, 3, 4], ticks="outside", side="right"),

    annotations=[
        dict(
            x=0.5,y=-0.12,xref="paper",yref="paper",showarrow=False,
            text="Household expenditure level by religion (PPP in USD/day/person)",textangle=0,align='center',
            font=dict(family='/Library/Fonts/SF Pro Display', size=20, color='black'),
        )
    ]+[
        dict(
            x=xpos,
            y=ypos,
            xref='x2',
            yref='y2',
            align='left',
            textangle=270,
            text=religions[xpos],
            showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        ) for xpos, ypos in zip([0, 1, 2, 3, 4],[1.18, 1.18, 1.175, 1.45, 1.35])
    ]+[
        dict(
            x=2,y=-0.075,
            xref='x'+str((i+1)*2),
            yref='paper',
            align='center',
            textangle=0,
            text=expenditures[i],
            showarrow=False,
            font=dict(family='/Library/Fonts/SF Pro Display', size=18, color='black'),
        ) for i in range(nexp)
    ]

)

fig.show()