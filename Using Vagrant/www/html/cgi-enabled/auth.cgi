#!/bin/bash
# Copyright (c) 2017 Oracle. All rights reserved.
# This material is the confidential property of Oracle Corporation or its
# licensors and may be used, reproduced, stored or transmitted only in
# accordance with a valid Oracle license or sublicense agreement.
# Live Experience Sample Auth Module
#
# This shell script allows a Javascript application to retrieve a JWT token
# from Live Experience when provided with a valid client ID and secret.
# The client-credentials should be written to a text file in the format:
# <ID>:<SECRET>
# e.g. using the command: echo "ID:SECRET" >secret.txt
# This line specifies the path to the client-credentials file,
# if you move the file update this line to the new location
SECRET_PATH="./secret.txt"
# make sure curl command can be found
PATH=/bin:/usr/bin:/usr/sbin:$PATH
# build up auth server URL (allow replacing the server on the command line for testing)
if [ $# -eq 1 ]; then
 AUTH_SERVER="$1"
else
 AUTH_SERVER="https://live.oraclecloud.com"
 ## EMEA customers use:
 ## AUTH_SERVER="https://emea.live.oraclecloud.com"
fi
AUTH_PATH="/auth/apps/api/access-token"
AUTH_ARGS="?grant_type=client_credentials&state=0&scope=optional&nonce=${RANDOM}"
AUTH_SECRET=`cat ${SECRET_PATH}`
# add curl arguments to temporary file to avoid including on curl command file
tmpdir=$(mktemp -d "${TMPDIR:-/tmp/}.XXXXXXXXXXXX")
cat >${tmpdir}/args.txt <<EOF
--insecure
--silent
--show-error
url = "${AUTH_SERVER}${AUTH_PATH}${AUTH_ARGS}"
user = "${AUTH_SECRET}"
EOF
# set the content type
echo "Content-type: application/json"
echo ""
# retrieve the JWT token
curl --disable --config ${tmpdir}/args.txt
echo ""
# remove the temporary directory
rm -rf ${tmpdir}
exit 0
