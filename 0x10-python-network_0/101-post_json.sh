#!/bin/bash
# sends a POST request to the passed URL, and displays the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
