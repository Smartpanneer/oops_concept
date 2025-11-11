class Student():
    def exam(self,mark):
        return f'The student scored in the exam {mark}/500'

obj=Student()
m=430
print(obj.exam(m))