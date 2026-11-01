def insertion_sort(nums):
    sorted=0
    while sorted<len(nums)-1:
        j=sorted+1
        if nums[j]<=nums[sorted]:
            for k in range(sorted,-1,-1):
                if nums[j]<=nums[k]:
                    nums[j],nums[k]=nums[k],nums[j]
                else:
                    pass
                j-=1
            sorted+=1
        else:
            sorted+=1
    print(nums)
nums1=[5,7,8,4,1,6,9,2]
insertion_sort(nums1)

"""Note:- For more optimal solution instead of swapping we can shift the element to the
          the find the right position."""
#Optimal Solution:-
def insertion_sort_optimal(nums):
    i=1
    while i<=len(nums)-1:
        if nums[i]< nums[i-1]:
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        i+=1
    print(nums)
nums2=[5,7,8,4,1,6,9,2]
insertion_sort_optimal(nums2)
   