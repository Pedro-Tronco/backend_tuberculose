# Projeto Tuberculose

## Backend API

This repository contains a Flask-based backend for recording and retrieving patient exam data related to tuberculosis.

### Run the backend server

1. Clone the repository and navigate to the backend directory:
   ```powershell
   git clone https://github.com/Pedro-Tronco/backend_tuberculose
   cd projeto_tuberculose/backend
   ```

2. (Optional) Set up a Python virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

4. Start the server:
   ```powershell
   python run.py
   ```

5. The backend will be available at:
   
   `http://127.0.0.1:7000`
   
   AKA
   
   `http://localhost:7000`
   


### Available endpoints

**Health Check:**
- `GET /api/health-check` — verify server liveness

**Patient Management:**
- `POST /api/patient/create` — create a new patient
- `GET /api/patient/all` — list all patients

**Exam Management:**
- `POST /api/exam/predict` — generate prediction for exam data
- `GET /api/exam/history` — retrieve exam history for a patient
- `GET /api/exam/results` — retrieve exam results for a patient

**Model Management:**
- `GET /api/model/list` — list available ML models

### API contract

See [`ENDPOINTS.md`](./ENDPOINTS.md) for full endpoint details, example requests, response structure, and error behavior.
