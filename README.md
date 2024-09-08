# Software Developer Salary Prediction API

This FastAPI application provides an API for predicting software developer salaries based on country, education level, and years of experience. The model used for predictions is a pre-trained machine learning model that has been serialized and loaded into the application.

## Features

- **GET `/calculate_salary`**: Predict salary using query parameters.
- **POST `/predict_salary`**: Predict salary using JSON payload.
- **PUT `/update_salary`**: Update and predict salary based on user input.
- **DELETE `/delete_salary`**: Simulate the deletion of salary prediction data.

## Getting Started

### Prerequisites

- Python 3.8 or later
- `pip`

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/upendrika/fastapi_Task.git
   ```

2. **Create a virtual environment and activate it:**


```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install the required dependencies:**
```
pip install -r requirements.txt
```

4. **Ensure you have the model file ```saved_steps.pkl``` in the root directory.**

## Running the Application
To start the FastAPI application locally, use the following command:

```
uvicorn main:app –reload
```
Visit http://127.0.0.1:8000 in your browser or use an API testing tool like Postman to interact with the API.
