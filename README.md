# 🛒 Pricesmart Riwi — Customer Order Management System
## 📖 Description
A modular command-line application built in Python that automates the registration and processing of customer orders for a company.
The system allows registering customers, products and orders, calculating daily revenue, and generating a consolidated final report all from the terminal, without
external dependencies.

## ⚙️ System Architecture
The application follows a modular architecture where each feature lives in its own independent file. The main.py file acts as the entry point and orchestrator: it imports all feature functions, maintains the shared state (tuples for customers, products, and orders), and routes user input from the main menu to the correct module

## 🔁 Flow Diagram
<img width="3920" height="3240" alt="Diagrama de flujo semana 2" src="https://github.com/user-attachments/assets/5eca3017-ebf3-4af5-b1a9-3e552d754f31" />

## How to run the program
1.	Clone or download the repository so all .py files are in the same folder.
2.	Open the main.py file and run it
3.	Follow the on-screen menu to register customers, products, and orders.
4.	After each option the program asks whether to return to the main menu. Type yes to continue or no to exit.

## 💡 Data structure and module descriptions
The code is based on the use of dictionaries and tuples that collect and store the information the user enters as the program requests it.
The program is divided into six independent modules, each responsible for a specific part of the system:

1. Customer Registration — register_client(): The user is asked to enter a customer ID, name, and email. This information is stored in a dictionary, and the
dictionary is added to a tuple that accumulates all registered customers. The user can register as many customers as needed before continuing.

2. Product Registration — register_products(): The user enters a product ID, name, and unit price. Each product is stored in a dictionary and
added to the products tuple. The program keeps asking if the user wants to add another product until they decide to stop.

3. Order Creation — create_order(): The user selects a customer and a product by their ID from the registered data. Then enters the quantity.
The system automatically calculates the subtotal by multiplying the unit price by the quantity and stores the complete order as a dictionary inside the orders tuple.

4. View Orders — check_orders(): This module displays all registered orders in an organized way, showing the order ID, customer name, product, quantity, and
subtotal for each one.

5. Total Sales — total_sales(): This function goes through all registered orders, adds up every subtotal, and returns the total revenue generated during the session.
This value is reused by the final report module.

6. Final Report — generate_final_report(): This part of the program consolidates everything. It displays the total number of orders, the total revenue (using total_sales()), all orders grouped by customer with their individual totals, and a summary of each product sold showing units and earnings. The program ends after the report is displayed.
