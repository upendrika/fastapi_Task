from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uvicorn
import pickle

app = FastAPI(debug=True)


with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data['model']
    le_country = data['le_country']
    le_education = data['le_education']


class SalaryPredictionRequest(BaseModel):
    country: str
    education_level: str
    years_of_experience: int

@app.get('/')
def home():
    return {'text': 'Software Developer Salary Prediction!'}

@app.get('/calculate_salary')
def predict_get(country: str, education_level: str, years_of_experience: int):
   
    country_encoded = le_country.transform([country])[0]
    education_encoded = le_education.transform([education_level])[0]
    input_data = [[country_encoded, education_encoded, years_of_experience]]
    
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return {'The estimated salary is {}'.format(output)}

@app.post('/predict_salary')
def predict_post(request: SalaryPredictionRequest):

    country_encoded = le_country.transform([request.country])[0]
    education_encoded = le_education.transform([request.education_level])[0]
    
    input_data = [[country_encoded, education_encoded, request.years_of_experience]]
    
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return {'The estimated salary is {}'.format(output)}


if __name__ == '__main__':
    uvicorn.run("mlfastapi:app", host="0.0.0.0", port=8000, reload=True)
