# Conner Radle
# 11/5/24
# U3L4
# binary or not to binary, a binary love story
# ʕ •ᴥ•ʔ the good luck bear
# 𓅭 the good luck duck



def binary_search(num, nums):

  if len(nums) == 1:
    return
  # find mid index
  midind = nums[int(len(nums) / 2)]
  print(f"Middle Index: {midind}")
  #half1 = nums[0:int(len(nums) / 2)]
  #half2 = nums[int(len(nums) / 2):]
  #print(f"left: {half1}\nright: {half2}\n")
  
  if midind == num:
    return midind

  elif midind < num:
    print(f"Searching: {nums[int(len(nums) / 2):]}")
    binary_search(num, nums[int(len(nums) / 2):])
    

  elif midind > num:
    binary_search(num, nums[0:int(len(nums) / 2)])
    print(f"Searching: {nums[0:int(len(nums) / 2)]}")
  

  







def main():
    nums = [1,2,3,4,5,6,7,8,9]

    test1 = binary_search(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binary_search(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binary_search(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")
    
    test4 = binary_search(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
    main()