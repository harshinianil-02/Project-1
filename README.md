#URL Shortener Web Application

#Overview:-
This project is a URL Shortener Web Application built using Python Flask and MySQL. The application allows users to enter a long URL and generate a unique short URL code. When the short URL is accessed, the application redirects the user to the original website

#Features:-
-> Generate unique short URLs for long links

-> Store original URLs and short codes in MySQL database

->Dynamic URL redirection using Flask routes

->Simple and beginner-friendly web interface

->Backend integration with MySQL

#Technologies Used:-
Python
Flask
MySQL
HTML

#Project Structure

URL-Shortener/
│
├── app.py
├── templates/
  └── index.html

How It Works:-

1. User enters a long URL in the input field.

2. Flask receives the URL using a POST request.

3. A random short code is generated.

4. The original URL and short code are stored in MySQL.

5. When the short URL is opened, Flask fetches the original URL from the database.

6. The user is redirected to the original website.

#Database Setup:-

1. Create database:

CREATE DATABASE url_shortener;

2. Use database:

USE url_shortener;

3. Create table:

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_url TEXT,
    short_code VARCHAR(10),
    clicks INT DEFAULT 0
);

#Installation Steps:-

Step 1: Install Flask

python -m pip install flask

Step 2: Install MySQL Connector

python -m pip install mysql-connector-python

#Run the Project:-

```bash
python app.py
```
#Open in browser:

http://127.0.0.1:5000





