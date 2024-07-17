import plotly.graph_objects as go
import numpy as np
import csv

ngroup = 5
ncategory = 14
cats = []
# xvals = ["Bottom 20%<br>(<&#36;1.92)", "Bottom 20–40%<br>(&#36;1.92–&#36;2.55)", "Middle 20%<br>(&#36;2.55–&#36;3.37)", "Top 20–40%<br>(&#36;3.37–&#36;4.93)", "Top 20%<br>(>&#36;4.93)"]
xvals = ["Bottom 20%<br>(<&#36;1.88)", "Low 20–40%<br>(&#36;1.88–&#36;2.50)", "Middle 20%<br>(&#36;2.50–&#36;3.31)", "High 20–40%<br>(&#36;3.31–&#36;4.84)", "Top 20%<br>(>&#36;4.84)"]
yvals = np.zeros((ngroup,ncategory))

with open('/Users/leejmacbook/github/microData/India/data/emission/2011_IND_hhs_Food_emission_inc_perCap_exp.csv') as csvfile:
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

# yvals[0,:]=[1894.84217264716,955.324581705564,111.040803763523,541.866123404056,25.3856038099547,5.35664038863416,117.894009970718,32.7748300085257,120.190007513928,59.8185398999887,151.800771227853,309.626273982612,297.704258695208,504.619427533474]
# yvals[1,:]=[2259.72551013419,1244.34564564028,240.576072891623,1047.63618956475,47.2673245525752,8.86122582955924,211.250573585617,71.2050946781049,182.357826133939,90.595633775901,261.844625451914,459.414660349818,376.221212520074,666.105246594797]
# yvals[2,:]=[2518.00337543224,1476.16258827412,406.766225389811,1518.18016548333,58.1957424619418,12.4395055180553,293.337352010765,135.620964894447,223.527338125723,133.317725078669,377.5697628783,595.918508810994,440.831655153773,793.641215641114]
# yvals[3,:]=[2809.7062859024,1771.89169258198,672.203488001281,2172.54227115013,64.5999785382953,17.9034544333807,381.790026427353,218.409856719069,282.190031824683,194.744031696992,536.09878959332,791.421059642729,557.638847103293,942.3909715182]
# yvals[4,:]=[3421.62209057939,2381.24017278849,1530.98021105182,3499.83839573041,72.2174472187305,21.9253202423687,564.527226220324,444.690836676722,528.629832747841,384.312728341786,1020.80487033872,1302.38264729714,1632.77760711019,1240.80930070807]
#
# cats=['Grain','Vegetable','Fruit','Dairy','Beef','Pork','Poultry','Other meat','Fish','Alcohol','Other beverage              ','Confectionery','Restaurant','Other food']

# reversed color-map
#colors=['#1f77b4','#aec7e8','#ff7f0e','#ffbb78','#2ca02c','#98df8a','#d62728','#ff9896','#9467bd','#c5b0d5','#8c564b','#c49c94','#e377c2','#f7b6d2','#7f7f7f','#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']
colors=['#2ca02c','#98df8a','#ff7f0e','#ffbb78','#e377c2','#f7b6d2','#d62728','#ff9896','#1f77b4','#aec7e8','#8c564b','#c49c94','#9467bd','#c5b0d5','#7f7f7f','#c7c7c7','#bcbd22','#dbdb8d','#17becf','#9edae5']

# set y-axis units
yvals /= 1000

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
    #font=dict(family='Arial', size=15, color='black'),
    width=1000, height=800,
    paper_bgcolor='white',
    plot_bgcolor='white',
    uniformtext_minsize=15,
    uniformtext_mode='show',
)

fig.update_xaxes(title="Household expenditure level (PPP in USD/day/person)",ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks", showticklabels=True)
fig.update_yaxes(title="Household food expenditure per capita (Thousands INR/yr/capita)",range=[0,20],tickvals=[0,5,10,15,20],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks")
#fig.update_yaxes(title="Household Food-consumption expenditure per capita (Rupees/yr/capita)",range=[0,0.22],ticks="outside", showline=True, linewidth=2, linecolor='black', mirror="allticks",tickvals=[0.05,0.1,0.15,0.2],tickformat=".2f")

fig.show()
#fig.write_image("/Users/leejmacbook/Desktop/test.png")