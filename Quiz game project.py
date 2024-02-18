print("****************************************")
print("Welcome to My Quiz Game")

Question_bank=[
 {"text":"The ability of one class to acquire methods and attributes from another class is called.","answer":"A"},
 {"text":"Who developed python","answer":"B"},
 {"text":"Which of the following is not a data type of python","answer":"B"},
 {"text":"What does mro stands for","answer":"A"},
 {"text":"Which of the following is not a OOPS concept","answer":"C"}
]

options=[["A. Inheritance","B. Abstraction","C. Encapsulation","D. Polymorphism"],
         ["A. Dennis Ritchie","B. Guido Von Rossum","C. James Gosling","D. Von Neumann"],
         ["A. bool","B. char","C. int","D. tuple"],
         ["A. Method Resolution Order","B. Method Recursive Object","C. Main Resolution Order","D. Method Resolution Object"],
         ["A. Class","B. Object","C. Function","D. Inheritance"]
]  

score=0
def check_answer(user_guess,correct_answer):
 if user_guess==correct_answer:
  return True
 else:
  return False

for question_num in range(len(Question_bank)):
 print("***************************************")
 print(Question_bank[question_num]["text"])
 
 for i in options[question_num]:
  print(i)

 guess=input("Enter your answer(A/B/C/D): ").upper()
 is_correct=check_answer(guess,Question_bank[question_num]["answer"])
 if is_correct:
  print("Correct answer")
  score += 1
 else:
  print("Incorrect answer")
  print(f"Correct answer is {Question_bank[question_num]["answer"]}")
 print(f"Your current score is {score}/{question_num+1}")
print(f"Your final score is {score}")
 


