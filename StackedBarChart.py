import plotly.graph_objects as go
import numpy as np
import csv

ngroup = 5
ncategory = 11
cats = []
# xvals = ["Bottom 20%<br>(<&#36;1.92)", "Bottom 20–40%<br>(&#36;1.92–&#36;2.55)", "Middle 20%<br>(&#36;2.55–&#36;3.37)", "Top 20–40%<br>(&#36;3.37–&#36;4.93)", "Top 20%<br>(>&#36;4.93)"]
xvals = ["Bottom 20%<br>(<&#36;1.88)", "Low 20–40%<br>(&#36;1.88–&#36;2.50)", "Middle 20%<br>(&#36;2.50–&#36;3.31)", "High 20–40%<br>(&#36;3.31–&#36;4.84)", "Top 20%<br>(>&#36;4.84)"]
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
cats[0] += "                                  "

# yvals[0,:]=[0.0654753072820605,0.0514176394537289,0.00182149955361959,0.0146701171517339,0.0077159555655048,0.00160714533560029,0.00327068542710216,0.00136667071462444,0.0338324566608322,0.00426503229655612,0.00982914618374354]
# yvals[1,:]=[0.0858517049398717,0.0934642729151861,0.00531191308171664,0.015724593277477,0.0137324492063268,0.00586570356653175,0.00591320878607659,0.00249092432956122,0.0470024613152578,0.00730842576570551,0.0162510795623089]
# yvals[2,:]=[0.103156498370651,0.135918574300434,0.0104444093638474,0.0155454206670334,0.0206505508535875,0.0140520512266593,0.00944851546287996,0.0039905861017941,0.0595097696134568,0.0117495887348339,0.0232767532140231]
# yvals[3,:]=[0.126678951716633,0.208899610563466,0.0195679673239165,0.0140408121939891,0.0322664858032946,0.0306417791043783,0.0157943214341321,0.00721753773353678,0.0774184397648609,0.0210743697102338,0.0364226676640442]
# yvals[4,:]=[0.199474243798206,0.480935839949014,0.0363367168934908,0.0109395195668918,0.0830270620677894,0.096650430784567,0.0484918314433447,0.020453995858408,0.13268132221562,0.109589838678859,0.108178310909856]
# cats=['Food','Electricity','Gas','Other energy','Public transport','Private transport','Medical care','Education','Consumable goods    ','Durable goods','Other services']

# rank order
# yvals[0,:]=[0.0514176394537289,0.0654753072820605,0.0338324566608322,0.00426503229655612,0.00982914618374354,0.00160714533560029,0.0077159555655048,0.00327068542710216,0.00182149955361959,0.00136667071462444,0.0146701171517339]
# yvals[1,:]=[0.0934642729151861,0.0858517049398717,0.0470024613152578,0.00730842576570551,0.0162510795623089,0.00586570356653175,0.0137324492063268,0.00591320878607659,0.00531191308171664,0.00249092432956122,0.015724593277477]
# yvals[2,:]=[0.135918574300434,0.103156498370651,0.0595097696134568,0.0117495887348339,0.0232767532140231,0.0140520512266593,0.0206505508535875,0.00944851546287996,0.0104444093638474,0.0039905861017941,0.0155454206670334]
# yvals[3,:]=[0.208899610563466,0.126678951716633,0.0774184397648609,0.0210743697102338,0.0364226676640442,0.0306417791043783,0.0322664858032946,0.0157943214341321,0.0195679673239165,0.00721753773353678,0.0140408121939891]
# yvals[4,:]=[0.480935839949014,0.199474243798206,0.13268132221562,0.109589838678859,0.108178310909856,0.096650430784567,0.0830270620677894,0.0484918314433447,0.0363367168934908,0.020453995858408,0.0109395195668918]
# cats=['Electricity','Food','Consumable goods','Durable goods','Other services','Private transport','Public transport','Medical care','Gas','Education','Other energy']



#colors=['#9edae5','#17becf','#dbdb8d','#bcbd22','#c7c7c7','#7f7f7f','#f7b6d2','#e377c2','#c49c94','#8c564b','#c5b0d5']  # TAbleau colormap
colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#1f77b4','#aec7e8','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b']  # reversed TAbleau colormap
#colors=['#17becf','#bcbd22','#7f7f7f','#e377c2','#8c564b','#9467bd','#d62728','#2ca02c','#ff7f0e','#1f77b4','#c5b0d5']
#colors=['#ffbb78','#aec7e8','#bcbd22','#dbdb8d','#e377c2','#c7c7c7','#7f7f7f','#c5b0d5','#c49c94','#8c564b','#f7b6d2']

fig = go.Figure()
for i in range(ncategory):
    fig.add_trace(go.Bar(name=cats[i], x=xvals, y=yvals[:,i], marker_color=colors[i],marker_line_width=0.0))

# Change the bar mode
fig.update_layout(
    barmode='stack',
    showlegend=True,
    legend=dict(x=0.022,y=0.96),
    bargap=0.35,
    bargroupgap=0.0,
    font=dict(family='/Library/Fonts/SF Pro Display', size=15, color='black'),
    width=1000, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=15,
    uniformtext_mode='show',
    # margin=dict(l=100, r=50, t=50, b=50),
)
fig.update_xaxes(title="Household expenditure level (PPP in USD/day/person)",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True)
fig.update_yaxes(title="Household consumption CF per capita (tCO<sub>2</sub>/yr/capita)",range=[0,1.5],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",tickvals=[0.3,0.6,0.9,1.2,1.5])

fig.show()
#fig.write_image("/Users/leejmacbook/Desktop/test.png")