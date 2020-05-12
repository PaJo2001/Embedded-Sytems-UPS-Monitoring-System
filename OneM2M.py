
import requests
import json
import time
import matplotlib.pyplot as plt_temp
import matplotlib.pyplot as plt_hum
import numpy as np


def get_data(uri, format="json"):
    """
        Method description:
        Gets data from the specified container(data_CIN)
        in the OneM2M framework/tree

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json'}

    response = requests.get(uri, headers=headers)
    #print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return _resp["m2m:cin"]["con"],_resp["m2m:cin"]["ct"] 

# ====================================================
# ====================================================

# use ggplot style for more sophisticated visuals
plt_temp.style.use('ggplot')
plt_hum.style.use('ggplot')

def live_plotter_temp(x_vec,y1_data,line1,identifier1='a'):
    figtemp = plt_temp.figure(figsize=(4,4))
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt_temp.ion()
        # figtemp = plt_temp.figure(figsize=(4,4))
        ax1 = figtemp.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax1.plot(x_vec,y1_data,'-o',alpha=1)        
        #update plot label/title
        plt_temp.ylabel('Y Label')
        plt_temp.title('Temp - Time Graph: {}'.format(identifier1))
        plt_temp.show()
        plt_temp.savefig("temp_graph.png")
        # plt_temp.close()
        # plt_temp.savefig("temp_graph.png",dpi=figtemp.dpi)
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    # if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
    #     plt_temp.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    # figtemp = plt_temp.figure(figsize=(4,4))    
    plt_temp.savefig("temp_graph.png")
    plt_temp.pause(0.00000001)
    plt_temp.close(figtemp)
    
    # return line so we can update it again in the next iteration
    return line1

def live_plotter_hum(x_vec,y1_data,line1,identifier2='b'):
    
    fighum = plt_hum.figure(figsize=(4,4))
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt_hum.ion()
        # fighum = plt_hum.figure(figsize=(4,4))
        ax = fighum.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=1)        
        #update plot label/title
        plt_hum.ylabel('Y Label')
        plt_hum.title('Humidity - Time Graph: {}'.format(identifier2))
        plt_hum.show()
        # plt_hum.close()
        plt_hum.savefig("hum_graph.png")
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    # if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
    #     plt_hum.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    # fighum = plt_hum.figure(figsize=(4,4))    
    plt_hum.savefig("hum_graph.png")
    plt_hum.pause(0.00000001)
    plt_hum.close(fighum)
    
    # return line so we can update it again in the next iteration
    return line1

if __name__ == "__main__":
    server = "http://139.59.42.21:8080"
    cse = "/~/in-cse/in-name/"