# OOP Calorie Counter

**Calorie Counter using Python**

## Overview

This repository contains a Python application for counting and tracking calorie intake. It's implemented using object-oriented programming (OOP) principles and provides a convenient way to monitor calorie comsumption and earnings in the restaurant.

## Directory Structure

The repository is organized as follows:

- `data/`: Contains JSON files and Python scripts for reading data.
  - `json_files/`: JSON data files.
    - `combos.json`: JSON file for combo meal data.
    - `meals.json`: JSON file for individual meal data.
    - `orders_history.json`: JSON file for order history.
  - `read_data_files/`: Python scripts to read and process JSON data.
    - `data_advanced_dict.py`: Script for advanced data dictionary operations.
    - `data_easy_dict.py`: Script for basic data dictionary operations.
- `module/`: Contains project modules and utilities.
  - `tests/`: Unit tests for the project.
    - `test_class.py`: Test cases for classes.
    - `test_function.py`: Test cases for functions.
  - `__init__.py`: An empty file to make the directory a Python module.
  - `exception.py`: Custom exceptions used in functions.
  - `functions_calorie_counter.py`: Functions to calculate calories and prices.
- `main_examples_of_use_functions.ipynb`: Jupyter Notebook with examples of using functions.
- `statistic_analysis_of_orders.ipynb`: Jupyter Notebook with data analysis and answers to specific questions.
- `requirements.txt`: List of project dependencies.
- `README.md`: This README file.

## Cloning and Environment Setup

To clone the repository and set up the environment, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ZofiaSamsel/OOP_Calorie_Counter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OOP_Calorie_Counter
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the calorie counter, see the `main_examples_of_use_functions.ipynb` and the `statistic_analysis_of_orders.ipynb` and follow the examples. You can add, update, and view your calorie intake.

## Running Tests

Unit tests are provided to ensure the correctness of the code. There are two test files available:

- `test_class.py`: This file contains test cases for classes within the project. It checks that class methods and attributes work as expected.

- `test_function.py`: This file contains test cases for functions in the project. It verifies that functions produce the correct results and handle edge cases properly.

To run the tests, make sure you are in the project directory and execute the following command:

    ```bash
    pytest
    ```



