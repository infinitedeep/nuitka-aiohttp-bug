#!/usr/bin/env bash

DIMG=$(basename "$(pwd)")
echo "Building image ${DIMG}:"
docker kill ${DIMG}
docker rm ${DIMG}
docker build -t "${DIMG}" .
docker run -d --restart=always --name "${DIMG}" "${DIMG}"
