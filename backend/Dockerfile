# Container image 
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Set env
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Install system dependencies for mysqlclient
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-dev

# Copy current directory to /app
COPY . /app

# Upgrade pip and install Python dependencies:
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Start uWSGi
CMD ["uwsgi", "app.ini"]
