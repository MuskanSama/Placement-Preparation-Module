class Solution(object):
    def generate(self, numRows):
        
        triangle = []

        for row in range(numRows):
            currentRow = [0] * (row + 1)
            currentRow[0] = 1
            currentRow[row] = 1

            for col in range(1, row):
                currentRow[col] = triangle[row-1][col-1] + triangle[row-1][col]

            triangle.append(currentRow)

        return triangle