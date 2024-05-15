# **Creation of a simple FastAPI application and containerisation with Docker**

## Instructions on how to build and run the Docker container and execute the unit tests:

***Build and Run Docker***

1- Open a terminal and browse to the directory where your FastAPI application and Docker file are located.

```bat
cd C:\Users\oumai\OneDrive\python_code\.venv
```

2- **Build Docker image:** Run the following command to build the Docker image.
```bat
docker build -t my-fastapi-app .
```

3- **Run Docker container:** After the image is built successfully, start a Docker container based on that image.

```bat
docker run -dp 8080:80 my-fastapi-app
```
***Execute unit tests***

1- Install the necessary dependencies for testing: pytest

```bat
pip install pytest
```

2- Open a terminal and browse to the directory where your FFastAPI application and unit test files are located.

3- Execute unit test with pytest

```bat
pytest test_main
```

