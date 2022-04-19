my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

even = []
not_even = []
outlier = []

for i in my_list:
	if i > 90:
		outlier.append(i)
	elif i%2 == 0:
		even.append(i)
	else:
		not_even.append(i)

print('Even numbers ', even)
print('Odd numbers ', not_even)
print('outliers ', outlier)
print()


#sum of all numbers
num_sum = 0

for i in my_list:
	num_sum += i

print('Sum of the elements in the list ', num_sum)
print()


#sum of even numbers
even = []

for i in my_list:
	if i%2 == 0:
		even.append(i)

sum_num = 0

for i in even:
	sum_num += i

print('Sum of the even numbers ', sum_num)
print()


#counting even numbers in a list
count = 0

for i in range(len(my_list)):
	if my_list[i]%2 ==0:
		count += 1

print('Count of even numbers in the list ', count)
print()


#Cummulative sum of all elements
initial_val = 0
cumsum = []

for i in my_list:
	initial_val += i
	cumsum.append(initial_val)

print('Cummulative sums of the list ', cumsum)

