# 1. Library imports
import uvicorn
from fastapi import FastAPI
from ml import ml
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'DEMOPROJ': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predictPrice')
def predict_ml(data:ml):
    CRIM=data['CRIM']  
    ZN= data['ZN']
    INDUS=data['INDUS']   
    CHAS=data['CHAS']       
    NOX=data['NOX']
    RM =data['RM'] 
    AGE=data['AGE']
    DIS=data['DIS']
    RAD=data['RAD'] 
    TAX =data['TAX']  
    PTRATIO=data['PTRATIO']
    B =data['B']
    LSTAT=data['LSTSAT']
    MEDV=data['MEDV']
    
   # print(model.predict([[variance,skewness,curtosis,entropy]]))
    @app.get("/predictPrice")
    prediction = model.predictPrice([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV]])
    return {'Price': prediction[0]}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#python -m uvicorn main:app --reload