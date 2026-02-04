class solution:
    def runningSum(self, nums):
        result = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            result.append(curr_sum)

            return result