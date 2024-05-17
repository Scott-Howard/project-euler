#generate fibonacci numbers
#start with 1 and 2 and the add the previous 2 elements
# fib = [1,2]
# print(fib)
# fib.append(3)
# print(fib)
# fib.append(fib[-1]+fib[-2])
# print(fib)

fib = [1,2]
even_sum = []
while (fib[-1])<4000000:
    print(fib[-1])
    if fib[-1]%2==0:
        a = fib[-1]
        print(a)
        even_sum.append(a)
    fib.append(fib[-1]+fib[-2])  
  
print(fib)   
print(sum(even_sum))     