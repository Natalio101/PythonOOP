from datetime import date, datetime
class School:
    def __init__(self,f_name,l_name,nationality, gender,birthdate):
        self.f_name = f_name
        self.l_name = l_name
        self.nationality = nationality
        self.gender = gender
        self.birthdate = birthdate
    def Full_Name(self):
        return self.f_name + " " + self.l_name
    def Email(self):
        return self.f_name[0] + self.l_name + "@bpsma.org"
    def Age(self):
        today = date.today()
        #YY,MM,DD
        age = today.year - self.birthdate.year - ((today.month, today.day)<(self.birthdate.month, self.birthdate.day))
        return f"You are: {age}"
    
class Teachers(School):
   
    raise_amount = 1.05
    def __init__(self,f_name,l_name,nationality, gender,birthdate,salary):
        super().__init__(f_name,l_name,nationality, gender,birthdate)
        self.salary = salary
    def Apply_Raise(cls):
        return cls.salary * cls.raise_amount

class Students(School):
    
    def __init__(self,f_name,l_name,nationality, gender,birthdate,grades):
        super().__init__(f_name,l_name,nationality, gender,birthdate)
        self.grades = grades
    def Get_GPA(cls):
        return sum(cls.grades)/len(cls.grades)
        
#Teachers
teacher_1 = Teachers('Mary','Jane','Portuguese','F',date(1986,3,21),20000)


#Students
student_1 = Students('John','Copnstantine','French','M',date(1998,9,20),[20,10,14,90])


print(student_1.Full_Name())