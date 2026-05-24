class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squre = defaultdict(set)    

        for row in range(9):
            for colum in range(9):
                if board[row][colum]==".":
                    continue
                if (board[row][colum] in rows[row] or
                    board[row][colum] in cols[colum] or
                    board[row][colum] in squre[(row//3, colum//3)]):

                    return False
                cols[colum].add(board[row][colum])
                rows[row].add(board[row][colum])
                squre[(row//3 , colum//3)].add(board[row][colum])
        return True
            

