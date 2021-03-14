#! /bin/bash

set -eu

if [[ -z ${AWS_ACCESS_KEY_ID+x} ]]; then echo "Variable AWS_ACCESS_KEY_ID unset" && exit 1; fi
if [[ -z ${AWS_SECRET_ACCESS_KEY+x} ]]; then echo "Variable AWS_SECRET_ACCESS_KEY unset" && exit 1; fi
if [[ -z ${MYSQL_PWD+x} ]]; then echo "Variable MYSQL_PWD unset" && exit 1; fi
user="root"
host=${MYSQL_HOST:="127.0.0.1"}
bucket=${AWS_BUCKET_NAME:=asset-migrator-legacy-s3}
database=${MYSQL_DB:=assets}
iterations=${ITERATIONS:=100}

echo "-> Generating $iterations records in DB and items in bucket"
for ((i = 0 ; i < $iterations ; i++)); do
    path="images/avatar$RANDOM.png"
    echo "INSERT INTO assets (path) VALUES (\"$path\");" | mysql -u $user -h $host assets
    aws s3 cp ./this_is_fine.png s3://$bucket/$path
done
echo "-> Done!"
