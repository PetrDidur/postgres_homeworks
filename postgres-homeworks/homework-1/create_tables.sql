-- SQL-команды для создания таблиц
CREATE TABLE employees (
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NUll,
	last_name VARCHAR(100) NOT NUll,
	title VARCHAR(50),
	birth_date DATE,
	notes TEXT
);

CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	company_name VARCHAR(100) NOT NULL,
	contact_name VARCHAR(100)
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id),
	employee_id INT REFERENCES employees(employee_id),
	order_date DATE,
	ship_city VARCHAR(50)
);
