class Student:
    def __init__(self, _name, _age, _department, _university):
        self.name = _name
        self.age = _age
        self.department = _department
        self.university = _university
    def print(self):
        print("이름:", self.name, 
              ", 나이:", self.age, 
              ", 학과:", self.department, 
              ", 학교:", self.university)
    def __str__(self):
        return "이름:"+self.name+", 나이:"+str(self.age)+", 학과:"+self.department + ", 학교:"+self.university
    
# Student() -> 객체
students = []
students.append(Student("chansoo", 25, "지능형", "전남대"))
students.append(Student("jinsoo", 21, "인공지능", "충남대"))
students.append(Student("hansoo", 30, "빅데이터", "경북대"))

for i in students:
    print (i)