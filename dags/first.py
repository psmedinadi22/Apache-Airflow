import pandas as pd
from airflow.exceptions import AirflowException
from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook

def export_to_excel():
    try:
        # Connect to the database and execute the SQL query
        mysql_hook = MySqlHook(mysql_conn_id='mysql_ecommerce')
        conn = mysql_hook.get_conn()
        query = 'SELECT * FROM ecommerce.orders;'
        df = pd.read_sql(query, conn)
        
        # Save results to an Excel file
        excel_file = '/Users/paulamedina/Documents/Airflow/file.xlsx'
        df.to_excel(excel_file, index=False) 
        print("Exported data to Excel successfully.")
    except Exception as e:
        # Catch any exceptions and log them as an error in Airflow
        error_message = f"An error occurred while exporting data to Excel: {str(e)}"
        print(error_message) 
        raise AirflowException(error_message)


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 3),
    'schedule_interval': '@daily',
}

with DAG('mysql_to_excel_report', default_args=default_args, catchup=False) as dag:
    export_to_excel_task = PythonOperator(
        task_id='export_to_excel',
        python_callable=export_to_excel
    )

export_to_excel_task
