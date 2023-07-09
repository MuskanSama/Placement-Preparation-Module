class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        columns = set()

        # Step 1: Find the rows and columns to be set to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        # Step 2: Set the elements to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0

        # Step 3: Return the modified matrix
        return matrix
            
        