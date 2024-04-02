#!/bin/bash
# sending an argument to the url.
curl -sL -w "%{http_code}" -I "$1" -o /dev/null
