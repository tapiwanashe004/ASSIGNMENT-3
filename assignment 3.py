#QUESTION 1
def classify_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num > 0:
                return "Positive"
            elif num < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#QUESTION 2

def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)


#Question 3
def get_valid_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


#QUESTION 4
def write_and_read_names():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]

    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

    with open("names.txt", "r") as file:
        for line in file:
            print(line.strip())


#QUESTION 5
def convert_temperatures():
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = list(map(lambda c: c * 9 / 5 + 32, celsius_temps))
    print("Converted temperatures:", fahrenheit_temps)


convert_temperatures()

#QUESTION 6
def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except TypeError:
        print("Both inputs must be numbers!")


#QUESTION 7.

class NegativeNumberError(Exception):
    pass


def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")



try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Error: {e}")

#QUESTION 8
import random


def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Random numbers:", random_numbers)
    average = sum(random_numbers) / len(random_numbers)
    print("Average:", average)


generate_random_numbers()

#QUESTION 9.

import re


def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)  # Find all emails in the text


def validate_date(date):
    return bool(re.match(r'\d{4}-\d{2}-\d{2}', date))  # Check if the date matches the "YYYY-MM-DD" format


def replace_word(text, old, new):
    return re.sub(r'\b' + old + r'\b', new, text)  # Replace a word with another


def split_string(text):
    return re.split(r'[^a-zA-Z0-9]', text)  # Split the text at non-letter/number characters


# Example usage
text = "Contact john.doe@example.com for more info."
print("Emails:", extract_emails(text))
print("Date valid:", validate_date("2023-09-12"))
print("Replaced text:", replace_word("Hello world", "world", "Python"))
print("Split text:", split_string("Hello, world! How are you?"))




# QUESTION 10
import socket


def server_program():
    server_socket = socket.socket()  # Create a server socket
    server_socket.bind(('localhost', 5000))  # Bind it to the address
    server_socket.listen(1)  # Listen for one client connection

    print("Server is running and waiting for a connection...")
    conn, addr = server_socket.accept()  # Accept a client connection
    print(f"Connected to {addr}")

    message = "Hello from server!"
    conn.send(message.encode())  # Send the message
    conn.close()  # Close the connection


if __name__ == '__main__':
    server_program()

#Client(Client.py)
import socket


def client_program():
    client_socket = socket.socket()  # Create a client socket
    client_socket.connect(('localhost', 5000))  # Connect to the server

    message = client_socket.recv(1024).decode()  # Receive the message from the server
    print("Message from server:", message)

    client_socket.close()  # Close the connection


if __name__ == '__main__':
    client_program()

#QUESTION 11

import requests


def get_data():
    response = requests.get('https://api.example.com/data')  # Request data from an API
    if response.status_code == 200:
        print("Data received:", response.json())  # Print the data from the API
    else:
        print(f"Error: {response.status_code}")


get_data()

#QUESTION 11 CONTINUING
import sqlite3
def connect_to_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 30))

    conn.commit()  # Save changes
    cursor.execute('SELECT * FROM users')
    print(cursor.fetchall())

    conn.close()
connect_to_db()

