# Employee Data Processing

This project is a data processing tool for employee records stored in a CSV file. It includes classes to model employee records (`Employee`) and process the data (`EmployeeDataProcessor`).

## Project Structure

- **`employee_data.csv`**: Sample CSV file containing employee data.
- **`sort.py`**: Python script that defines the `Employee` and `EmployeeDataProcessor` classes for processing employee data.

## Classes

### `Employee`

- Models an employee record with attributes for first name, last name, email, and years of employment (`years`).
- Supports comparison methods (`__eq__`, `__lt__`) to enable sorting and equality checks based on last name, first name, email, and years.

### `EmployeeDataProcessor`

- Manages a list of `Employee` objects and provides methods to process and retrieve employee data.
  
#### Methods:

- **`get_data_list_from_csvfile(file_name)`**:
  - Reads data from a CSV file and creates `Employee` objects for each record.
  - Appends each object to a list and returns the list.

- **`initialize(file_name)`**:
  - Initializes the `EmployeeDataProcessor` instance with data from the specified CSV file.

- **`get_data_size()`**:
  - Returns the number of `Employee` records in the data list.

- **`get_employee_record(first_name, last_name, years)`**:
  - Retrieves the first `Employee` object that matches the provided first name, last name, and years of employment.
  - Returns `None` if the record is not found.

- **`get_employee_list(start, end, sorted=False)`**:
  - Returns a list of `Employee` objects within a specified range of indices (`start` to `end-1`).
  - Supports optional sorting of the returned list based on last name, first name, and years of employment.

- **`get_years_list()`**:
  - Extracts and returns a list of years of employment from all records in the data list.

- **`plot_emp_years()`**:
  - Generates and displays a histogram plot of years of employment for all employees in the data list using matplotlib.

## Usage

1. **Setup**:
   - Ensure Python is installed on your system.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/namdavid2904/employee-data-processing.git
   ```

3. **Navigate to Project Directory**:
   ```bash
   cd employee-data-processing
   ```

4. **Install Dependencies** (if required):
   ```bash
   pip install matplotlib
   ```

5. **Run the Script**:
   ```bash
   python sort.py
   ```

6. **Output**:
   - The script reads data from `employee_data.csv`, initializes `EmployeeDataProcessor`, and generates a histogram plot of years of employment for employees.

## Dependencies

- **Python**: Programming language used for script execution.
- **matplotlib**: Python library used for data visualization (histogram plot).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
