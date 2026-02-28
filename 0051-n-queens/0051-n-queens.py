class Solution(object):
    def solveNQueens(self,n):
        s = []

        def Bt(r, c, dl, dr, b):
            if r == n:
                board = []
                for col in b:
                    row = "." * col + "Q" + "." * (n - col - 1)
                    board.append(row)
                s.append(board)
                return

            for col in range(n):
                d1 = r - col
                d2 = r + col

                if (col in c) or (d1 in dl) or (d2 in dr):
                    continue

                c.add(col)
                dl.add(d1)
                dr.add(d2)
                b.append(col)

                Bt(r + 1, c, dl, dr, b)

                c.remove(col)
                dl.remove(d1)
                dr.remove(d2)
                b.pop()

        Bt(0, set(), set(), set(), [])
        return s