def towerOfHN(n, source, auxiliary, destination):
    if n <= 0:
        print("Nothing to do")
        return
    
    if n == 1:
        print("Move %d from %s to %s" % (n, source, destination))
        return 
    
    # n > 1
    #1. move n-1 rings from source to auxiliary and using destination as support peg 
    towerOfHN(n-1, source, destination, auxiliary)
    #2. move the last ring in source to destination
    print("Move %d from %s to %s" % (n, source, destination))
    #3. move n-1 rings from auxiliary to destination and using source as support peg
    towerOfHN(n-1, auxiliary, source, destination)


towerOfHN(3, 'S', 'A', 'D')
