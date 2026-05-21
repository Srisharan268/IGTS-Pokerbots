def solve_psne(p1_matrix, p2_matrix):

    rows = len(p1_matrix)
    cols = len(p1_matrix[0])

    p1_best =[]
    p2_best =[]

    psne=[]

    for j in range(cols):
        
        x = -2**31

        for i in range(rows):
            if p1_matrix[i][j] >= x:
                x = p1_matrix[i][j]
        
        for i in range(rows):
            if p1_matrix[i][j] == x:
                p1_best.append((i,j))

    for i in range(rows):
        x = max(p2_matrix[i])
        for j in range(cols):
            if p2_matrix[i][j] == x:
                p2_best.append((i,j))

    for n in p1_best:
        if n in p2_best:
            psne.append(n)

    return psne