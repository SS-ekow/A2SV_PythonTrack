if __name__ == '__main__':
    N = int(input())
    queries = []
    for _ in range(N):
        queries.append(input().split())
        

        
    
    
    
arr = []

for ops in queries: 
    
     if (ops[0]== 'print'):
         print(arr)
       
     elif (ops[0]== 'insert'):
         arr.insert(int(ops[1]), int(ops[2]))
       
     elif (ops[0]== 'remove'):
         arr.remove(int(ops[1]))
       
     elif (ops[0]== 'append'):
         arr.append(int(ops[1]))
       
     elif (ops[0]== 'sort'):
         arr.sort()
       
     elif (ops[0]== 'pop'):
         arr.pop()
       
     elif (ops[0]== 'reverse'):
         arr.reverse()