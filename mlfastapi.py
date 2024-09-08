from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uvicorn
import pickle

app = FastAPI(debug=True)

# Load the model and label encoders when the app starts
with open('C:/Users/ASUS/Documents/IS_Project/assign2/saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data['model']
    le_country = data['le_country']
    le_education = data['le_education']

# Define a Pydantic model for the POST request body
class SalaryPredictionRequest(BaseModel):
    country: str
    education_level: str
    years_of_experience: int

@app.get('/')
def home():
    return {'text': 'Software Developer Salary Prediction'}

@app.get('/calculate_salary')
def predict_get(country: str, education_level: str, years_of_experience: int):
    # Transform the input using the label encoders
    country_encoded = le_country.transform([country])[0]
    education_encoded = le_education.transform([education_level])[0]
    
    # Prepare the input for prediction
    input_data = [[country_encoded, education_encoded, years_of_experience]]
    
    # Make prediction
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return {'The estimated salary is {}'.format(output)}

@app.post('/predict_salary')
def predict_post(request: SalaryPredictionRequest):
    # Transform the input using the label encoders
    country_encoded = le_country.transform([request.country])[0]
    education_encoded = le_education.transform([request.education_level])[0]
    
    # Prepare the input for prediction
    input_data = [[country_encoded, education_encoded, request.years_of_experience]]
    
    # Make prediction
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return {'The estimated salary is {}'.format(output)}


@app.put('/update_salary')
def update_salary(request: SalaryPredictionRequest):
    # Example: Simulate a check if this specific combination of country, education level, 
    # and years of experience exists (for the sake of updating it).
    country_encoded = le_country.transform([request.country])[0]
    education_encoded = le_education.transform([request.education_level])[0]

    # If a match or specific condition is required before updating, it can be checked here.
    # For now, it directly moves to updating (similar to the POST operation).
    
    input_data = [[country_encoded, education_encoded, request.years_of_experience]]
    
    # Make prediction (this is essentially the update operation)
    prediction = model.predict(input_data)
    output = round(prediction[0], 2)

    return {'The updated estimated salary is {}'.format(output)}


@app.delete('/delete_salary')
def delete_salary(country: str, education_level: str, years_of_experience: int):
    # Example logic for deletion, this could be adjusted depending on your needs
    # Transform the input using the label encoders
    country_encoded = le_country.transform([country])[0]
    education_encoded = le_education.transform([education_level])[0]

    # Check if the combination exists and simulate deletion
    # Since this is a model prediction app, we'll simulate the deletion process
    # Example: if country, education, and experience match certain conditions, delete it
    
    if country_encoded == 1 and education_encoded == 2 and years_of_experience == 5:
        return {'message': 'Entry deleted successfully.'}
    else:
        raise HTTPException(status_code=404, detail="Entry not found for deletion.")



if __name__ == '__main__':
    uvicorn.run("mlfastapi:app", host="127.0.0.1", port=8000, reload=True)
