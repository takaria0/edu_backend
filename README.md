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

1. install Python3.7 or later and Docker
2. clone this repository
3. run docker-compose.dev.yml (flask and postgres)
run with database (postgres)
```
sh run_dev.sh
```



# For Production

## How to deploy to Google Cloud Run

1. Upload Docker Image to Container Registory
Before deploying to Cloud, be sure to run Docker image on local machine to check it behaves properly.
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

2. Use GUI to deploy to Cloud Run.

If you could upload container correctly, the following part has to be easy. 


3. Configure Settings with Cloud SQL. set ENV correctly.
