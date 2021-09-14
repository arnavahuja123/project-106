import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks=[]
    present=[]
    with open (data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            present.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return {"x":present,"y":marks}

def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(Correlation[0,1])

def setUp():
    data_path="Student Marks vs Days Present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
