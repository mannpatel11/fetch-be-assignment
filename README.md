# fetch-be-assignment

This is the points system for the Fetch backend engineer intern assignment

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone this repository or download the source code.

2. Open a terminal/command prompt and navigate to the project directory.

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On UNIX systems:
     ```
     source venv/bin/activate
     ```

5. Install the required package:
   ```
   pip install Flask
   ```

## Running the Application

1. In the project directory, run the following command:
   ```
   python app.py
   ```

2. The server will start, and you should see output similar to this:
   ```
   * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
   ```

3. The application is now running and listening on port 8000.

## API Endpoints

### 1. Add Points

- **URL:** `/add`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "payer": "[payer name]",
    "points": [number of points],
    "timestamp": "[ISO 8601 format]"
  }
  ```
- **Success Response:** Code 200

### 2. Spend Points

- **URL:** `/spend`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "points": [number of points to spend]
  }
  ```
- **Success Response:** 
  - Code 200
  - Content: JSON array of points spent per payer

### 3. Check Balance

- **URL:** `/balance`
- **Method:** GET
- **Success Response:** 
  - Code 200
  - Content: JSON object with payer balances

## Testing the Application

You can use tools like cURL, Postman, or any HTTP client to test the API endpoints. Here are some example cURL commands:

1. Add points:
   ```
   curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}'
    curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"}'
    curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"}'
    curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z"}'
    curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"}'

   ```

2. Spend points:
   ```
   curl -X POST http://localhost:8000/spend -H "Content-Type: application/json" -d '{"points": 5000}'
   ```

3. Check balance:
   ```
   curl http://localhost:8000/balance
   ```

## Error Handling

The application includes basic error handling:

- If there are not enough points to spend, it will return a 400 error.
- Invalid JSON in requests will result in a 400 error.

For production use, you may want to add more comprehensive error handling and logging.

## Notes

- This application uses in-memory storage and will reset when the server is restarted. For a production environment, consider using a persistent database.