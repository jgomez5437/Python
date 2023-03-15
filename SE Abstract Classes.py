#Jesus Gomez Martinez
#22561 Prog & Prob Solv 2
#SE w/ Abstract Classes & Methods

from abc import ABC, abstractmethod
import doctest

class Employee(ABC):
    def __init__(self, first_name=None, last_name=None, social_security=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__social_security = social_security
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        
        self.__first_name = first_name
    
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        
        self.__last_name = last_name
        
    @property
    def social_security(self):
        return self.__social_security
    @social_security.setter
    def social_security(self, social_security):
        self.__social_security = social_security
    
    @abstractmethod
    def earnings(self):
        raise NotImplementedError
    def __repr__(self):
        return f'{self.first_name} {self.last_name}, SSN: {self.social_security}'
    
class SalariedEmployee(Employee):
    def __init__(self, first_name=None, last_name=None, social_security=None, weekly_salary=None):
        """Initializes a SalariedEmployee object.
        
        >>> person1 = SalariedEmployee("Jesus", "Martinez", 1234567, 1500)
        >>> person1.first_name
        'Jesus'
        >>> person1.earnings
        'Earnings: 1500'
        
        Earnings method should return an error if salary is less than 0.
        >>> person1.earnings = -100
        Traceback (most recent call last):
        ...
        ValueError: Weekly salary must be greater than or equal to zero.
        """   
        super().__init__(first_name, last_name, social_security)
        self.__weekly_salary = weekly_salary
    
    @property
    def earnings(self):
        return f'Earnings: {self.__weekly_salary}'    
    @earnings.setter
    def earnings(self, weekly_salary):
        if weekly_salary >= 0: #Will check if value is greater than or equal to 0.
            self.__weekly_salary = weekly_salary
        else:
            raise ValueError("Weekly salary must be greater than or equal to zero.")
    def __repr__(self):
        return ('Salaried, ' + super().__repr__() + f', Weekly Salary: {self.__weekly_salary}')
    
class HourlyEmployee(Employee):
    def __init__(self, first_name=None, last_name=None, social_security=None,#continues on next line
                 hourly_wage=None, work_week_hours=None, weekly_earnings=None): #end
        """Initializes an HourlyEmployee object.
        
        >>> person2 = HourlyEmployee("Jesus", "Martinez", 1234567, 15, 45)
        >>> person2.last_name
        'Martinez'
        >>> person2.earnings
        'Earnings: 712.5'
        >>> person2.wage = -10
        Traceback (most recent call last):
        ...
        ValueError: Wage must be greater than 0.
        >>> person2.hours = 200
        Traceback (most recent call last):
        ...
        ValueError: Please enter weekly hours between the range 0-168.
        """
        
        super().__init__(first_name, last_name, social_security)
        self.__hourly_wage = hourly_wage
        self.__work_week_hours = work_week_hours
        self.__weekly_earnings = weekly_earnings
        
    @property
    def wage(self):
        return self.__hourly_wage
    @wage.setter
    def wage(self, wage):
        if wage < 0: #Will check if wage is less than 0 and return an error.
            raise ValueError("Wage must be greater than 0.")
        self.__hourly_wage = wage
    
    @property
    def hours(self):
        return self.__work_week_hours
    @hours.setter
    def hours(self, hours):
        if hours > 0 and hours < 168: #Will check if hours are between 0 and 168
            self.__work_week_hours = hours
        else:
            raise ValueError("Please enter weekly hours between the range 0-168.")
        
    @property
    def earnings(self):
        if self.__work_week_hours > 40: #will calculate regular and overtime pay.
            forty_hours = self.__hourly_wage * 40
            overtime = (self.__work_week_hours - 40) * (self.__hourly_wage * 1.5)
            self.__weekly_earnings = forty_hours + overtime
        elif self.__work_week_hours <= 40:
            self.__weekly_earnings = self.__work_week_hours * self.__hourly_wage
        return f'Earnings: {self.__weekly_earnings}'
    def __repr__(self):
        if self.__weekly_earnings is None:
            self.earnings
        return ('Hourly, ' + super().__repr__() + f', Weekly Earnings: {self.__weekly_earnings}')

#Unit Testing 
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

#Assigning objects and iterating over them from a list called employees.
person1 = SalariedEmployee('Jesus', 'Martinez', 1234567, 1500)
person2 = HourlyEmployee('Bob', 'Builder', 7654321, 15, 45)
employees = [person1, person2]
for emp in employees:
    print(emp.__repr__())
    print(emp.earnings)