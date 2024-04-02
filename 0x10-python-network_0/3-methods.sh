#!/bin/bash
# display the available http method and server will accept.
curl -sI "$1" | awk -v FS=": " '/^Allow/{print $2}'
