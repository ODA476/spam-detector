# Use a slim Python image for efficiency
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Install dependencies first (better caching)
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app folder
COPY ./app /code/app

# Run the API using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]