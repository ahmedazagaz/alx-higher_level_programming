#!/bin/bash
# Get the URL request that is sent and displays the size of the body of the response.
curl -s "$1" | wc -c
