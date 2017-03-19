#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the size of the body
curl -l -s -i $1 | grep Content-Length | cut -b 17,18
