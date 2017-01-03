#!/bin/bash

sleep 1

say 'your finder is saying hello to you'

osascript -e 'tell application "Finder" to display dialog "hello"' 

exit

