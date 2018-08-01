class Student():
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def marks_avg(self):
		return (sum(self.marks)/len(self.marks))

anna = Student("Anna", "MIT")
anna.marks.append(23)
anna.marks.append(45)
avg_marks = anna.marks_avg()
print(avg_marks)

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        my_dict = {"name":name,"price":price}
        self.items.append(my_dict)

    def stock_price(self):
    	total = 0
        for item in self.items:
        	total = total + item["price"]
        return total

'''
For more information on class and static methods use the following link
https://www.geeksforgeeks.org/class-method-vs-static-method-python/
''