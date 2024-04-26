#!/bin/bash
# Displays response after DELETE request

url="${1}"

curl -sX DELETE "$url"
