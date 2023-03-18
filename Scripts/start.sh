#!/bin/bash
set -e

export SSL=false
export DOMAIN_NAME=localhost:5213

dotnet /app/Server.dll &
exec "$@"