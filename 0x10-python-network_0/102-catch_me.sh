#!/bin/bash

# Set the target URL
URL="http://0.0.0.0:5000/catch_me"

# Create a JSON file with the required content
echo '{"key": "You got me!"}' > request.json

# Send a POST request with the JSON file
curl -s -X POST -H "Content-Type: application/json" -d @request.json "$URL" >/dev/null 2>&1

# Clean up the temporary JSON file
rm request.json

