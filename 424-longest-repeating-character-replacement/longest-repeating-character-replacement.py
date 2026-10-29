class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = {}
        maxwindow = 0
        
        for right in range(len(s)):
            max_freq[s[right]] = max_freq.get(s[right], 0) + 1
            maxwindow = max(maxwindow, max_freq[s[right]])

            if right - left + 1 - maxwindow > k:
                max_freq[s[left]] -= 1
                left += 1
            
        return len(s) - left