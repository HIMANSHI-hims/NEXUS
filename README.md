# NEXUS – Microservices-Based Application

## Overview
NEXUS is a containerized microservices-based application developed to understand and implement the fundamentals of cloud computing and modern application deployment using Docker.

The project follows a microservices architecture, where application components are developed and executed as independent services. Each service performs a specific task and communicates through APIs.

## Objectives
- Understand microservices architecture.
- Learn containerization using Docker.
- Build and run independent application services.
- Implement REST APIs for service communication.
- Explore container-based application deployment and management.

## Tech Stack
- **Backend:** Python
- **Framework:** FastAPI
- **Containerization:** Docker
- **Architecture:** Microservices
- **API Testing:** Browser / REST API requests

## Project Structure
```text
NEXUS/
│
├── services/
│   └── user-service/
│       ├── main.py
│       ├── Dockerfile
│       └── requirements.txt
│
└── README.md
```

## Current Features
- User service implementation.
- REST API for handling user-related requests.
- Health check endpoint to monitor service status.
- JSON-based API responses.
- Docker image creation and containerized execution.

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd NEXUS
```

### 2. Build the Docker Image
```bash
docker build -t nexus-user-service:latest ./services/user-service
```

### 3. Run the Container
```bash
docker run -d -p 8000:8000 --name nexus-user nexus-user-service:latest
```

### 4. Access the Application

Open the following URLs in your browser:

- Health Check: `http://localhost:8000/health`
- User API: `http://localhost:8000/users`

## Learning Outcomes
Through NEXUS, the project explores:
- Microservices-based application design.
- Docker image creation and container execution.
- RESTful API development.
- Service health monitoring.
- Fundamentals of scalable and distributed application architecture.

## Future Enhancements
- Add more independent microservices.
- Implement inter-service communication.
- Integrate a database for persistent storage.
- Use Docker Compose for managing multiple containers.
- Explore cloud deployment.

## Author
**Himanshi Srivastava**

Computer Science Engineering – Blockchain
Topics-Cloud Computing Advanced with full-stack implementation

