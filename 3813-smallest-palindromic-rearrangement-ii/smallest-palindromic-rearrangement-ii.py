class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        
        # Count character frequencies for the first half
        freq = [0] * 26
        for i in range(half_len):
            freq[ord(s[i]) - ord('a')] += 1
            
        def count_ways(freq_list: list[int], cap: int) -> int:
            """Computes multinomial coefficient capped at `cap`."""
            rem = sum(freq_list)
            ways = 1
            
            for f in freq_list:
                if f > 0:
                    # Calculate nCr(rem, f)
                    r = min(f, rem - f)
                    n_val = rem
                    ncr = 1
                    for i in range(1, r + 1):
                        ncr = ncr * (n_val - i + 1) // i
                        if ncr * ways >= cap:
                            return cap
                    ways *= ncr
                    if ways >= cap:
                        return cap
                    rem -= f
            return ways

        # Check if total possible palindromic permutations is less than k
        if count_ways(freq, k) < k:
            return ""

        # Construct the first half character by character
        first_half = []
        for _ in range(half_len):
            for c in range(26):
                if freq[c] > 0:
                    # Try placing character c
                    freq[c] -= 1
                    ways = count_ways(freq, k)
                    
                    if ways >= k:
                        first_half.append(chr(ord('a') + c))
                        break  # Fix character c at this position
                    else:
                        k -= ways
                        freq[c] += 1  # Backtrack and try next character

        half_str = "".join(first_half)
        mid_char = s[half_len] if n % 2 != 0 else ""
        
        return half_str + mid_char + half_str[::-1]