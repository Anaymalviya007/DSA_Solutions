class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency map for s1
        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1

        window_counts = {}
        left = 0

        for right in range(len(s2)):
            # 1. Add the current character to the window
            current_char = s2[right]
            window_counts[current_char] = window_counts.get(current_char, 0) + 1

            # 2. If window is too big, shrink from the left
            if (right - left + 1) > len(s1):
                char_to_remove = s2[left]
                window_counts[char_to_remove] -= 1
                if window_counts[char_to_remove] == 0:
                    del window_counts[char_to_remove]
                left += 1

            # 3. Check if current window matches s1 counts
            if window_counts == s1_counts:
                return True
        
        return False
