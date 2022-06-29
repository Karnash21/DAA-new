# importing the module
import timeit


# sample function that returns
# square of the value passed
def print_square(x):
	print(x**2)

# records the time at this instant
# of the program
start = timeit.default_timer()

# calls the function
print_square(int(input("x: ")))

# records the time at this instant
# of the program
end = timeit.default_timer()

# printing the execution time by subtracting
# the time before the function from
# the time after the function
print(end-start)
