## o(n^2) -- a loop inside a loop
# O(n) -- a single loop
# O(1) -- constant time, no loops   
# 0(n^3) -- a loop inside a loop inside a loop

import time

def calculate_sum(n):
    sum =0
    for numb in range (1,n+1):
        print(f"sum ={sum} , numb={numb}")
        sum=sum+numb
    print(f"For {n} The sum is {sum}")
    return sum

start_time = time.time()
calculate_sum(50000)
end_time=time.time()
diff = end_time - start_time
print(f"Speed {diff}")
