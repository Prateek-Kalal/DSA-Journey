def bubble_sort(nums):
    for p in range(1,len(nums)):
        for i in range(0,len(nums)-p):
            if nums[i]>=nums[i+1]:
                temp=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
            else:
                pass
    print(nums)
nums1=[5,7,8,4,1,6,9,2]
bubble_sort(nums1)
