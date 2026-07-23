"""
LeetCode #271. Encode and Decode Strings
(Premium)

Pattern:
    Arrays & Hashing
    String Serialization

Difficulty:
    Medium

Time Complexity:
    Encode:
        O(n)

    Decode:
        O(n)

Space Complexity:
    Encode:
        O(n)

    Decode:
        O(n)

Pattern Recognition:
    ✓ Need to convert multiple strings into one string?
        → Serialization

    ✓ Delimiters may appear inside strings?
        → Store metadata (length)

    ✓ Need perfect reconstruction?
        → Length + Delimiter + Data

Use Cases:
    • Network Communication:
        Serialize data before transmission.

    • REST APIs:
        Convert objects into transferable formats.

    • Databases:
        Store structured data as strings.

    • File Formats:
        JSON, XML, YAML serialization.

    • Message Queues:
        Kafka, RabbitMQ payload serialization.

    • Distributed Systems:
        Exchange structured messages between services.

    • Multiplayer Games:
        Serialize player state before sending over the network.

    • Remote Procedure Calls:
        gRPC and Protocol Buffers.

Key Idea:
    Instead of searching for where a string ends,
    store how many characters belong to that string.

    Example:

        ["neet", "code"]

    Encoded:

        4#neet4#code

    Decoding:

        Read length → 4
        Skip '#'
        Read next 4 characters → "neet"

        Repeat until finished.

Hash Map:
    Not Required
        
"""

from typing import List


# ==========================================================
# Codec
# ==========================================================


class Codec:
    """
    Time Complexity:
        Encode: O(n)

        Decode: O(n)

    Space Complexity:
        Encode: O(n)

        Decode: O(n)
    """
    def encode(self, strs: List[str]) -> str:
        """ 
        Encode list of strings into one string.
        """
        encoded = ""
        for word in strs: 
            encoded += str(len(word)) + "#" + word 
        
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decode an encoded string back into
        the original list of strings.
        """
        decoded = []
        
        pointer = 0 
        
        while pointer < len(s):
            delimiter = pointer 
            
            while s[delimiter] != "#":
                delimiter += 1
            
            length = int(s[pointer: delimiter])
            
            pointer = delimiter + 1 
            
            decoded.append(s[pointer:pointer+length])
            
            pointer += length
        
        return decoded 
    
    
# ==========================================================
# Test Cases
# ==========================================================

if __name__ == "__main__":

    codec = Codec()

    words = [
        "neet",
        "code",
        "love",
        "you"
    ]

    encoded = codec.encode(words)

    print("=== Original ===")
    print(words)

    print()

    print("=== Encoded ===")
    print(encoded)

    print()

    print("=== Decoded ===")
    print(codec.decode(encoded))

    print()

    words2 = [
        "abc#xyz",
        "",
        "hello,world",
        "Python"
    ]

    encoded2 = codec.encode(words2)

    print("=== Edge Case ===")
    print(codec.decode(encoded2))
            