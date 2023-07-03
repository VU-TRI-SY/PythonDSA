def wins_rock_scissors_paper(opt1: str, opt2: str) -> bool:
    player = opt1.lower()
    opponent = opt2.lower()
    if player == opponent:
        return False
    elif player == "rock":
        if opponent == "scissors":
            return True
        else:
            return False
    elif player == "scissors":
        if opponent == "paper":
            return True
        else:
            return False
    elif player == "paper":
        if opponent == "rock":
            return True
        else:
            return False
    else:
        return False
    
def factorial(n: int)->int:
    # res = 1
    # for i in range(1, n+1):
    #     res *= i
    # return res
    #-----------------------------------------
    # if n == 1:
    #     return 1
    # return n*factorial(n-1)
    #-----------------------------------------
    res = 1
    while n > 0:
        res *= n
        n -= 1
        #n--: error
    return res

# print(factorial(5))

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_to_goal(numbers : list, goal : int)->int:
    for i in range(len(numbers)):
        if (goal-numbers[i]) in numbers: #O(n)
            return numbers[i] * (goal-numbers[i])
    return 0

# assume: a + b = goal 
# numbers[i] = a => b = goal - numbers[i] ===> check b is in list or not
print(sum_to_goal([1,3,6,8,9,0,4,7], 11))

def function3(list): #bubble sort
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp


