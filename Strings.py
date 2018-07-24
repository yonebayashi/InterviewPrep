class Solution:

	""" Palindrome String """

    # @param A : string
    # @return an integer
        
    def isPalindrome(self, A):
        A = ''.join(a for a in A if a.isalnum()).lower()
        
        i = len(A) - 1
        j = 0

        while i >= 0:
            if (A[i] != A[j]):
                return 0
            i -= 1
            j += 1
        return 1


    """ Longest Palindromic Substring """

    # @param A : string
    # @return a strings

    def longestPalindrome(A):
	    longestPal = A[0]
	    
	    i = 0
	    while i < len(A):
	        j = len(A) - 1
	        while j >= 0:
	            sofar = A[i:j+1]
	            if isPalindrome(sofar) and len(sofar) > len(longestPal):
	                longestPal = sofar
	            j -= 1
	        i += 1
	        
	    return longestPal