import os

setting = os.environ.get('SETTING', "dev")

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
  

elif setting == "prod":
  # Remember - storing secrets in plaintext is potentially unsafe. Consider using
  # something like https://cloud.google.com/kms/ to help keep secrets secret.
  db_user = os.environ.get("DB_USER")
  db_pass = os.environ.get("DB_PASS")
  db_name = os.environ.get("DB_NAME")
  cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

  SQLALCHEMY_DATABASE_URI = "postgresql+pg8000://{db_user}:{db_password}@/{db_name}?unix_sock=/cloudsql/{cloud_sql_connection_name}/.s.PGSQL.5432".format(
      db_user=db_user,
      db_password=db_pass,
      db_name=db_name,
      cloud_sql_connection_name=cloud_sql_connection_name
  )
  
