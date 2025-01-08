import pyodbc
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)


def get_mssql_connection():
    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={os.getenv("server")};DATABASE={os.getenv("database")};'
            f'Trusted_Connection=yes;Encrypt=no;TrustServerCertificate=yes'
        )
        return connection
    except Exception as e:
        print("Error in get_mssql_connection " + str(e))
        return None


def put_result(query, data):
    try:
        mssql_conn = get_mssql_connection()
        cursor_str = mssql_conn.cursor()
        cursor_str.execute(query, data)
        mssql_conn.commit()
        mssql_conn.close()
        return cursor_str.rowcount
    except Exception as e:
        print("Error in put_result()" + str(e))


def get_result_col(query):
    try:
        mssql_conn = get_mssql_connection()
        cursor_str = mssql_conn.cursor()
        cursor_str.execute(query)
        res = cursor_str.fetchall()
        field_names = [i[0] for i in cursor_str.description]
        cursor_str.close()
        mssql_conn.close()
        return res, field_names
    except Exception as e:
        print("Error in get_result_col()" + str(e))


def get_result(query):
    try:
        mssql_conn = get_mssql_connection()
        cursor_str = mssql_conn.cursor()
        cursor_str.execute(query)
        row = cursor_str.fetchall()
        mssql_conn.close()
        return row
    except Exception as e:
        print("Error in get_result()" + str(e))


def call_proc(query, values):
    try:
        mssql_conn = get_mssql_connection()
        cursor_str = mssql_conn.cursor()
        cursor_str.execute(query, values)
        rows = cursor_str.fetchall()
        cursor_str.close()
        mssql_conn.commit()
        mssql_conn.close()
        return rows if rows else None
    except Exception as e:
        print("Error in call_proc()" + str(e))


def do_result(query):
    try:
        mssql_conn = get_mssql_connection()
        cursor_str = mssql_conn.cursor()
        cursor_str.execute(query)
        mssql_conn.commit()
        mssql_conn.close()
        return cursor_str.rowcount
    except Exception as e:
        print("Error in do_result()" + str(e))
