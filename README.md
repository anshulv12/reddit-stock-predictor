# Reddit Penny Stock Tracker

This project consists of:

- `backend/` → Flask API for Reddit sentiment analysis and stock forecasting.
- `frontend/` → React Vite frontend for displaying stock sentiment data.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Node.js (v16+) & npm**
- **Git**

## Backend Setup (Flask)

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # For Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install flask flask-cors requests
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. The API will now be running on `http://127.0.0.1:5000/api/health`.

## Frontend Setup (React Vite)

1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Open `http://localhost:5173` in your browser.

## API Endpoints

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| GET    | `/api/health` | Check if the backend is running |

## Project Structure

```
reddit-stock-predictor/
│── backend/              # Flask API server
│   ├── venv/            # Virtual environment
│   ├── app.py           # Main Flask application
│   ├── requirements.txt # (Optional) For dependencies
│── frontend/             # React Vite frontend
│   ├── src/
│   ├── package.json
│   ├── index.html
│── README.md             # Documentation
```
