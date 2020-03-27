# For Developlement

run with database (postgres)

```
sh run_dev.sh
```

## Dev tools
Postman on Chrome


# For Production
app.py
Dockerfile

# How to deploy to Google Cloud Run

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
