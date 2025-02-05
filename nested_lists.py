if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        
    
    
    a = sorted(set([x[1] for x in arr]))[1]
    
    
    b = sorted([x[0] for x in arr if x[1]== a])
    
    for name in b: 
        print(name)
