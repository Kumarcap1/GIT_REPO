def PascalsTriangle(n):
    # Seed the first row
    triangleData = [[1]]
    
    # loop for the remaining rows
    for r in range(1,n):
        # create list to store row values
        rowData = [] 
        # first row value always 1
        rowData.append(1)
        # loop for row values up to the penultimate entry
        for e in range(1,r):
            # compute entry value from previous row values
            rowEntry = triangleData[r-1][e-1]+triangleData[r-1][e]
            # append computed value to rowData
            rowData.append(rowEntry)
    
        # last row value always 1
        rowData.append(1)
        # add list of row values to triangleData
        triangleData.append(rowData)
    
    # Print data
    for r in range(0, len(triangleData)):
        for e in range(0, len(triangleData[r])):
            print("%d\t" % (triangleData[r][e]), end="")
        print("\n")

PascalsTriangle(26)
