class Solution:
    def romanToInt(self, s: str) -> int:
        x = len(s)
        y=0
        for i in range (x):
            if s[i] == "M":
                y+=1000
            if s[i] == "D":
                y+=500
            if s[i] == "C":
                if (s[i+1] == "D") or (s[i+1] == "M"):
                    y-=100
                else:
                    y+=100
            if s[i] == "L":
                y+=50
            if s[i] == "X":
                if (s[i+1] == "C") or  (s[i+1] == "L"):
                    y-=10
                else:
                    y+=10
            if s[i] == "V":
                y+=5
            if s[i] == "I":
                if i < x-1:
                    if  (s[i+1] == "X")  or (s[i+1] == "V"):
                        y-=1
                    else:
                        y+=1
                else:
                    y+=1

        return y