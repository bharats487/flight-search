# Flight Search Web Application

A web application that allows users to search for flights by entering their origin, destination, and travel dates.

## Features

- Search for flights using origin and destination airport codes
- Select departure and optional return dates
- View flight results including prices, durations, and times
- Responsive design for mobile and desktop

## Installation

1. Clone the repository
2. Install the required packages:

```
pip install -r requirements.txt
```

3. (Optional) Create a `.env` file in the project root with your flight search API key:

```
FLIGHT_API_KEY=your_api_key_here
```

Note: Without an API key, the application will use demo data.

## Usage

1. Run the Flask application:

```
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`
3. Enter your flight search criteria and click "Search Flights"

## API Integration

This application can be integrated with the Skyscanner Flight Search API. To use real flight data:

1. Sign up for an API key at [RapidAPI](https://rapidapi.com/skyscanner/api/skyscanner-flight-search)
2. Add your API key to the `.env` file

## Technologies Used

- Flask - Python web framework
- HTML/CSS - Frontend
- Requests - HTTP library for API calls
