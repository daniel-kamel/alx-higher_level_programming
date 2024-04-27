#!/bin/bash
# Displays the status code of a given URL
curl -s -o /dev/null -w "%{http_code}" "$1"
