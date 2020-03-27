import os
setting = os.environ['SETTING']

if setting == "dev":
  user = os.environ['POSTGRES_USER']
  password = os.environ['POSTGRES_PASSWORD']
  host = os.environ['POSTGRES_HOST']
  db = os.environ['POSTGRES_DB']
  port = os.environ['POSTGRES_PORT']

  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
          user=user,
          password=password,
          host=host,
          port=port,
          database=db
      )