"""
LeetCode #36. Valid Sudoku

Pattern:
    Arrays & Hashing
    Hash Set
    Membership Checking

Difficulty:
    Medium

Hash Set:
    Row Set
    Column Set
    Box Set

Use Cases:
    • Spreadsheet Validation:
        Detect duplicate values within rows or columns.

    • Database Validation:
        Ensure unique values inside constrained groups.

    • Form Validation:
        Check uniqueness of user inputs before submission.

    • Constraint Satisfaction Problems:
        Validate partially completed puzzles and schedules.

    • Data Integrity:
        Verify uniqueness constraints across multiple dimensions.

Key Idea:
    Instead of counting frequencies,
    simply check whether a digit has already been seen.

    Every digit must be unique within:
        1. Its Row
        2. Its Column
        3. Its 3×3 Box
"""

from typing import List


# ==========================================================
# Solution
# ==========================================================


class Solution:
    """
    Hash Set Solution

    Time Complexity:
        O(81) = O(1)

    Space Complexity:
        O(81) = O(1)
    """
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                value = board[row][col] 
                
                if value == ".":
                    continue
                
                box = (row // 3)*3 + (col // 3)
                
                if (value in rows[row] or value in cols[col] or value in boxes[box]):
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                boxes[box].add(value)
        
        return True


# ==========================================================
# Test Case
# ==========================================================

if __name__ == "__main__":

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solution = Solution()

    print(solution.isValidSudoku(board))
    

# ==========================================================
# Complexity Analysis
# ==========================================================

"""
Time Complexity

    O(81)

    We visit every cell exactly once.

    Since the Sudoku board size is fixed (9×9),
    this is considered O(1).

Space Complexity

    O(81)

    Three collections of sets are maintained
    for rows, columns, and boxes.

    Since their maximum size is fixed,
    this is also O(1).

Key Takeaways

1.
    Use Hash Sets when checking whether
    an element has already been seen.

2.
    Ignore '.' because empty cells
    cannot violate Sudoku rules.

3.
    Every digit must be unique within:
        • Row
        • Column
        • 3×3 Box

4.
    The current box is identified by

        (row // 3) * 3 + (col // 3)

5.
    Return False immediately when any
    duplicate is detected.

6.
    If the entire board is scanned
    without violations,
    return True.
"""