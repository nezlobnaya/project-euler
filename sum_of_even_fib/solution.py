class Solution:
    def fib_even(self, num):
        
        prev_prev = 0  # 0th fibonacci
        prev = 1       # 1st fibonacci
        sum = 0
        current = 0
        while current < num:

            current = prev + prev_prev
            if (current % 2 == 0):
                sum+=current
            prev_prev = prev
            prev = current

        return sum

print(Solution().fib_even(4000000)) # 4613732