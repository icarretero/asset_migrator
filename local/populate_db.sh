#! /bin/bash

set -eu

# Flags supported"
# -c: create objects: database "assets" and table "assets"

CREATEOBJECTS='false'

while getopts 'c' flag; do
  case "${flag}" in
    c) CREATEOBJECTS='true' ;;
  esac
done
readonly INCLUDEGLOBALS

user="root"
if [[ -z ${MYSQL_PWD+x} ]]; then echo "Variable MYSQL_PWD unset" && exit 1; fi
iterations=${ITERATIONS:=1000}
host=${MYSQL_HOST:="127.0.0.1"}

if [[ $CREATEOBJECTS = "true" ]]; then
    echo "-> Create objects option activated. Creating DB and table"
    mysql -u $user -h $host mysql < create_db.sql
    echo "-> DB and tables created"
fi

echo "-> Generating $iterations records"
for ((i = 0 ; i < $iterations ; i++)); do
    mysql -u $user -h $host assets < insert_row.sql
done
echo "-> Done!"
