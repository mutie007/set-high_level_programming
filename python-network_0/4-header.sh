#!/bin/bash
# Takes a URL, sends a GET request with header X-School-User-Id: 98, and displays the body
curl -sH "X-School-User-Id: 98" "$1"
