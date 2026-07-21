"""
LeetCode #219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Pattern:
    Arrays & Hashing

Difficulty:
    Easy

Time Complexity:
    Brute Force: O(n²)
    Optimized: O(n)

Space Complexity:
    Brute Force: O(1)
    Optimized: O(n)

Key Idea:
    Unlike Contains Duplicate, we must also know where the previous
    occurrence appeared. Therefore, a Hash Map is required to store
    the latest index of each number.

"""

from typing import List


# ==========================================================
# Brute Force Solution
# ==========================================================

def contains_duplicate_ii_brute_force(nums: List[int], k:int)-> bool:
    """
    Compare every pair of elements.

    Time Complexity:
        O(n²)

    Space Complexity:
        O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            print(f"Comparing ({i}, {j}) -> ({nums[i]}, {nums[j]})")

            if nums[i] == nums[j]:
                print(f"Duplicate found at {i} and {j}")

                if j - i <= k:
                    print("Distance OK")
                    return True

    return False


# ==========================================================
# Test Cases
# ==========================================================


if __name__ == "__main__":

    nums1 = [1, 2, 3, 1]
    nums2 = [1, 0, 1, 1]
    nums3 = [1, 2, 3, 1, 2, 3]
    nums4 = [1, 2, 3, 1, 4, 1]

    k1 = 3
    k2 = 1
    k = 2

    print("=== Brute Force Solution ===")
    print(contains_duplicate_ii_brute_force(nums1, k1))
    print()
    print(contains_duplicate_ii_brute_force(nums2, k2))
    print()
    print(contains_duplicate_ii_brute_force(nums3, k))
    print()
    print(contains_duplicate_ii_brute_force(nums4, k))