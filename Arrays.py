class Solution:

	""" Min Steps in Infinite Grid """

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer

    def coverPoints(self, X, Y):
        min_steps = 0
        i = 0
        while i < len(X) - 1:
            diff_x = abs(X[i] - X[i+1])
            diff_y = abs(Y[i] - Y[i+1])
            min_steps += max(diff_x, diff_y)
            i += 1            
        return min_steps


     """ Find Duplicate in Array """

    # @param A : tuple of integers
    # @return an integer

    def repeatedNumber(self, A):
        A = list(A)
        i = 0
        while i < len(A):
            index = abs(A[i])
            if A[index] >= 0:
                A[index] = -A[index]
            else:
                return index
            i += 1    
        return -1 
