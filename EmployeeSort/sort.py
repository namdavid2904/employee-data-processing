import csv
import matplotlib.pyplot as plt

class Employee:
    """models an Employee record."""
    def __init__(self, first_name, last_name, email, years):
        self.first_name=first_name
        self.last_name=last_name
        self.email = email
        self.years = years

    def  __eq__(self, other):
        return (self.last_name == other.last_name) and (self.first_name == other.first_name) and (self.email == other.email) and (int(self.years) == int(other.years))

    def __lt__(self, other):
        if self.last_name != other.last_name:
            return self.last_name < other.last_name
        elif self.first_name != other.first_name:
            return self.first_name < other.first_name
        else:
            return int(self.years) > int(other.years)


    def __str__(self):                                                                                                                                                                            
        info_str = f'{self.first_name} {self.last_name} {"email:"} {self.email}' \
                    f' {"years:"} {self.years}' 
        return(info_str)  

class EmployeeDataProcessor:

    def __init__(self, data_list=None):
        self.data_list = []

    def get_data_list_from_csvfile(self, file_name):
        """This method opens the csv file passed in and 
            creates an Employee object for each row of data
            in the file. It appends each object to a list and 
            returns that list."""
        with open(file_name, "r") as  file:
            next(file)
            read_data = file.readlines()
        for line in read_data:
            self.data_list.append(Employee(*line.strip().split(",")))
        return self.data_list

    def initialize(self, file_name):
        self.data_list = self.get_data_list_from_csvfile(file_name)

    def get_data_size(self):
        return len(self.data_list)

    def get_employee_record(self, first_name, last_name, years):
        """Returns the first Employee object in the data_list that
           matches first_name, last_name, and years.
           Returns None if the record is not found."""
        if self.data_list:
            for employee in self.data_list:
                if (employee.first_name == first_name) and (employee.last_name == last_name) and (int(employee.years) == int(years)):
                    return employee
        return None


    def get_employee_list(self, start, end, sorted=False):
        """ Returns a list of employee object from data_list that fall
            within a specific range as specified by start and end index parameters.
            The value of start can be: 0<= start < end.
            The value of end can be: start < end <= length of data_list.
            An Exception is raised if start and end values do not meet these constraints.
            Note that start and end are list indexes, and you should return Objects from start to end -1, 
            so the end index is not included in the range.
            Example:
            start 0, end 5
            first employee:  'hbartczak0@squidoo.com'
            last employee:  'bbamell4@cafepress.com'
            The list is returned in ascending order if the sorted parameter is True,
            unsorted otherwise (default)."""
        if self.data_list:
            if (0 <= start < end <= len(self.data_list)) == False:
                raise Exception("Invalid Range")
            else:
                if sorted == False:
                    return self.data_list[start:end]
                else:
                    a = self.data_list[start:end]
                    a.sort()
                    return a


    def get_years_list(self):
        """Returns a list that contains only the years from 
            all records on the data_list."""
        if self.data_list:
            return [int(i.years) for i in self.data_list]



    def plot_emp_years(self):
        """Creates and displays a histogram plot of all of the years
            that employees in data_list have worked."""
        data = self.get_years_list()
        #specify bin start and end points
        bin_ranges = [0,1,2,3,4,5,6,7,8,9,10]
        #create histogram with 4 bins
        plt.hist(data, bins=bin_ranges, edgecolor='black')
        plt.title("Years of Employment")
        plt.xlabel("Years")
        plt.ylabel("Frequency")
        plt.show()   

if __name__=="__main__":
    file_name = "employee_data.csv"
    #file_name = "test.csv"
    emp_proc = EmployeeDataProcessor()
    emp_proc.initialize(file_name)
    emp_proc.plot_emp_years()
