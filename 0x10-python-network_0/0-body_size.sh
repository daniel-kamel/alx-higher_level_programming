#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -ne 1 ]; then
  echo "Usage: $0 <url>"
  exit 1
fi

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
