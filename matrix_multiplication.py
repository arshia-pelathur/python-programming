m1 = [[1,2,3],[4,5,6]]
m2 = [[9,8],[6,5],[7,4]]

solution = [[sum(m1[i][j] * m2[j][k] for j in range(len(m2)))  for k in range(len(m2[0])) ] for i in range(len(m1))]


print(solution)