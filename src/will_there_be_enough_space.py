def enough(cap, on, wait):
    sum = on + wait
    if sum <= cap:
        return 0 
    if sum > cap:
        return sum - cap

print(enough(10,5,5))
