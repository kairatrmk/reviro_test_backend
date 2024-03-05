## Test assignment for Backend developer

### Overview

You are provided with a [BRD for Reviro Internship TechStart - Spring 2024](https://docs.google.com/document/u/0/d/1vb_hHeQ4kBvzXeq4mOyko4oYZkhplLKHhy7YlUq64Lc/edit). Your task is creating a simple product inventory management system. The system should allow users to add, update, delete, and list establishments and products in the inventory. Each product will have the following attributes:

- Product ID (unique identifier)
- Name
- Description
- Price
- Quantity in stock

Each establishment will have the following attributes:

- Establishment ID (unique identifier)
- Name
- Description
- Locations
- Opening hours

### Requirements

- API Development
  - Develop a RESTful API using Django, Flask or FastAPI that exposes endpoints for CRUD (Create, Read, Update, Delete) operations on establishments and products.
  - Ensure the API supports pagination for listing establishments and products.
- Docker Compose
  - Containerize your application using Docker. Ensure your application and the PostgreSQL database are defined in a docker-compose.yml file for easy setup and teardown.
- Swagger Documentation
  - Integrate Swagger using libraries like flasgger for Flask or fastapi's built-in support for Swagger. Document all your API endpoints, including parameters, request bodies, and response schemas.
- Write a comprehensive README file that includes:
  - An overview of the project
  - Instructions on how to build and run your application using Docker Compose
  - A brief guide on how to use the API (with examples of requests and responses)
- Suite of Unit Tests
  - Write unit tests for your API endpoints. Cover positive scenarios and error handling.
  - Use a Python testing framework such as pytest and ensure your tests can be easily run in the Docker environment.
- PostgreSQL Integration
  - Use PostgreSQL as the database for storing establishments information.
  - Define your database schema and ensure your application properly handles connections to PostgreSQL.

### Deliverables

- Source code pushed to a Git repository (e.g., GitHub, GitLab).
- Dockerfile and docker-compose.yml for containerization.
- Swagger documentation accessible through a URL.
- A README file with setup and usage instructions.
- A suite of unit tests.

### Evaluation Criteria

- Functionality: The application works as described and meets all the functional requirements.
- Code Quality: The code is clean, well-organized, and follows best practices.
- Error Handling: The application gracefully handles and reports errors.
- Documentation: The API is well-documented, and the README provides clear setup and usage instructions.
- Testing: The application includes a comprehensive suite of unit tests.

### Submission Instructions

- Provide a link to the Git repository containing your project. Ensure the repository is public or share access with [internship@reviro.io](mailto:internship@reviro.io).
- Include any additional notes or comments in your submission.
- Submission form can be found [here](https://forms.gle/nTqTo7wuVFerpknB6).

--- 

## Setup Instructions

### Prerequisites

Make sure you have Docker and Docker Compose installed on your system.

```bash
git clone <repository-url>
cd <repository-folder>
```

Create a `.env` file based on the `env.example` sample file in the root directory and define the following environment variables:


Start the application using Docker Compose:
```bash
docker-compose up --build
```

### Viewing API Documentation
Swagger Documentation
The API endpoints are documented using Swagger. You can access the Swagger documentation by visiting the following URL:

```bash
http://localhost:8000/api/schema/swagger/ # Swagger
http://localhost:8000/api/schema/redoc/  # Redoc
```
