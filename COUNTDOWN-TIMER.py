# Countdown timer that counts down from a specified number of seconds and prints the remaining time at each second.

import time

my_time = int(input("Enter the time in seconds for countdown: "))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = seconds//60
    hours = minutes//60
    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
    time.sleep(1)


print('Time up')    

# Example :
# Input: 3 
# Output:
# 00:00:03
# 00:00:02  
# 00:00:01
# Time up



