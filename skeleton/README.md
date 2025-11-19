# Code Explainer

This project is a simple web application that explains code snippets in plain English. It uses a local Large Language Model (LLM) to generate explanations and streams them to the user in real-time.

## Tech Stack

*   **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
*   **Frontend:** [React](https://react.dev/) (with Vite)
*   **LLM:** A local model served with [Ollama](https://ollama.ai/)

## Features

*   Simple, clean user interface.
*   Real-time streaming of code explanations.
*   Easy to set up and run locally.

## Getting Started

### Prerequisites

*   [Python 3.7+](https://www.python.org/downloads/)
*   [Node.js 14+](https://nodejs.org/)
*   [Ollama](https://ollama.ai/) installed and running. You should also have a model pulled, for example, by running `ollama pull llama2`.

### Setup and Running the Application

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Backend Setup:**
    *   Navigate to the `backend` directory:
        ```bash
        cd backend
        ```
    *   Install the Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Run the backend server:
        ```bash
        uvicorn main:app --reload
        ```
    The backend will be running at `http://127.0.0.1:8000`.

3.  **Frontend Setup:**
    *   In a new terminal, navigate to the `frontend` directory:
        ```bash
        cd frontend
        ```
    *   Install the Node.js dependencies:
        ```bash
        npm install
        ```
    *   Run the frontend development server:
        ```bash
        npm run dev
        ```
    The frontend will be running at `http://localhost:5173` (or another port if 5173 is in use).

4.  **Open the application:**
    Open your web browser and go to `http://localhost:5173` to use the Code Explainer.

## Project Structure

```
.
├── backend/
│   ├── main.py         # FastAPI application
│   └── requirements.txt  # Python dependencies
└── frontend/
    ├── src/
    │   └── App.jsx     # Main React component
    ├── package.json    # Node.js dependencies
    └── index.html      # Entry point for the frontend
```
