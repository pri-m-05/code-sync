class Solution(object):
    def solveSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_id(r, c)].add(ch)

        def backtrack(i):
            if i == len(empties):
                return True  

            r, c = empties[i]
            b = box_id(r, c)

            for d in "123456789":
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(i + 1):
                        return True

                    
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)

            return False

        backtrack(0)