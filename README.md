# Continente Automated Grocery Shopping

This is a project that aims to automate the grocery shopping process. It is a work in progress.

## Features

- Integrates with the Continente website to place the order

## Requirements

- Python 3.6+
- A Continente account

## Setup

1. Clone the repository
2. Install Selenium by running `pip install selenium` in the command line
3. Create a file called `.env` in the root directory of the project with your Continente credentials
   - `CONTINENTE_USERNAME=your_username`
   - `CONTINENTE_PASSWORD=your_password`
4. Create a file called `groceries.txt` in the root directory of the project with the items you want to buy
   - Each item should be on a new line
   - Example:
     ```
     banana
     apples
     orange
     ```
5. Run `python main.py` in the command line
