# API Endpoints

This backend exposes endpoints for patient management, exam predictions, health checks, and model management.

## Base URL

- `http://127.0.0.1:7000/api`
- `http://localhost:7000/api`

---

## Health Check

### GET /api/health-check

Check the API server liveness and health status.

**Request:**
- Method: `GET`
- URL: `/api/health-check`
- Body: None

**Response:**
- Status: `200 OK`
- Body: JSON object with health status information

**Notes:**
- No request body required.
- Use this endpoint to verify the server is running and responsive.

---

## Patient Management

### POST /api/patient/create

Create a new patient record.

**Request:**
- Method: `POST`
- URL: `/api/patient/create`
- Content-Type: `application/json`
- Body: Patient information object

**Response:**
- Status: `201 Created`
- Body: JSON object with created patient data

### GET /api/patient/all

Retrieve all registered patients.

**Request:**
- Method: `GET`
- URL: `/api/patient/all`
- Body: None

**Response:**
- Status: `200 OK`
- Body: JSON array containing all patient records

---

## Exam Management

### POST /api/exam/predict

Generate a prediction for an exam using clinical data.

**Request:**
- Method: `POST`
- URL: `/api/exam/predict`
- Content-Type: `application/json`
- Body schema:
  - `PACIENTE`: object with patient information
    - `NOME`: string
    - `CPF`: integer
  - `DADOS`: object with exam attributes and clinical fields
  - `MODELO`: string

**Example request body:**

```json
{
  "PACIENTE": {
    "NOME": "João Silva",
    "CPF": 12345678901
  },
  "DADOS": {
    "AGRAVTABAC": "Não",
    "AGRAVDROGA": "Não",
    "AGRAVAIDS": "Ignorado",
    "AGRAVDIABE": "Ignorado",
    "HIV": "Negativo",
    "POP_RUA": "Não",
    "POP_LIBER": "Não",
    "POP_IMIG": "Não",
    "CS_SEXO": "M",
    "BACILOSC_E": "Negativo",
    "RAIOX_TORA": "Normal",
    "CS_RACA": "Parda",
    "TRATAMENTO": "Caso novo",
    "CS_ESCOL_N": "Ensino médio completo",
    "SG_UF_NOT": "SP",
    "IDADE_ANOS": 35
  },
  "MODELO": "modelo-v1"
}
```

**Response:**
- Status: `200 OK`
- Body: JSON object with prediction results

**Notes:**
- Many fields under `DADOS` accept restricted literal values, and several may also be `null` if missing.
- The request payload is validated using Pydantic schemas.

### GET /api/exam/history

Retrieve exam history for a patient.

**Request:**
- Method: `GET`
- URL: `/api/exam/history`
- Content-Type: `application/json`
- Body schema:
  - `NOME`: string
  - `CPF`: integer

**Example request body:**

```json
{
  "NOME": "João Silva",
  "CPF": 12345678901
}
```

**Response:**
- Status: `200 OK`
- Body: JSON object containing exam history for the patient

**Notes:**
- If the patient does not exist, returns `404 Not Found`.

### GET /api/exam/results

Retrieve exam results for a patient.

**Request:**
- Method: `GET`
- URL: `/api/exam/results`
- Content-Type: `application/json`
- Body schema:
  - `NOME`: string
  - `CPF`: integer

**Response:**
- Status: `200 OK`
- Body: JSON object containing exam results

---

## Model Management

### GET /api/model/list

List all available ML models.

**Request:**
- Method: `GET`
- URL: `/api/model/list`
- Body: None

**Response:**
- Status: `200 OK`
- Body: JSON array with available models

---

## Error responses

- `400 Bad Request` — invalid JSON, missing required fields, or schema validation failure
- `404 Not Found` — resource not found
- `500 Internal Server Error` — unexpected server error
