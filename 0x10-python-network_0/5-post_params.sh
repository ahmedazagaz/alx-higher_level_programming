#!/bin/bash
# sending a POST request .
curl "$1" -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
