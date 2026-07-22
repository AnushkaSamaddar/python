import pandas as pd
df=pd.read_csv(r'C:\Users\ANUSHKA\Downloads\sensor_data.csv',header=None,names=["x","y","z","val"])
print(df.describe())
print(df.shape)
print(df.isnull().sum())
print(df.plot())
print(df.hist())
print(df.boxplot())