
#  Una Health Backend
## Description

I implemented Una health API with Django.

- /api/v1/levels/  Retrieve ( GET ) a list of glucose levels for a given
    
    user_id , filter by start and stop timestamps (optional). This endpoint should support pagination, sorting, and a way to limit the number of glucose levels returned.

- /api/v1/levels/<id>/  Retrieve ( GET ) a particular glucose level by id .
## Run Locally

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   # Clone repo
   git clone https://github.com/takahiromitsui/una-health.git
   ```
2. **Poetry install**
   This project uses Poetry for dependency management. To install Poetry, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

Once you have Poetry installed, you can install the project dependencies with:

```bash
  cd backend
  poetry install
```

3. Migration and insert data

```bash
    cd rest_api
    # migration
    poetry run python manage.py migrate
    # load csv files
    poetry run python manage.py load_glucose_data ./restapi/glucose_levels/data_files/
```



4. Access the application:
```bash

poetry run python manage.py runserver

```

- Django Endpoint: Open your browser and go to http://127.0.0.1:8000/api/docs/ to view the API documentation and test endpoints.


5. Run tests:

```bash
poetry run pytest
```



## Deployment

I separated local and production environments.

If you would like to use different database or other settings such as CORS,
you can add settings on `backend/restapi/settings/production.py`.

And you need to turn it off debug mode on `backend/restapi/settings/base.py`


```bash
DEBUG = False

```

