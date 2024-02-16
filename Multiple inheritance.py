# Python example to show the working of multiple inheritance
class human:
 def __init__(self,heart):
  self.eyes=2
  self.nose=1
  self.heart=heart
 def eat(self):
  print("I can eat")
 def work(self):
  print("I can work")
 
class male:
 def __init__(self,name):
  self.name=name
 def lift(self):
  print("I can lift")
 def work(self):
  print("I can code")

class boy(human,male):
 def __init__(self,name,heart,language):
  self.language=language
  human.__init__(self,heart)
  male.__init__(self,name)
 def work(self):
  print("I can test")
 def display(self):
  print(f"I work on {self.language}")
boy_1=boy("Ram",1,"python")

boy_1.work()
male.work(boy_1)
human.eat(boy_1)
print(boy.mro())
print(boy_1.nose)
print(boy_1.eyes)
print(boy_1.name)
print(boy_1.heart)
print(boy_1.language)
boy_1.display()