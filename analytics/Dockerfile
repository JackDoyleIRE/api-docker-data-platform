FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the script files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run generate_report.py when the container launches
CMD ["python" ,"generate_report.py"]