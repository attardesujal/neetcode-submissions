class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list=[]
        for i in nums:
            product=1
            for j in nums:
                if i==j:
                    pass
                else:
                    product *= j
            product_list.append(product)

        return product_list