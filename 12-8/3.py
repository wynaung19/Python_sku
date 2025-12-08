from datetime import date

class Person:
    name = ""
    birthYear = 0
    birthDay = 0
    birthMonth = 0
    
    count = 0

    def __init__(self):
        self.name = "UNKNOWN"
        Person.count += 1
    def getAge(self):
        today = date.today()
        current_year = today.year
        current_month = today.month
        current_day = today.day
        
        age = current_year - self.birthYear
        if current_month < self.birthMonth:
            age -= 1
        elif current_month == self.birthMonth:
            if current_day < self.birthDay:
                age -= 1
                
        return age


p = Person()
p.name = "WaiYanNaung"
p.birthYear = 2003
p.birthDay = 4
p.birthMonth = 4

print(p.name,"is",p.getAge(),"years old")

print("Total :",Person.count)
