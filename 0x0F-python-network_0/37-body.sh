#!/bin/bash
#takes in a URL,sends a GET request to the URL displays the body of the response
curl -L -s -i $1 -XGET | tail -1
