☕ Python Command-Line Coffee Machine Simulator
This project is a command-line interface (CLI) application that simulates the operation of a coffee vending machine. It allows users to select from various coffee drinks, checks for ingredient availability, processes payments with change, and manages internal resources. This interactive simulation serves as a practical demonstration of core Python programming principles and robust application design.

✨ Features
Drink Selection: Users can choose from "espresso", "latte", or "cappuccino".
Resource Management: Tracks and updates internal supplies of water, milk, and coffee beans.
Resource Checking: Verifies if sufficient ingredients are available before processing an order.
Payment System:
Prompts for coin insertion.
Accumulates payment incrementally.
Provides real-time feedback on the amount due.
Calculates and dispenses change.
Allows users to cancel payment at any point.
Error Handling: Gracefully manages invalid (non-numeric) user input during payment.
Reporting: Provides an on-demand report of current resource levels and accumulated money.
Graceful Exit: Allows the user to "turn off" the machine, exiting the program cleanly.
⚙️ Algorithm & Design
The application follows a structured, modular design pattern:

Initialization:
Global menu (drink recipes and costs) and resources (current inventory) are loaded from external modules (menu.py, resources.py), promoting separation of concerns.
Main Loop (coffee_machine function):
Operates in an infinite loop, constantly prompting the user for their desired action (drink order, "report", or "turn off").
Validates user input for the primary choice.
Action Dispatch:
If "report" is chosen, the report() function displays current resource levels.
If "turn off" is chosen, a farewell message is displayed, and the loop breaks, ending the program.
For drink orders:
Resource Check (check_resource): Iterates through the ingredients required for the chosen drink. It compares these against current resources. If any ingredient is insufficient, it informs the user and aborts the order.
Payment Processing (cashier): If resources are sufficient, the cashier function takes over.
It maintains a total_paid accumulator.
A while loop continues until total_paid meets or exceeds the drink's cost.
Inside the loop, try-except ValueError handles non-numeric input, re-prompting the user.
Users can type "cancel" to abort payment, triggering a refund of total_paid.
Upon successful payment, the machine's money resource is updated, and change is calculated and dispensed. The function returns True for success, False for cancellation.
Coffee Production (produce_coffee): If cashier returns True, the produce_coffee function is called. It deducts the required ingredients from resources and prints a "Enjoy!" message.
This design ensures that each core operation (checking, paying, producing) is encapsulated within its own function, improving readability and maintainability.

💻 Skills Demonstrated
This project effectively showcases a range of essential Python programming skills relevant to software development:

Python Fundamentals: Strong command of core syntax, data types (dictionaries, lists, floats, booleans), control flow (if/elif/else, while loops), and string formatting (f-strings).
Modular Programming: Expert use of functions for logical decomposition and code reusability. The design promotes single responsibility for each function.
Data Structures: Practical application of dictionaries for representing complex data (menu items, ingredients, resources) and lists for managing choices.
Robust Error Handling: Implementation of try-except blocks to gracefully manage ValueError from user input, making the application resilient to common user mistakes.
Input Validation: Thorough validation of user choices and numerical inputs, ensuring program stability and a smooth user experience.
State Management: Effective management of mutable program state (resources dictionary) across different functions, demonstrating how to track and update dynamic data.
User Interface (CLI): Design of clear and informative command-line prompts and outputs for an intuitive user interaction.
Floating-Point Arithmetic Handling: Awareness and application of formatting techniques (.2f) to display currency values accurately and cleanly, mitigating common floating-point precision issues.
External Data Loading: Utilization of import statements to load configuration/initial data from separate modules, promoting cleaner code and easier updates.
