import mysql.connector
import pandas as pd
import streamlit as st

st.title("📊 Kafka Logs Dashboard (MySQL)")

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',      # replace with your MySQL username
    password='12345',  # replace with your MySQL password
    database='kafka_logs'
)

# Query data from MySQL
query = "SELECT * FROM user_logs"
df = pd.read_sql(query, conn)

st.dataframe(df)
