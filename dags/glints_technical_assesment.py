import datetime as dt

from airflow import DAG

from airflow.operators.postgres_operator import PostgresOperator

from airflow.hooks.postgres_hook import PostgresHook

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2021, 5, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('glints_technical_assessment',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:


    src = PostgresHook(postgres_conn_id='src_postgress_conn')

    dest = PostgresHook(postgres_conn_id='dest_postgress_conn')

    src_conn = src.get_conn()

    cursor = src_conn.cursor()

    dest_conn = dest.get_conn()

    dest_cursor = dest_conn.cursor()

    dest_cursor.execute("SELECT COUNT(id) FROM dest_airflow_assessment;")

    id = dest_cursor.fetchone()[0]

    if id is None:

        id = 0

    cursor.execute("SELECT * FROM src_airflow_assessment", [id])

    dest.insert_rows(table="dest_airflow_assessment", rows=cursor)

   
