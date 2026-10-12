# Week 1.3, Session 1: Task 3b

fruit = ['apple','pear','banana','orange']

while fruit:
	current_fruit = fruit.pop()

	if current_fruit == "apple":
		print(f"{current_fruit} is my favourite!")
	else:
		print(current_fruit) 

else:
	print("The list is now empty.")


# Add an else clause with a message that the list is now empty