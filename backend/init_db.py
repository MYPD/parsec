import os
import psycopg2

#for localhost

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['postgres'],
    password=os.environ['Foxtastic'])
