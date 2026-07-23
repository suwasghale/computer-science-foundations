"""
LeetCode #49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Pattern:
    Arrays & Hashing
    
# Hash Map
    # Key   -> Signature (Sorted String / Frequency Tuple)
    # Value -> List of Anagrams

Difficulty:
    Medium

Time Complexity:
    Sorting Signature:
        O(n × k log k)

    Frequency Tuple Signature:
        O(n × k)

Space Complexity:
    Sorting Signature:
        O(n × k)

    Frequency Tuple Signature:
        O(n × k)

Pattern Recognition:
    ✓ Need to group similar elements?
        → Hash Map

    ✓ Need identical representation?
        → Signature

    ✓ Need faster than sorting?
        → Frequency Tuple

Key Idea:
    Every anagram must generate the same signature.

    Examples:

        "eat" -> "aet"
        "tea" -> "aet"
        "ate" -> "aet"

    OR

        "eat" -> (1,0,0,0,1,...,1,...)
        "tea" -> (1,0,0,0,1,...,1,...)

    Once every word has the same signature,
    simply group them inside a hash map.
"""

from typing import List


# ==========================================================
# Sorting Signature Solution
# ==========================================================


def group_anagrams_sorting(strs: List[str]) -> List[List[str]]:
    """
    Generate a sorted string as the signature.
    """
    groups: dict[str, List[str]] = {}
    
    for word in strs: 
        signature = "".join(sorted(word))
        
        if signature not in groups: 
            groups[signature] = []
        groups[signature].append(word)
    
    return list(groups.values())


# ==========================================================
# Frequency Tuple Signature Solution (Optimized)
# ==========================================================

class Solution:
    """
    Time Complexity:
        O(n × k)

    Space Complexity:
        O(n × k)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups: dict[tuple, List[str]] = {}
        
        for word in strs:
            frequency = [0] * 26 
            
            for char in word: 
                frequency[ord(char)- ord("a")] += 1
            
            signature = tuple(frequency)
            
            if signature not in groups:
                groups[signature] = []
            
            groups[signature].append(word)
        
        return list(groups.values())


# ==========================================================
# Test Cases
# ==========================================================

if __name__ == "__main__":

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    words2 = ["saw", "listen", "lentis", "goman", "suwas", "wasus", "nap","mango", "pan", "sit", "silent", "its", "was", "nomag"]

    print("=== Sorting Signature ===")
    print(group_anagrams_sorting(words))
    print(group_anagrams_sorting(words2))

    print()

    print("=== Frequency Tuple Signature ===")
    solution = Solution()
    print(solution.groupAnagrams(words))
    print(solution.groupAnagrams(words2))


"""
NOTE: 
Key Takeaways

1. Grouping problems almost always suggest using a Hash Map.

2. Instead of comparing every word with every other word, create a signature.

3. A signature must be:

    - Identical for all anagrams.
    - Immutable (hashable).
    - Easy to generate.

4. Two popular signatures:

Sorted String

eat
↓
aet

or

Frequency Tuple
(1,0,0,0,1,...)

5. Dictionary keys cannot be:

list ❌
set ❌
dictionary ❌

because they are mutable.

6. A tuple is immutable.

Therefore

tuple
↓

Dictionary Key

7. Pattern Recognition

    Need to compare?

    ↓

    Signature

    Need grouping?

    ↓

    Hash Map

    Need faster signature?

    ↓

    Frequency Tuple

"""