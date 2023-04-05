#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
<<<<<<< HEAD
curl -s "$1" | wc -c
=======
echo "$(curl -s -o /dev/null -w %{size_download} $1)"
>>>>>>> 6aac49cdb4c301ed463ac144e40d92f793d4802d
