# Store Sash

The project of a small marketplace specialized in the sale of clothing

#### Stack:

##### Frontend

- [JavaScript](https://nodejs.org/en/download/)
- [CSS](https://ru.wikipedia.org/wiki/CSS/)
- [HTML](https://ru.wikipedia.org/wiki/HTML/)

##### Backend

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.11 -m venv ../venv
   source ../venv/bin/activate
   ```
2. Install packages:
   ```bash
   poetry install
   poetry update
   ```
3. Run project dependencies, migrations, fill the database with the fixture data etc.:
   ```bash
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver
   ```
4. Run [Redis Server](https://redis.io/docs/getting-started/installation/):
   ```bash
   redis-server
   ```
5. Run Celery:
   ```bash
   celery -A store worker --loglevel=INFO
   ```
