import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from OneM2M import *
import numpy as np
import time

XTemp = deque([])
XTemp.append(1)
YTemp = deque([])
YTemp.append(1)
XHum = deque([])
XHum.append(1)
YHum = deque([])
YHum.append(1)
Xem1E = deque([])
Xem1E.append(1)
Yem1E = deque([])
Yem1E.append(1)
Xem2E = deque([])
Xem2E.append(1)
Yem2E = deque([])
Yem2E.append(1)
Xem1P = deque([])
Xem1P.append(1)
Yem1P = deque([])
Yem1P.append(1)
Xem2P = deque([])
Xem2P.append(1)
Yem2P = deque([])
Yem2P.append(1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [   html.H1('Temperature - Time Graph'),
        html.P('Y-Axis = Temp(Celsius), X-Axis = Time'),
        dcc.Graph(id='live-graph1', animate=False),
        html.H1('Humidity - Time Graph'),
        html.P('Y-Axis = Humidity(%), X-Axis = Time'),
        dcc.Graph(id='live-graph2', animate=False),
        html.H1('EnergyMeter1 - Time Graph'),
        html.P('Y-Axis = EnergyMeter1 (Energy), X-Axis = Time'),
        dcc.Graph(id='live-graph3', animate=False),
        html.H1('EnergyMeter2 - Time Graph'),
        html.P('Y-Axis = EnergyMeter2 (Energy), X-Axis = Time'),
        dcc.Graph(id='live-graph4', animate=False),
        html.H1('EnergyMeter1 - Time Graph'),
        html.P('Y-Axis = EnergyMeter1 (Power), X-Axis = Time'),
        dcc.Graph(id='live-graph5', animate=False),
        html.H1('EnergyMeter2 - Time Graph'),
        html.P('Y-Axis = EnergyMeter2 (Power), X-Axis = Time'),
        dcc.Graph(id='live-graph6', animate=False),
        dcc.Interval(
            id='graph-update1',
            interval=1*1000
        ),

    ]
)

@app.callback(Output('live-graph1', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    temp,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    #time=(temp.split(";")[1])
    print (time);
    temp=temp[temp.find("(")+1:temp.find(")")]
    tempcel=(temp.split(",")[0])
    XTemp.append(XTemp[-1]+1)
    YTemp.append(tempcel)

    data = plotly.graph_objs.Scatter(
            x=list(XTemp),
            y=list(YTemp),
            name='Scatter',
            mode= 'lines+markers'
            )   

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(XTemp),max(XTemp)]),
                                                height=300)}

@app.callback(Output('live-graph2', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    hum,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    #time=(hum.split(";")[1])
    hum=hum[hum.find("(")+1:hum.find(")")]
    humidity=(hum.split(",")[1])
    XHum.append(time)
    YHum.append(humidity)

    data = plotly.graph_objs.Scatter(
            x=list(XHum),
            y=list(YHum),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(XHum),max(XHum)]),
                                                height=300)}

@app.callback(Output('live-graph3', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    em1,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    #time=(em1.split(";")[1])
    em1=em1[em1.find("(")+1:em1.find(")")]
    em1=em1.split(",")[2]
    Xem1E.append(time)
    Yem1E.append(em1)

    data = plotly.graph_objs.Scatter(
            x=list(Xem1E),
            y=list(Yem1E),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(Xem1E),max(Xem1E)]),
                                                height=300)}

@app.callback(Output('live-graph4', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    em2,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    em2=em2[em2.find("(")+1:em2.find(")")]
    em2=em2.split(",")[3]
    Xem2E.append(time)
    Yem2E.append(em2)

    data = plotly.graph_objs.Scatter(
            x=list(Xem2E),
            y=list(Yem2E),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(Xem2E),max(Xem2E)]),
                                                height=300)}

@app.callback(Output('live-graph5', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    em1p,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    #time=(em1p.split(";")[1])
    time = time[:3]+'-'+time[4:5]+"-"+time[6:7]+' '+time[9:10]+':'+time[11:12]+':'+time[13:14]
    print(time)
    em1p=em1p[em1p.find("(")+1:em1p.find(")")]
    em1p=em1p.split(",")[4]
    Xem1P.append(time)
    Yem1P.append(em1p)

    data = plotly.graph_objs.Scatter(
            x=list(Xem1P),
            y=list(Yem1P),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(Xem1P),max(Xem1P)]),
                                                height=300)}

@app.callback(Output('live-graph6', 'figure'),
              [Input('graph-update1', 'n_intervals')])
def update_graph_scatter(input_data):
    em2p,time=get_data("http://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la")
    #time=(em2p.split(";")[1])
    em2p=em2p[em2p.find("(")+1:em2p.find(")")]
    em2p=em2p.split(",")[3]
    Xem2P.append(time)
    Yem2P.append(em2p)

    data = plotly.graph_objs.Scatter(
            x=list(Xem2P),
            y=list(Yem2P),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(Xem2P),max(Xem2P)]),
                                                height=300)}


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080 ,debug=False)