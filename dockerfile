# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for MySQL database
ENV MYSQL_DATABASE=ERMS
ENV MYSQL_USER=ROOT
ENV MYSQL_PASSWORD=1991
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the command to start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
