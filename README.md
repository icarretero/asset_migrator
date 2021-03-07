# asset_migrator
Migrate assets between buckets

## Local instructions for Development:
If you want to populate a local MariaDB for a dev enviroment follow these steps. It is asumed you have a terminal capable of running bash and docker daemon installed and working.

### Spin up a MariaDB docker container
```bash
docker run -e MYSQL_ROOT_PASSWORD=<password-of-your-choice> -p 3306:3306 mariadb
```
Do not forget to run this command with a user with access to the Docker socket or capable of sudo.

### Populate the DB
In a different terminal run the script in the `local` folder with the following env-vars:
- `MYSQL_PWD`: The password for the `root` user you chose in the previous step
- `MYSQL_HOST`: (optional) The host in case you don't use docker as in the previous step. Default is `127.0.0.1`
- `ITERATIONS`: (optional) The number of entries you want to be created. Default is 1000

```bash
ITERATIONS=500 MYSQL_PWD=<password-you-chose-in-previous-step> ./populate_db.sh
```

If you __don't__ want to create the DB `assets` and the table `assets` remove the `-c` parameter in the previous command. The populate script requires that DB and table to exist.
