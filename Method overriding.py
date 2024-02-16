class human:
 def eat(self):
  print("I can eat")
 def work(self):
  print("I can work")

class male(human):
 def lift(self):
  print("I can lift")
 def work(self):    #overridden method
  print("I can code")

male_1=male()
male_1.work()

human_1=human()
human_1.work()