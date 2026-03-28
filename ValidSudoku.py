# method 1 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        my_set = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row = f"{board[i][j]} ROW {i}"
                col = f"{board[i][j]} COL {j}"
                box = f"{board[i][j]} BOX {i//3}, {j//3}"

                if row in my_set or col in my_set or box in my_set:
                    return False
                my_set.add(row)
                my_set.add(col)
                my_set.add(box)
        return True

# method 2 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        # validate the rows
        for i in range(rows):
            my_set = set()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in my_set:
                    my_set.add(board[i][j])
                else:
                    return False

        # validating the rows
        for j in range(cols):
            my_set = set()
            for i in range(rows):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in my_set:
                    return False
                my_set.add(board[i][j])

        def traversal(sr,sc,end_row,end_col):
            st = set()
            for i in range(sr,end_row+1):
                for j in range(sc,end_col+1):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] in st:
                        return False
                    st.add(board[i][j])
            return True
        # validating the 3x3 square
        for i in range(0,rows,3):
            end_row = i + 2
            for j in range(0,cols,3):
                end_col = j + 2
                flag = traversal(i,j,end_row,end_col)
                if flag == True :
                    continue
                return False
        return True
