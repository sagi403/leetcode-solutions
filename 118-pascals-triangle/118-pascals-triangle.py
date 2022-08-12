class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for row in range(2, numRows):
            newRaw = [1]
            for i in range(1, row):
                newNum = res[-1][i - 1] + res[-1][i]
                newRaw += [newNum]
            newRaw += [1]
            res.append(newRaw)
        return res