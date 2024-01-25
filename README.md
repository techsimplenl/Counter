COUNTER API SERVICE WITH DOCKER
__________________________________

This readme file provides instructions on how to use the api that is containerized using Docker. 
This containerized application allows you to easily deploy and run the counter application in a consistent and isolated environment.

PREREQUISITES
______________

Before you begin, ensure that you have the following software installed on your machine:
. Docker
. Git

GETTING STARTED
______________________

1. Clone the repository to your local machine: git clone https://github.com/techsimplenl/Counter.git
2. Navigate to the project directory: cd /path/to/Counter
3. Build the Docker image: docker build -t name_of_docker_from_your_choice:version .
4. Running the Application in Docker: docker run -d -p 8000:8000 --name containername name_of_docker_from_your_choice:version
5. Navigate to http://localhost:8000/counter and include the initial value in the request in JSON format
6. Don't forget to include the Content-Type header in your requests and set it to application/json, as the server exclusively accepts data in JSON format

## HINTS ##
___________

The application is developed using the Flask framework, which is exceptionally well-suited for building simple and compact web applications due to its lightweight and modular nature
