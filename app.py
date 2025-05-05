import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variables
API_KEY = os.getenv('FLIGHT_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get search parameters from form
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    departure_date = request.form.get('departure_date')
    return_date = request.form.get('return_date')
    
    # Validate input
    if not all([origin, destination, departure_date]):
        return render_template('index.html', error="Please fill all required fields")
    
    # Search for flights
    flights = search_flights(origin, destination, departure_date, return_date)
    
    return render_template('results.html', 
                          flights=flights, 
                          origin=origin, 
                          destination=destination,
                          departure_date=departure_date,
                          return_date=return_date)

def search_flights(origin, destination, departure_date, return_date=None):
    """
    Search for flights using an external API
    
    For this example, we'll use the Skyscanner Flight Search API.
    You'll need to sign up for an API key at RapidAPI:
    https://rapidapi.com/skyscanner/api/skyscanner-flight-search
    
    Store your API key in a .env file as FLIGHT_API_KEY=your_api_key_here
    """
    # Check if API key is available
    if not API_KEY:
        # For demo purposes, return dummy data if no API key is provided
        return get_dummy_flight_data(origin, destination, departure_date, return_date)
    
    # Real API implementation
    try:
        # RapidAPI Skyscanner endpoint
        url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/{}/{}/{}".format(
            origin, destination, departure_date
        )
        
        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API error: {response.status_code}")
            # Fall back to dummy data if API call fails
            return get_dummy_flight_data(origin, destination, departure_date, return_date)
            
    except Exception as e:
        print(f"Error fetching flights: {e}")
        # Fall back to dummy data if API call fails
        return get_dummy_flight_data(origin, destination, departure_date, return_date)

def get_dummy_flight_data(origin, destination, departure_date, return_date=None):
    """Generate dummy flight data for demonstration purposes"""
    return {
        "flights": [
            {
                "airline": "Demo Airlines",
                "flight_number": "DA101",
                "departure": {
                    "airport": origin,
                    "time": "08:00",
                    "date": departure_date
                },
                "arrival": {
                    "airport": destination,
                    "time": "10:30",
                    "date": departure_date
                },
                "price": 299.99,
                "duration": "2h 30m",
                "stops": 0
            },
            {
                "airline": "Mock Air",
                "flight_number": "MA202",
                "departure": {
                    "airport": origin,
                    "time": "12:45",
                    "date": departure_date
                },
                "arrival": {
                    "airport": destination,
                    "time": "16:20",
                    "date": departure_date
                },
                "price": 249.50,
                "duration": "3h 35m",
                "stops": 1
            },
            {
                "airline": "Example Airways",
                "flight_number": "EA505",
                "departure": {
                    "airport": origin,
                    "time": "17:30",
                    "date": departure_date
                },
                "arrival": {
                    "airport": destination,
                    "time": "19:45",
                    "date": departure_date
                },
                "price": 350.00,
                "duration": "2h 15m",
                "stops": 0
            }
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
