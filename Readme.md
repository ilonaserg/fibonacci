# Fibonacci API

## Running the application

### Prerequisites

You must have Python3 and pip installed.

Create a virtual environment:

`python -m venv venv`

Activate the virtual environment by running the activate script in the `venv/Scripts` directory.
[This step is OS-dependent](https://docs.python.org/3/tutorial/venv.html).

As per the Python documentation:

On Windows, run:

`venv\Scripts\activate`

On Linux or MacOS, run:

`source venv/bin/activate`

Install the required dependencies by running
`pip install -r requirements.txt` in the root directory of the project.

### Testing the application

Run the API in development mode by executing:

`python app.py`

Once the app is running, go to http://127.0.0.1:5000/fibonacci/1 to see the first element of the Fibonacci sequence.

Feel free to replace 1 by any arbitrary number under the maximum limit of 100.000.

### Running it in production

The flask application has to be placed behind a [WSGI server](https://flask.palletsprojects.com/en/stable/tutorial/deploy/#run-with-a-production-server) (e.g. Gunicorn).

E.g. if you have waitress installed as your WSGI server, the command for running the application is:

`waitress-serve --port 80 app:app`

Now the endpoint is accessible from port 80:

http://127.0.0.1/fibonacci/1

## Operational Considerations

### Containerization

We can build our own Docker image using the base image of Python.

Copy the source code to the container. Install the dependencies from the `requirements.txt` and also our chosen WSGI server.
Run the application using the WSGI server's command with the desired port number.
The exposed port number should be indicated.

If needed, create a docker-compose file with additional configuration and resources, such as redis for caching.

### CI/CD Strategy

[SonarQube](https://github.com/SonarSource/sonarcloud-github-action) could be used for code analysis for PRs.
Merging could only be allowed once the code analysis passes.

After merging, a Docker image could be built, scanned by [Trivy](https://trivy.dev/v0.57/) and then pushed to the Docker registry.

Dependabot on GitHub should be enabled to automatically update dependencies and protect against potential vulnerabilities.
Unit and integration tests could also be automated in GitHub Actions.

### Logging Strategy

Logs could be aggregated on Datadog. We could forward the logs in a JSON format and filter according to our needs.
Datadog agent has to be installed to collect the logs on the server/in the container.

We can use Prometheus for collecting metrics. Grafana could be utilized for performance/availability monitoring, e.g. response time, request and error rate.
Alerts could be set up if anomalies detected, which do not have to be a fixed value,
they could also be dynamically adjusted using trend based anomaly detection (to account for different load based on the time of the day for example).

### Scaling

We can use a load balancer and auto-scaling to distribute the traffic between the instances.

Rate limiting is also important to be set to prevent DoS attacks.

In a containerized environment, we could create a cluster where the scaling is happening automatically based on the load and traffic.

Considering the high amount of repetitive answers, caching would make sense to speed up the response process.