#!/bin/bash

# Set the target URL
url="http://0.0.0.0:5000/catch_me"

# Send a POST request with a custom header
curl -X POST "$url" -H "Custom-Header: You got me!" >/dev/null 2>&1

# The server response will be displayed by curl, so we don't need to echo anything
