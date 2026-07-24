
"""
LeetCode #238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

Pattern:
    Arrays & Hashing
    Prefix Product
    Suffix Product

Difficulty:
    Medium

Hash Map:
    Not Required

Use Cases:
    • Financial Analysis:
        Compute portfolio values excluding one asset.

    • Statistics:
        Calculate aggregate metrics while excluding the current observation.

    • Machine Learning:
        Leave-one-out computations during feature engineering.

    • Data Processing:
        Compute cumulative products while omitting the current element.

    • Distributed Systems:
        Aggregate contributions from all nodes except the current node.

Key Idea:
    Instead of computing the total product and using division,
    compute:

        Left Product × Right Product

    for every index.

    Pass 1:
        Store prefix (left) products.

    Pass 2:
        Multiply by suffix (right) products.

"""


from typing import List


# ==========================================================
# Brute Force Solution
# ==========================================================


def product_except_self_brute_force(nums: List[int]) -> List[int]:
    """
    Multiply every element except itself.

    Time Complexity:
        O(n²)

    Space Complexity:
        O(1)
    """
    result = []
    
    for i in range(len(nums)):
        
        product = 1 
        
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        
        result.append(product)
    
    return result


# ==========================================================
# Optimal Prefix + Suffix Solution
# ==========================================================

class Solution:
    """
    Prefix + Suffix Product

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)
        (excluding the output array)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [1]*n 
        
        # ---------------------------------------------
        # Prefix Products
        # ---------------------------------------------
        
        prefix = 1
        for i in range(n):
            result[i] = prefix 
            prefix *= nums[i]
        
        # ---------------------------------------------
        # Suffix Products
        # ---------------------------------------------  
        
        suffix = 1 
        for i in range(n-1, -1, -1):
            result[i] *= suffix 
            suffix *= nums[i]
            
        return result
    

# ==========================================================
# Test Cases
# ==========================================================

if __name__ == "__main__":

    nums = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]

    print("=== Brute Force ===")
    print(product_except_self_brute_force(nums))
    print(product_except_self_brute_force(nums2))


    print()

    print("=== Optimal ===")
    solution = Solution()
    print(solution.productExceptSelf(nums))
    print(solution.productExceptSelf(nums2))

    print()

    nums = [-1, 1, 0, -3, 3]

    print("=== Edge Case ===")
    print(solution.productExceptSelf(nums))



# ==========================================================
# Complexity Analysis
# ==========================================================

"""
Brute Force

Time:
    O(n²)

Space:
    O(1)


Optimal

Time:
    O(n)

Space:
    O(1)
    (excluding output array)


Key Takeaways

1.
    Division is not reliable because arrays may contain zeros.

2.
    Prefix product = product of everything before the current index.

3.
    Suffix product = product of everything after the current index.

4.
    Final Answer

        Left Product × Right Product

5.
    The output array is reused to store prefix products first,
    then updated with suffix products.

6.
    This introduces the Prefix/Suffix Pattern,
    which appears frequently in Dynamic Programming,
    Prefix Sum, and many interval problems.
"""