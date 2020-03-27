# Environment
for Mac

LANG: 
- Python 3.7 / Flask

DB:
- Postgres in docker for local
- Postgres in Google Cloud SQL for staging and production

Other tools:
- Docker
- SQLAlchemy (ORM for Python)
- Postman

# For Developlement
## setup

1. install Python3.7 or later
2. clone this repository
3. create virtual env for python
```
python3 -m venv env_dev
```
4. install libraries using pip
```
pip install -r requirements.dev.txt
```

## run on local
run with database (postgres)

```
sh run_dev.sh
```


# For Production

## How to deploy to Google Cloud Run

1. Upload Docker Image to Container Registory
Before deploying to Cloud, be sure to run Docker image on local machine to check it behave properly.

without database
```
docker build -t foo .
docker run -t foo
```

or with database (postgres)

```
sh run_dev.sh
```

Once the contairer runs correctly, push the image to Google Container Storage

```
gcloud builds submit --tag gcr.io/[project-id]/[container-name]
```

2. Use GUI to deploy to Cloud Run
if you can upload container correctly, the following part has to be easy.

3. Configure Settings with Cloud SQL. set ENV correctly.
