FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./api/requirements.txt .

# Install the dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API source code into the container
COPY ./api .

# Expose the port that FastAPI will run on (default is 8000)
EXPOSE 8080

# Start FastAPI with Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
