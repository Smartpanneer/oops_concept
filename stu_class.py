class College:
   def result(self,m,c,p):
        maths=m
        chemistry=c/2
        physics=p/2
        mark=maths+chemistry+physics
        return f'The student 12th cut off mark is  {mark}'

stu_1=College()
stu_2=College()
print(stu_1.result(100,100,100))
print(stu_2.result(78,62,79))