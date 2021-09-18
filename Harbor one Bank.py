from datetime import date
import datetime
class HOB:
    employee = 0
    raise_amount = 1.02
    def __init__(self,f_name,l_name,birthdate,salary):
        self.f_name = f_name
        self.l_name = l_name
        self.birthdate = birthdate
        self.salary = salary
        HOB.employee+=1
    def Email(self,website):
        self.website = website
        return self.f_name + self.l_name + "@"+self.website
    
    def Age(self):
        today = date.today()
        age = today.year-self.birthdate.year -((today.month,today.day)<(self.birthdate.month,self.birthdate.day))
        return age
    def Apply_Raise(self):
        new_payment = self.salary * self.raise_amount
        return new_payment
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    classmethod
    def from_string(cls, str_emp):
        f_name, l_name, birthdate, payment = str_emp.split("-")
        return cls(f_name, l_name, birthdate, payment)
    @staticmethod
    def Workday(day):
        if day.weekday() ==5 and day.weekday() == 6:
            return False
        return True


emp_1 = HOB("Natalio","Gomes",date(2003,12,24),100000)
emp_2 = HOB("Kevin","Antunes",date(2003,12,24),100800)
emp_3 = HOB("Edwin","Caldwell",date(2003,12,24),100050)
emp_4 = HOB("Mary","Teixeira",date(2003,12,24),100030)
emp_5 = HOB("Jane","Fernandes",date(2003,12,24),100100)
emp_6 = HOB("Jhon","Pina",date(2003,12,24),100010)
emp_7 = HOB("Imelda","Mel",date(2003,12,24),100020)
emp_8 = HOB("Maria","Alves",date(2003,12,24),100600)
emp_9 = HOB("Loreta","KBA",date(2003,12,24),109000)
emp_10 = HOB("Key","SIA",date(2003,12,24),100209)
emp_11= HOB("Flavio","Cardoso",date(2003,12,24),192000)

HOB.set_raise_amt(1.03)
print(emp_1.Apply_Raise())

now = datetime.date(2021,7,21)
print(HOB.Workday(now))