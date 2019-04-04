"""
Problem
You are catering a party for some children, and you are serving them a cake in the 
shape of a grid with R rows and C columns. Your assistant has started to decorate 
the cake by writing every child's initial in icing on exactly one cell of the cake. 
Each cell contains at most one initial, and since no two children share the same 
initial, no initial appears more than once on the cake.

Each child wants a single rectangular (grid-aligned) piece of cake that has their 
initial and no other child's initial(s). Can you find a way to assign every blank 
cell of the cake to one child, such that this goal is accomplished? It is 
guaranteed that this is always possible. There is no need to split the 
cake evenly among the children, and one or more of them may even get a 1-by-1 piece; 
this will be a valuable life lesson about unfairness.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with two integers R and C. Then, there are R more lines of C characters each, representing the cake. Each character is either an uppercase English letter (which means that your assistant has already added that letter to that cell) or ? (which means that that cell is blank).

Output
For each test case, output one line containing Case #x: and nothing else. Then output R more lines of C characters each. Your output grid must be identical to the input grid, but with every ? replaced with an uppercase English letter, representing that that cell appears in the slice for the child who has that initial. You may not add letters that did not originally appear in the input. In your grid, for each letter, the region formed by all the cells containing that letter must be a single grid-aligned rectangle.

If there are multiple possible answers, you may output any of them.

Limits
1 ≤ T ≤ 100.
There is at least one letter in the input grid.
No letter appears in more than one cell in the input grid.
It is guaranteed that at least one answer exists for each test case.


Sample:

Input 
     
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE


Output 
 
Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE
"""
t=int(input())
for x in range(t):
    m,n=map(int, input().split())
    l=[]
    emptyRows=[]
    for i in range(m):
        l.append(list(input()))
    for rowindex, row in enumerate(l):
        tempi=-1
        for i in range(n):
            if row[i] !="?":
                temp=row[i]
                tempi=i
                break
        if tempi==-1:
            emptyRows.append(rowindex)
            continue
        for i in range(tempi):
            row[i]=temp
        for i in range(tempi,n):
            if row[i]=="?":
                row[i]=temp
            else:
                temp=row[i]
    
    
    for i in range(m):
        if i not in emptyRows:
            temprow=l[i]
            break
    for i in range(m):
        if i in emptyRows:
            l[i]=temprow
        else:
            temprow=l[i]
    print("Case#%d"%(x+1))
    for row in l:
        for letter in row:
            print(letter, end="")
        print()
           
