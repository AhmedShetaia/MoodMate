# Use a lightweight version of Python
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./app/requirements.txt .

# Install the dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit source code into the container
COPY ./app .

# Expose the port that Streamlit will run on (default is 8501)
EXPOSE 8501

# Start Streamlit
CMD ["streamlit", "run", "app.py"]
