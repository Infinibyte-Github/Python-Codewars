def determinant(matrix):
    match len(matrix):
        case 1:
            return matrix[0][0]
        case 2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        case _:
            det = 0
            for index, element in enumerate(matrix[0]):
                if index%2 == 0:
                    det += element * determinant([r[:index] + r[index+1:] for r in (matrix[1:])])
                else:
                    det -= element * determinant([r[:index] + r[index+1:] for r in (matrix[1:])])
            return det