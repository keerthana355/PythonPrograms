         #Program-1
#Python program to create class and object
class Instructor:
 pass
Instructor_1=Instructor()
Instructor.name="Rama"
Instructor.age="37"
print(Instructor.name)
print(Instructor.age)

         #Program-2
#Python program to illustrate __init__ and self in a class
class Instructor:
   def __init__(self,name,address):
     self.name=name
     self.address=address
Instructor_1=Instructor("Ram","Delhi")
print(Instructor_1.name,Instructor_1.address)
Instructor_2=Instructor("sita","Pune")
print(Instructor_2.name,Instructor_2.address)

         #Program-3
#Python program to illustrate adding methods to class
class Instructor:
   def __init__(self,name,address):
     self.name=name
     self.address=address
   def display(self,course):
     print(f"hi! {self.name}is learning {course}")
Instructor_1=Instructor("Ram","Delhi")
print(Instructor_1.name,Instructor_1.address)
Instructor_1.display("Python")

         #Program-4
#Python program to calculate the area and circumference of circle
class circle:
 pi=3.14            #class object attribute
 def __init__(self,radius):
  self.radius=radius
 def circumference(self):
  return 2*circle.pi*self.radius
 def area(self):
  return circle.pi*self.radius*self.radius
circle_1=circle(6)
print(circle_1.radius)
print(circle_1.circumference())
print(circle_1.area())

        #Program-5
#Python program to calculate the area of rectangle
class rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
rectangle_1=rectangle(3,9)
print(rectangle_1.area())

   