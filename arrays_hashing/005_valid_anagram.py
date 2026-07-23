"""
LeetCode #242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Pattern:
    Arrays & Hashing

Difficulty:
    Easy

Time Complexity:
    Sorting Solution:
        O(n log n)

    Two Hash Maps:
        O(n)

    One Hash Map:
        O(n)

Space Complexity:
    Sorting Solution:
        O(n)

    Two Hash Maps:
        O(n)

    One Hash Map:
        O(n)

Pattern Recognition:
    ✓ Need to compare frequencies?
        → Hash Map

    ✓ Same characters with same counts?
        → Frequency Counting

    ✓ Compare two collections efficiently?
        → Increment / Decrement Technique

Use Cases:
    • Spell Checkers:
        Detect anagrams for word games.

    • Search Systems:
        Match rearranged search queries.

    • Puzzle Applications:
        Validate scrambled word solutions.

    • Language Learning:
        Generate anagram exercises.

Key Idea:
    Two strings are anagrams if they contain exactly the same
    characters with the same frequencies, regardless of order.
    
"""


# ==========================================================
# Sorting Solution
# ==========================================================


def is_anagram_sorting(s:str, t:str)-> bool:
    """
    Sort both strings and compare them.
    """
    return sorted(s) == sorted(t)


# ==========================================================
# Two Hash Maps Solution
# ==========================================================

def is_anagram_two_hashmaps(s:str, t:str) -> bool:
    """
    Count character frequencies in both strings,
    then compare the dictionaries.
    """
    if len(s) != len(t):
        return False 
    
    frequency_s = {}
    frequency_t = {}
    
    for char in s: 
        frequency_s[char] = frequency_s.get(char, 0) + 1
    
    for char in t:
        frequency_t[char] = frequency_t.get(char, 0) + 1
        
    return frequency_s == frequency_t



# ==========================================================
# One Hash Map Solution(Optimized)
# ==========================================================


class Solution:
    """
    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False 
        
        frequency: dict[str, int] = {}
        
        # increment count from s
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        
        # decrement count from t
        for char in t: 
            frequency[char] = frequency.get(char, 0) -1 
        
        for count in frequency.values():
            if count != 0:
                return False 
        
        return True


# ==========================================================
# Test Cases
# ==========================================================


if __name__ == "__main__":

    s = "anagram"
    t = "nagaram"

    print("=== Sorting Solution ===")
    print(is_anagram_sorting(s, t))

    print()

    print("=== Two Hash Maps Solution ===")
    print(is_anagram_two_hashmaps(s, t))

    print()

    print("=== One Hash Map Solution ===")
    solution = Solution()
    print(solution.isAnagram(s, t))
    

""" 

NOTE: Key Takeaways
- An anagram depends on frequency, not character order.
- Always check the lengths first. If they're different, return False immediately.
- Sorting is simple but costs O(n log n).
- Hash maps allow frequency counting in linear time.
- A single hash map can act like a balance sheet:
    - Increment for the first string.
    - Decrement for the second string.
    - Every count should end at zero.
- Pattern Recognition:
        Need character frequencies?
                ↓
        Hash Map

        Need to compare two collections?
                ↓
        Frequency Counting

        Need to balance two datasets?
                ↓
        Increment / Decrement

"""