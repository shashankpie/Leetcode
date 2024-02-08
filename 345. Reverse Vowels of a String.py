class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        l = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and l[left] not in vowels:
                left = left + 1
            while right > left and l[right] not in vowels:
                right = right - 1
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
        return ''.join(l)
