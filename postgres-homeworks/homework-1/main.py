"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

"""Создаем подключение"""
conn = psycopg2.connect(
    user='postgres',
    password='9184',
    host='localhost',
    database='north'
)

"""создаем курсор"""
cursor = conn.cursor()

with open("north_data/customers_data.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        query = 'INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)'
        cursor.execute(query, tuple(row))

with open("north_data/employees_data.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        query = 'INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, tuple(row))

with open("north_data/orders_data.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        query = 'INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(query, tuple(row))

conn.commit()
cursor.close()
conn.close()