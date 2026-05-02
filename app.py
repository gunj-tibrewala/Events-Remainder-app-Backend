from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Allow requests from local development and the deployed GitHub Pages frontend
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500", "https://gunj-tibrewala.github.io"]}})

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

supabase: Client = None
if url and key and url != "your-supabase-url-here":
    supabase = create_client(url, key)

@app.route('/add-event', methods=['POST'])
def add_event():
    data = request.json
    
    # Validation: Check if required fields exist and are not empty
    if not data or not data.get('title') or not data.get('date') or not data.get('time'):
        return jsonify({"error": "Invalid data: title, date, and time are required."}), 400

    if not supabase:
        return jsonify({"error": "Supabase credentials not configured."}), 500

    try:
        # Supabase will automatically generate the 'id' if the table is set up properly
        if 'id' in data:
            del data['id'] 
        response = supabase.table('events').insert(data).execute()
        return jsonify({"message": "Event added successfully", "event": response.data[0]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-events', methods=['GET'])
def get_events():
    if not supabase:
        return jsonify([])

    try:
        response = supabase.table('events').select('*').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete-event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    if not supabase:
        return jsonify({"error": "Supabase credentials not configured."}), 500

    try:
        response = supabase.table('events').delete().eq('id', event_id).execute()
        return jsonify({"message": "Event deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Get configuration from .env
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, port=port)