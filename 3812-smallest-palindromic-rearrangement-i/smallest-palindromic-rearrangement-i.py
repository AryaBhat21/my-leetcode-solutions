class Solution:

  def smallestPalindrome(self, s: str) -> str:
    # Frequency array for 26 lowercase English letters
    freq = [0] * 26

    # Count character occurrences
    for char in s:
      freq[ord(char) - ord("a")] += 1

    first_half = []
    mid = ""

    # Build first half in alphabetical order
    for i in range(26):
      if freq[i] > 0:
        char = chr(ord("a") + i)
        first_half.append(char * (freq[i] // 2))

        # Capture the middle character if frequency is odd
        if freq[i] % 2 != 0:
          mid = char

    left = "".join(first_half)
    return left + mid + left[::-1]