"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction- the ability to hide details we don't need. For example, someone doesn't need
to know if an attribute is an instance attribute or class attribute.
Polymorphism- the ability to make things interchangeable. For example, if you declare a
method in a parent class, you can easily call that same method on all instances of its
subclass with the same syntax.
Encapsulation - the ability to keep everything together. This allows you to group attributes
and methods all together so they're easily inherited all at once to each instance created

2. What is a class?

A class is a type of thing with certain attributes in common

3. What is an instance attribute?

An instance attribute is an attribute on an individual instance and does not come from
class or parent class(es). It is declared in the init process of an instane or with the
syntax self.attribute = attribute (Ex: cat.name = "Fluffy")

4. What is a method?

A method is like a function, but it is called on an instance of a class (or subclass).

5. What is an instance in object orientation?

An instance is an item declared of a class. An instance has all the attributes associated
with that class (and parent classes).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is inherited from the instance's class (or parent class). An instance
attribute is given to a specific instance. You would use a class attribute when that 
attribute is true for most or all of the class. You would use an instance attribute when
something is true for that specific instance and not the majority of the class.
Ex: In the Cat class: 
	class attribute: self.species = "cat"
	instance attribute: self.name = "Fluffy"

"""


# Parts 2 through 5:
# Create your classes and class methods
class Student(object):

	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.student_dictionary = {"first_name": self.first_name,
									"last_name": self.last_name, "address": self}

class Question(object):

	def __init__(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer
		self.question_dictionary = {"question": self.question, 
									"correct_answer": self.correct_answer}

	def ask_and_evaluate(self):
		print self.question
		user_answer = raw_input(" > ")
		if user_answer == self.question_dictionary["correct_answer"]:
			return True
		else:
			return False

class Exam(object):

	def __init__(self, name):
		self.name = name
		self.questions = []
		self.exam_dictionary = {"name": self.name, "questions": self.questions}

	def add_question(self, question, correct_answer):
		self.exam_questions = []
		self.added_question = Question(question, correct_answer)
		self.exam_questions.append(self.added_question)

	def administer(self):
		self.score = 0
		for question in self.exam_questions:
			if self.added_question.ask_and_evaluate() is True:
				self.score = self.score + 1
		# print self.score
		return self.score

def take_test(student, exam):
	self.administer()
	return student.first_name, student.last_name, "score is ", self.score

def example():
	exam = Exam('really hard math test')
	exam.add_question("What is 1 + 1?", "2")
	exam.add_question("What is 10 - 5?", "5")
	emily = Student("Emily", "Flagg", "Kingston Ave")
	exam.administer()

example()

class Quiz(Exam):

	def administer(self):
		self.score = 0
		for question in self.exam_questions:
			if self.added_question.ask_and_evaluate() is True:
				self.score = self.score + 1
		if self.score >= len(exam_questions)/2:
			return True
		elif self.score < len(exam_questions)/2:
			return False