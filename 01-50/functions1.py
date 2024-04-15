
def multiples_3_5( n):
    """
    n is an integer and upper bound of the list to check
    for multiples of 3 and 5
    """
    holding = []
    for number in range(1,n):
        if number%3==0:
            holding.append(number)
        elif number%5==0:
            holding.append(number)
    return(sum(holding))    
    


if __name__ == "__main__":
    print("Test")

    print(multiples_3_5(1000))