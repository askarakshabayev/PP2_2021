import os
def read():
    currentPath = os.getcwd()
    print(currentPath)
    # os.path.join(path_to_folder1, path_to_folder2)
    with open(os.path.join(currentPath, 'folder1/input.txt'), 'r') as file:
        line = file.readline()
        nums = line.split(' ')
        print(nums)
        numSum = 0
        for num in nums:
            numSum += int(num)
        return numSum


sum = read()
print(sum)