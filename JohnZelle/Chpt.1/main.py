#!/usr/bin/python3
# File: chaos
# A Simple program illustrating a chaotic function

def main():
	print("This program illustrates a chatic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)
