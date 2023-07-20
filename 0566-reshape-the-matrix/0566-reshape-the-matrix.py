class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Check if the reshape operation is possible
        if m * n != r * c:
            print("Reshape operation is not possible with the given parameters.")
            return mat

        # Reshape the matrix
        reshaped_matrix = [mat[i][j] for i in range(m) for j in range(n)]
        reshaped_matrix = [reshaped_matrix[i:i + c] for i in range(0, len(reshaped_matrix), c)]

        # Output the reshaped matrix
        print("Reshaped matrix:")
        for row in reshaped_matrix:
            print(row)

        return reshaped_matrix