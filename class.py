class Demo:
      pers_rise=1.5
      def __init__(self,f,l,marks):       #pass
       self.f=f;
       self.l=l;
       self.marks=marks
       self.email=f+l+"@gmail.com"

      def fullname(self):
       return '{} {}'.format(self.f, self.l)
      def apply_raise(self):
       mar= self.marks = int(self.marks*1.05)
       return mar
class  Dumb (Demo):
  def __init__(self,f,l,marks,prog_lan):
     super().__init__(f,l,marks)
     self.prog_lan=prog_lan
std1=Dumb('divya','Jain',89,'Python')
print(std1.pers_rise)
print(std1.prog_lan)
std2=Demo('divy','jain',79)
#std1.f='Divyajain'
#std1.l='Jain'
#std1.marks=88
#std2.f='Divy'
#std2.l='Jain'
#std2.marks=68
print(help(Dumb))

print(std2.email)
print(std1.email)
print(std1.fullname())
print(std2.fullname())
print(std1.apply_raise())
print(std1.__dict__)
print(std2.__dict__)
print(std1.pers_rise)

