"""
LeetCode #347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

Pattern:
    Arrays & Hashing

Difficulty:
    Medium

Time Complexity:
    Brute Force:
        O(n log n)

    Bucket Sort:
        O(n)

Space Complexity:
    Brute Force:
        O(n)

    Bucket Sort:
        O(n)

Key Idea:
    1. Count the frequency of every number using a hash map.
    2. Instead of sorting the frequencies, place each number into a bucket (list of list)
       corresponding to its frequency.
    3. Traverse the buckets from highest frequency to lowest until k elements
       have been collected.
"""

from typing import List

nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]
k = 2

frequency: dict[int, int] = {}

for num in nums:
    if num in frequency:
        frequency[num] = frequency[num] + 1
        
    else:
        frequency[num] = 0 + 1


print(frequency)
print(frequency.items())
print(frequency.keys())
print(frequency.values())


# ==========================================================
# Brute Force Solution
# ==========================================================


def top_k_frequent_brute_force(nums: List[int], k: int) -> List[int]:
    """
    Count frequencies using a hash map,
    then sort the frequency map in descending order.
    """
    frequency: dict[int, int] = {}
    
    for num in nums: 
        frequency[num] = frequency.get(num, 0) + 1
    
    sorted_frequency = sorted(
        frequency.items(),
        key = lambda item: item[1],
        reverse = True
    )
    
    result = []
    
    for number, _ in sorted_frequency[:k]:
        result.append(number)
    
    return result


class Solution:
    """
    Bucket Sort Solution

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequencies
        frequency: dict[int, int] = {}
        
        for num in nums: 
            frequency[num] = frequency.get(num, 0) + 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Place numbers into buckets
        for number, count in frequency.items():
            buckets[count].append(number)
        
        # Step 4: Collect top k frequent elements
        result = []
        
        for count in range(len(buckets)-1, 0, -1):
            for number in buckets[count]:
                result.append(number)
            
                if len(result) == k:
                    return result


# ==========================================================
# Test Cases
# ==========================================================

if __name__ == "__main__":
    
    print("=== Brute Force Solution ===")
    print(top_k_frequent_brute_force(nums, k))
    
    print()
    
    print("=== Bucket Sort Solution ===")
    solution = Solution()
    print(solution.topKFrequent(nums, k))
    

"""
NOTE: Key Takeaways:
- A Hash Map is the best choice for counting frequencies.
- Sorting solves the problem but costs O(n log n).
- The maximum possible frequency is n, allowing us to create n + 1 buckets.
- Bucket Sort groups numbers by frequency instead of sorting them.
- Traversing buckets from highest frequency to lowest gives the answer in O(n).
"""