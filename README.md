# Flight Search Web Application

A web application that allows users to search for flights by entering their origin, destination, and travel dates. The application is containerized with Docker and can be deployed to Kubernetes using Helm.

## Features

- Search for flights using origin and destination airport codes
- Select departure and optional return dates
- View flight results including prices, durations, and times
- Responsive design for mobile and desktop
- Containerized with Docker
- Kubernetes deployment using Helm

## Project Structure

```
flight_search/
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   ├── index.html          # Search form
│   └── results.html        # Flight results display
├── static/                 # Static assets
│   └── styles.css          # CSS styling
├── Dockerfile              # Container definition
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
├── build-and-deploy.sh     # Deployment script
└── helm/                   # Helm chart for Kubernetes
    └── flight-search/      # Chart directory
        ├── Chart.yaml      # Chart metadata
        ├── values.yaml     # Default configuration
        └── templates/      # Kubernetes manifests
            ├── deployment.yaml  # Pod configuration
            ├── service.yaml     # Service definition
            └── ingress.yaml     # Ingress configuration
```

## Local Development Setup

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/bharats487/flight-search.git
   cd flight-search
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) Create a `.env` file in the project root with your flight search API key:
   ```
   FLIGHT_API_KEY=your_api_key_here
   ```
   Note: Without an API key, the application will use demo data.

### Running Locally

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000`
3. Enter your flight search criteria and click "Search Flights"

## Docker Containerization

### Prerequisites

- Docker

### Building the Docker Image

Build the Docker image with:

```bash
docker build -t flight-search:latest .
```

### Running the Docker Container

Run the containerized application:

```bash
docker run -p 5000:5000 flight-search:latest
```

Access the application at http://localhost:5000

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (Minikube, Docker Desktop Kubernetes, or cloud provider)
- kubectl CLI
- Helm

### Deployment Steps

1. Ensure your Kubernetes context is set to your target cluster:
   ```bash
   kubectl config current-context
   ```

2. Deploy the application using Helm:
   ```bash
   helm upgrade --install flight-search ./helm/flight-search
   ```

3. Check the deployment status:
   ```bash
   kubectl get pods,svc,ingress -l app.kubernetes.io/instance=flight-search
   ```

### Accessing the Application

#### Option 1: Port Forwarding

1. Forward a local port to the service:
   ```bash
   kubectl port-forward svc/flight-search-flight-search 8080:80
   ```

2. Access the application at http://localhost:8080

#### Option 2: Ingress

1. Add an entry to your hosts file:
   ```
   127.0.0.1 flight-search.local
   ```

2. Ensure your cluster has an Ingress controller running
3. Access the application at http://flight-search.local

## API Integration

This application can be integrated with the Skyscanner Flight Search API. To use real flight data:

1. Sign up for an API key at [RapidAPI](https://rapidapi.com/skyscanner/api/skyscanner-flight-search)
2. Add your API key to the `.env` file or as a Kubernetes secret

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Package Management**: Helm
- **HTTP Client**: Requests library
- **Environment Variables**: python-dotenv

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
