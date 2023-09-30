#!/bin/bash
# send a get request with custome data and display body
curl -s "$1" -X GET -H 'X-HelloSchool-User-Id: 98'
