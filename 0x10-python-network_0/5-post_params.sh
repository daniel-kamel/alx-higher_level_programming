#!/bin/bash
# sends a POST request to the passed URL, and displays the response
curl -sX POST -d "email=test%40gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
