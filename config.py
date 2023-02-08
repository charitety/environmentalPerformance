import pandas as pd

data = pd.read_csv("/Users/croblescarvajal_ifds/Desktop/Exercises/phase2Excercises /HDI.csv") 

for columnHeaders in data.columns: 
    print(columnHeaders)

epiForEngine = 'postgresql+psycopg2://postgres:password@localhost:5432/epi'