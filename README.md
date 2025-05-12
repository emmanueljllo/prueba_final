Inventory Management System - Module 1

This is a basic Inventory Management System written in Python as part of a performance test for Module 1. It allows users to manage products through a console-based interface.

Features

Add new products to the inventory

Search for existing products

Update product details

Delete products

Calculate total inventory value

Display full inventory

Input validation for name, price, and quantity


Getting Started

Prerequisites

Python 3.x installed on your machine


Running the Program

To run the program, simply execute the Python file in your terminal or IDE:

python <filename>.py

Menu Options

Once the program starts, the user will see a menu with the following options:

1. Add Products: Add a new product by entering name, price, and quantity.


2. Search Products: Search for a product by name.


3. Update Products: Update the price and quantity of an existing product.


4. Delete Products: Remove a product from the inventory.


5. Calculate Inventory Value: Calculate the total value of the inventory.


6. Show Inventory: Display all the products in the inventory.


7. Exit: Exit the program.



Validation Rules

Name: Must be alphabetic, 3–20 characters long.

Price: Must be a positive number.

Quantity: Must be a non-negative integer.


File Structure

All data is stored in a Python list of dictionaries during runtime.

Each product is represented as a dictionary with name, price, and quantity.


Notes

This program runs in memory only. No external storage is used.

All operations and validations are performed through terminal prompts.
