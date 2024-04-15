"""If we list all the natural numbers below 
 that are multiples of 3 or 5
, we get 3 and 5, 6, 9. The sum of these multiples is 
23.

Find the sum of all the multiples of 3 and 5
 below 1000. """

#improvements
#build a function to take multiples of any value
#include documentation
#build a test for this function

n=15
multiple_list = []
for number in range(1,n):
    if number%3==0:
        multiple_list.append(number)
    elif number%5==0:
        multiple_list.append(number)
print(multiple_list)
print(sum(multiple_list))