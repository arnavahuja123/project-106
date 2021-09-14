import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open (data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            sleep.append(float(row["sleep in hours"]))
            coffee.append(float(row["Coffee in ml"]))

    return {"x":sleep,"y":coffee}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(Correlation[0,1])

def setUp():
    data_path="cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
