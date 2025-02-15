# Natural Language to SQL Query Converter

## Description
This project is a full-stack application that converts natural language questions into SQL queries using Google's Gemini AI. It features a Flask backend API that processes queries through the Gemini model and a React frontend that displays the results in a sortable, searchable table.

## Features
- Natural language to SQL query conversion using Google's Gemini-Pro model
- RESTful API built with Flask
- Interactive React frontend with:
  - Sortable columns
  - Real-time search functionality
  - Responsive table design
  - Error handling and loading states
- SQLite database integration
- CORS support for cross-origin requests
- Environment variable configuration

## Tech Stack
- **Backend:**
  - Flask (Python web framework)
  - Google Generative AI (Gemini-Pro model)
  - SQLite3
  - python-dotenv
- **Frontend:**
  - React
  - Lucide React (for icons)
  - Tailwind CSS (for styling)

## Prerequisites
- Python 3.7 or higher
- Node.js and npm
- Google API key for Gemini

## Installation

### Backend Setup
1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies
```bash
pip install flask python-dotenv google-generativeai sqlite3 flask-cors
```

4. Create a `.env` file in the root directory with:
```
GOOGLE_API_KEY=your_gemini_api_key
PORT=5000
```

### Frontend Setup
1. Navigate to the frontend directory
```bash
cd frontend
```

2. Install dependencies
```bash
npm install
```

## Database Schema
The application expects a SQLite database with a PATIENT table containing:
```sql
CREATE TABLE PATIENT (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    condition TEXT,
    admitted_date DATE,
    lab_results_pending BOOLEAN,
    emergency_visit_today BOOLEAN
);
```

## Usage

### Starting the Backend
```bash
python app.py
```
The server will start on http://localhost:5000

### Starting the Frontend
```bash
cd frontend
npm start
```
The application will be available at http://localhost:3000

## API Endpoints

### Convert Natural Language to SQL Query
- **URL:** `/post/query`
- **Method:** `POST`
- **Body:**
```json
{
    "question": "Show me all patients over 30 years old"
}
```
- **Success Response:**
```json
{
    "query": "SELECT id, name, age, gender, condition FROM PATIENT WHERE age > 30",
    "results": [...]
}
```

## Error Handling
The application includes comprehensive error handling for:
- Invalid API requests
- Database connection issues
- Query execution errors
- Missing or invalid input data

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
