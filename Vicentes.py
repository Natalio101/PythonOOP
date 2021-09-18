from datetime  import date
class Vicentes:
    members = 0
    raise_amount = 1.04
    def __init__(self, f_name, l_name, BirthDate, pay):
        self.f_name = f_name
        self.l_name = l_name
        self.BirthDate = BirthDate
        self.pay = pay
        Vicentes.members +=1
    def Full_Name(self):
        return self.f_name + " " + self.l_name
    def email(self):
        email = self.f_name[0] + self.l_name+ "@Vicentes.com"
        return email
    def age(self):
        today = date.today()
        age = today.year - self.BirthDate.year -((today.month,today.day)<(self.BirthDate.month, self.BirthDate.day))
        return age
    def apply_raise(self):
        payment = self.pay = float(self.pay * self.raise_amount)
        return payment
    @classmethod
    def Set_Raise_Amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,dob,payment = emp_str.split('-')
        return cls(first,last,dob,payment)
class Employee(Vicentes):
    Emp_raise = 1.15
    def __init__(self, f_name, l_name, BirthDate, pay,Job_Desciprtion):
        super().__init__( f_name, l_name, BirthDate, pay)
        self.Job_Desciprtion = Job_Desciprtion
    def Raise_Apply(self):
        return self.pay * self.Emp_raise
class Manager(Vicentes):
    mng_raise = 1.20
    def __init__(self, f_name, l_name, BirthDate, pay,Job_Desciprtion):
        super().__init__( f_name, l_name, BirthDate, pay)
        self.Job_Desciprtion = Job_Desciprtion
    def MnGRaise_Apply(self):
        return self.pay * self.mng_raise
emp1 = Vicentes("Natalio","Gomes",date(2002,12,24),30000)

emp = 'Natalio-Gomes-2003,09,09-40000'
#
new_emp = Vicentes.from_string(emp)
emp_1 = Employee("Natalio","Gomes",date(2002,12,24),30000,"Cashier")
manager_1 = Manager("Kevin","Alves",date(1980,12,24),30000,"Mnager")
print(manager_1.Full_Name())