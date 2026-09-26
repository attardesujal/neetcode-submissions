class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the output array with 1s
        output = [1] * n
        
        # Step 1: Calculate prefix products (going Left to Right) -> O(N)
        # output[i] will store the product of all elements before index i
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Multiply by suffix products (going Right to Left) -> O(N)
        # Multiply output[i] by the product of all elements after index i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output