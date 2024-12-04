def increasing(nums):
    check = 0
    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] >= 0 or nums[i] - nums[i+1] < -3:
            
            print(nums[0:i+1] + nums[i+2:])
            check += safe_increasing(nums[0:i+1] + nums[i+2:])
            if check > 1:
                return 0
             
    return 1

def safe_increasing(nums):
    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] < -3 or nums[i] - nums[i+1] >= 0:
            return 2
    return 1

    


def decreasing(nums):
    check = 0
    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] <= 0 or nums[i] - nums[i+1] > 3:
            
            print(nums[0:i+1] + nums[i+2:])
            check += safe_decreasing(nums[0:i+1] + nums[i+2:])
            if check > 1:
                return 0
    return 1

def safe_decreasing(nums):
    for i in range(len(nums)-1):
        if nums[i] - nums[i+1] > 3 or nums[i] - nums[i+1] <= 0:
            return 2
    return 1

with open("inputd2.txt", 'r') as f:
    safe = 0
    for line in f:
        level = []
        report = line.split()
        for r in report:
            level.append(int(r))

        if level[0] > level[1]:
            safe += decreasing(level)
        elif level[0] < level[1]:
            safe += increasing(level)
        else:
            continue
    
    print(safe)
        
