from math import ceil

class Solution:
	def is_prime(self, n):
		if n == 2 or n == 3: 
			return True
			
		if n < 2 or n % 2 == 0: 
			return False

		if n < 9: 
			return True

		if n % 3 == 0: 
			return False

		r = int(n ** 0.5)
		f = 5

		while f <= r:
			if n % f == 0: 
				return False
			if n % (f + 2) == 0: 
				return False

			f += 6

		return True    
	
	def is_palindrome(self, n):
		return str(n)[::-1] == str(n)

	def next_palindrome(self, n, depth = 0):
		if n + depth < 10:
			return n + depth, depth
		
		if n < 10:
			depth -= 10 - n
			n = 10

		size = len(str(n))
		initial_root_size = ceil(size / 2)
		root = int(str(n)[0:initial_root_size]) + depth
		root_size = len(str(root))
		reverse_size = root_size - 1 if root_size >= 2 else root_size
		root_reversed = int(str(root)[0:reverse_size])
		palindrome = int(str(root) + str(root_reversed)[::-1])

		if palindrome < n:
			return self.next_palindrome(n, depth + 1)
		else:
			return palindrome, depth

	def primePalindrome(self, n: int) -> int:
		last_palindrome, depth = self.next_palindrome(n)

		while not self.is_prime(last_palindrome):
			response = self.next_palindrome(n, depth + 1)
			last_palindrome = response[0]
			depth += 1

		return last_palindrome

print(Solution().primePalindrome(6))