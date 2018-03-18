num = int(input('How many numbers: '))
total_sum = 0
for i in range(num):
numbers = float(input('Enter number : '))
total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
