class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_list=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_list.append([i,j])
        for [i,j] in zero_list:
            for col in range(n):
                matrix[i][col]=0
            for row in range(m):
                matrix[row][j]=0