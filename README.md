# Setup and run:
1. Make sure docker and docker-compose is installed.
2. Clone the project to your local.
3. Setup `.env` file according to `.env-example`
4. Run `docker-compose build` to build the dependencies.
5. Run `docker-compose up database` then `docker-compose run --rm web python manage.py migrate` to make necessary migrations.
6. Run `docker-compose up database` then `docker-compose up web` to start application.


# Debugging:
1. Based on `docker-compose.override.example.yml` create a `docker-compose.override.yml`
2. Create launch.json file with the following
```
{
  "name": "Remote Django App",
  "type": "python",
  "request": "attach",
  "pathMappings": [
    {
      "localRoot": "${workspaceFolder}",
      "remoteRoot": "/code"
    }
  ],
  "port": 3500,
  "host": "localhost"
}
```