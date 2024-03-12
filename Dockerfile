# Base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install necessary dependencies
RUN apk add --no-cache git go musl-dev

# Clone and build Subfinder
RUN git clone https://github.com/projectdiscovery/subfinder.git && \
    cd subfinder/v2/cmd/subfinder && \
    go build .

# Copy the Subfinder binary to a directory with appropriate permissions
RUN cp /app/subfinder/v2/cmd/subfinder/subfinder /usr/local/bin/subfinder && \
    chmod +x /usr/local/bin/subfinder

# Copy the Python files
COPY app.py requirements.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt

# Set execute permissions for subfinder binary
RUN chmod +x /app/subfinder/v2/cmd/subfinder/subfinder

# Expose the API port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]
