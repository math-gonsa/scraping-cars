from .parser import generate_id

import matplotlib.pyplot as plt

def pie_charts(values, label, filename=None): 
    fig, ax = plt.subplots()
    
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    
    filename = f"{generate_id()}.png" if filename == None else f"{filename}.png"
    fig.savefig(filename)
    return filename

def bar_chart(values, labels, titles, filename=None):
    fig = plt.figure() 
    
    plt.bar(labels, values) 
    
    plt.xlabel(titles[0]) 
    plt.ylabel(titles[1]) 
    plt.title(titles[2]) 
    
    filename = f"{generate_id()}.png" if filename == None else f"{filename}.png"
    fig.savefig(filename, dpi=200)
    return filename

def multiple_bar_chart(data, titles, filename=None):
    fig = plt.figure() 
    
    for values in data:
        plt.bar( values[0] + 0.00, values[1], color = 'b', width = 0.25,  edgecolor ='grey', label='Maior')
        plt.bar( values[0] + 0.25, values[2], color = 'g', width = 0.25,  edgecolor ='grey', label='Menor')
    
    plt.xlabel(titles[0]) 
    plt.ylabel(titles[1]) 
    plt.title(titles[2]) 
    
    filename = f"{generate_id()}.png" if filename == None else f"{filename}.png"
    fig.savefig(filename, dpi=200)
    return filename
