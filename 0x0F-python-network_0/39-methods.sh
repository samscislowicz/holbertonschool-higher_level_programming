#!/bin/bash
# displays all HTTP methods the server will accept.
curl -s -i -L  $1 | grep Allow: | cut -b 8-
