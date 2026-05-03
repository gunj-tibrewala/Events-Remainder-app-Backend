# EventHive - Backend

This is the backend repository for the EventHive application, built for academic submission. It is a RESTful API built with Flask that connects to a Supabase PostgreSQL database to store and manage event data.

## Team Members
* Gunj Tibrewala
* Sumati Sen

## Features
* **REST API**: Provides endpoints to Add, Get, and Delete events.
* **Data Validation**: The `POST /add-event` endpoint validates that required fields (title, date, time) are present before inserting into the database.
* **Supabase Integration**: Uses the official Supabase Python client to interact with the database.
* **CORS Support**: Configured to securely accept requests from the frontend client.

## Tech Stack
* Python 3
* Flask
* Supabase (PostgreSQL)

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the directory:
   ```bash
   cd Eevnts-remainder-app-Backend
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up your environment variables. Create a file named `.env` in the root folder and add your Supabase credentials:
   ```env
   SUPABASE_URL=your-supabase-url
   SUPABASE_KEY=your-supabase-api-key
   PORT=5000
   DEBUG=True
   ```

## Usage
Start the Flask server:
```bash
python app.py
```
The server will start running at `http://127.0.0.1:5000`. You can now connect the frontend application to this server.

## API Endpoints
* `POST /add-event`: Adds a new event. Expects JSON with `title`, `date`, `time`, `location`, `description`.
* `GET /get-events`: Retrieves all events from the database.
* `DELETE /delete-event/<event_id>`: Deletes a specific event by its ID.
