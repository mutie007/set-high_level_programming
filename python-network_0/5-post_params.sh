#!/bin/bash
# Takes a URL, sends a POST request with email and subject parameters, and displays the body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
