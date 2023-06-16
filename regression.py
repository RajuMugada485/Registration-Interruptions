import joblib
import pandas as pd
import numpy as np 
import pickle

# Train the model

#importing dataset using pandas
df=pd.read_csv(r"C:\Users\mugada raju\Downloads\hackathon (1).csv")
#categorization of indepedent and dependent varibles
IndepVar = []
for col in df.columns:
    if col != 'PS_RATE' and col!='ABILITY':
        IndepVar.append(col)

TargetVar = 'PS_RATE'

x = df[IndepVar]
y = df[TargetVar]


from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100)
model.fit(x, y)
filename= 'saved_model.sav'
saved_model=joblib.dump(model,filename)