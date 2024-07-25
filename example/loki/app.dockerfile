# Use the official Python image from the Docker Hub
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./main.py /app

RUN pip install logman

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]
