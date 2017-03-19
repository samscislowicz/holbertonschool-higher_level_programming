#!/bin/bash
# sends a DELETE request to the URL
curl -s -i -L -X "DELETE" $1 | tail -1
