# Dockerfile

# Get base image
FROM python:3.7

# Set label
LABEL version="v1.0.1" maintainer="luthfi.anandra@gmail.com"

# Copy and install requirements
COPY requirements.txt /
RUN pip install -r requirements.txt

# Copy remaining files and set workdir
COPY . /usr/local/lib/python3.7/site-packages/bmi-calculator
WORKDIR /usr/local/lib/python3.7/site-packages/bmi-calculator

# Run application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
