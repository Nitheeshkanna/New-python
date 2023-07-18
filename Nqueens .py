class solution:
    def solveNQueens(self, n:int) -> list[list[str]]:
        col =set()
        pdiag= set()
        ndiag= set()
        
        res=[]
        board=[["."]* n for i in range(n)]
        
        def backtracker(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or(r+c) in pdiag or(r-c) in ndiag:
                    continue
                
                col.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                board[r][c]='Q'
                
                backtracker(r+1)
                
                col.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
                board[r][c]="."
        backtracker(0)
        return res