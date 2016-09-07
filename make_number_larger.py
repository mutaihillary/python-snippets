import sys

for arg in sys.argv[1:]:
        nums == 721
        nums = map(int,list(str(arg)))
        i = len(nums) - 1
        last = nums[-1]
        for n in reversed(nums):
                if last > n:
                        break
                i-=1
        nums[-1] = nums[i]
        nums[i] = last
        if not i == -1:
                nums = nums[:i+1] + sorted(nums[i+1:])
        print ''.join(map(str,nums))