# API Endpoints

This backend exposes endpoints for health checks and patient exam management.

## Base URL

- `http://127.0.0.1:7000/api`

## GET /api/health-check

Check the API server liveness and health status.

### Request

- Method: `GET`
- URL: `/api/health-check`

### Response

- Status: `200 OK`
- Body: JSON object with health status information

### Notes

- No request body required.
- Use this endpoint to verify the server is running and responsive.

## GET /api/exam/predict

Save a new exam record for a patient (prediction endpoint).

### Request

- Method: `GET`
- URL: `/api/exam/predict`
- Content-Type: `application/json`
- Body schema:
  - `PACIENTE`: object with patient information
    - `NOME`: string
    - `CPF`: integer
  - `DADOS`: object with exam attributes and clinical fields

### Example request body

```json
{
  "PACIENTE": {
    "NOME": "João Silva",
    "CPF": 12345678901,
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
    "CS_SEXO": "Masculino",
    "BACILOSC_E": "Negativo",
    "CULTURA_ES": "Não realizada",
    "RAIOX_TORA": "Normal",
    "CS_RACA": "Parda",
    "TRATAMENTO": "Caso novo",
    "CULTURA_OU": "Não realizada",
    "HISTOPATOL": "Não realizado",
    "TRATSUP_AT": "Não",
    "CS_ESCOL_N": "Ensino médio completo",
    "SG_UF_NOT": "SP",
    "IDADE_ANOS": 35
  }
}
```

### Response

- Status: `200 OK`
- Body: JSON object containing the stored exam data keyed by the patient tuple.

### Notes

- The request payload is validated using the current schema definitions.
- All fields under `DADOS` are required and must match one of the accepted literal values.

## GET /api/exam/history

Retrieve exam data for an existing patient.

### Request

- Method: `GET`
- URL: `/api/exam/history`
- Content-Type: `application/json`
- Body schema:
  - `NOME`: string
  - `CPF`: integer

### Example request body

```json
{
  "NOME": "João Silva",
  "CPF": 12345678901
}
```

### Response

- Status: `200 OK`
- Body:
  - `DADOS`: object with exam attributes stored for the patient

### Example response body

```json
{
  "DADOS": {
    "AGRAVTABAC": "Não",
    "AGRAVDROGA": "Não",
    "AGRAVAIDS": "Ignorado",
    "AGRAVDIABE": "Ignorado",
    "HIV": "Negativo",
    "POP_RUA": "Não",
    "POP_LIBER": "Não",
    "POP_IMIG": "Não",
    "CS_SEXO": "Masculino",
    "BACILOSC_E": "Negativo",
    "CULTURA_ES": "Não realizada",
    "RAIOX_TORA": "Normal",
    "CS_RACA": "Parda",
    "TRATAMENTO": "Caso novo",
    "CULTURA_OU": "Não realizada",
    "HISTOPATOL": "Não realizado",
    "TRATSUP_AT": "Não",
    "CS_ESCOL_N": "Ensino médio completo",
    "SG_UF_NOT": "SP",
    "IDADE_ANOS": 35
  }
}
```

### Notes

- This endpoint currently expects the patient identifiers in the JSON request body, not as query parameters.
- If the stored patient does not exist, the API returns a `404 Not Found` error.

## Error responses

- `400 Bad Request` — invalid JSON, missing required fields, or schema validation failure
- `404 Not Found` — patient record does not exist
- `500 Internal Server Error` — unexpected server error or storage issue

## Storage behavior

- The backend uses a simple in-memory dictionary to store exam results.
- Data is not persisted across server restarts.
- This is intended as a demo implementation for the current backend.
