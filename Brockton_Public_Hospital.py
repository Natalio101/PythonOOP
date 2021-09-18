from datetime import date
class Hospital:
    def __init__(self,f_name,l_name,birthdate,address):
        self.f_name = f_name
        self.l_name = l_name
        self.birthdate = birthdate
        self.address = address
    
    def Email(self):
        return self.f_name[0] + "." + self.l_name + "@bphospital.gov"
    
    def Age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month,today.day)<(self.birthdate.month, self.birthdate.day))
    def Full_name(self):
        return self.f_name + " " + self.l_name
class Doctor(Hospital):
    pay_raise = 1.10
    def __init__(self,f_name,l_name,birthdate,address,Salary, Field,patients = None):
        super().__init__(f_name,l_name,birthdate,address)
        self.Salary = Salary
        self.Field = Field
        if patients is None:
            self.patients = []
        else:
            self.patients = patients
    def Add_Patient(self,patient):
        if patient not in self.patients:
            self.patients.append(patient)
    
    def Remove_Patient(self,patient):
        if patient in self.patients:
            self.patients.remove(patient)
    
    def Print_Patient(self):
        for i in self.patients:
            print(i.Full_name())

    def Apply_Raise(self):
        return self.Salary * self.pay_raise
    @classmethod
    def Set_Raise(cls,amount):
        cls.pay_raise = amount

class Patient(Hospital):
    def __init__(self,f_name,l_name,birthdate,address,Condition, Insurance):
        super().__init__(f_name,l_name,birthdate,address)
        self.Condition = Condition
        self.Insurance = Insurance

patient_1 = Patient('Ana','Amado',date(1998,5,5),'367 ulm ave','Flu','Masshealth')
patient_2 = Patient('Maria','Amado',date(1988,5,5),'367 ulm ave','Covid-19','MassHealth')

doctor_1=  Doctor('Bella','Amado',date(1978,5,5),'767 alm st',700000,'Neurologist',[patient_1,patient_2])
doctor_1.Set_Raise(1.3)

print(doctor_1.Print_Patient())