#!/usr/bin/env python3

def get_order():
	print("[command] [item] (command is 'a' to add, 'd' to delete, 'q' to quit")
	line = input()
	
	command = line[:1]
	item = line[2:]

	return command, item

def add_to_cart(item, cart):
	if not item in cart:
		cart[item] = 0
	cart[item]+= 1

def delete_from_cart(item, cart):
	if item in cart:
		cart[item] -= 1
		if cart[item] <= 0: # This removes the dict entry if its empty
			 del cart[item]
	
def process_order(order, cart):
	command, item = order

	if command	== "a":
		add_to_cart(item, cart)
	elif command == "d":
		delete_from_cart(item, cart)
	elif command == "q":
		return False

	return True

# main function
def go_shopping():
	cart = dict() # stores it in a dictionary

	while True:
		order = get_order()
		if not process_order(order, cart):
			break

	print(cart)
	print("All done!")

go_shopping()