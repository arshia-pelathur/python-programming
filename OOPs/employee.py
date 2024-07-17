class Employee:
    def __init__(self,name,idnumber,dept,jobtitle):
        self.name = name
        self.id = idnumber
        self.dept = dept
        self.jobtitle = jobtitle

    def display(self):
        print('\nEmployee Name - ',self.name)
        print('ID Number - ',self.id)
        print('Department - ',self.dept)
        print('Job Title - ',self.jobtitle)

emp1 = Employee("Vishnu Boorla", 47899, "Development", "Senior project Manager")
emp2 = Employee("Diksha Singh", 39119, "IT Dept", "Software Developer III")
emp3 = Employee("Susan Rogers", 81774, "Human Resources", "Talent Search Specialist")

emp1.display()
emp2.display()
emp3.display()