

matrix_1 = [
	["7", "i", "3"],
	["T", "s", "i"],
	["h", "%", "x"],
	["i", " ", "#"],
	["s", "M", " "],
	["$", "a", " "],
	["#", "t", "%"],
	["^", "r", "!"]
]

def decode_mat_by_columns(matrix):

    rows_num = len(matrix)
    columns_num = len(matrix[0])
    result = ""

    for i in range(columns_num):  # 0, 1, 2
	    for j in range(rows_num):  # 0,1, .. 7
		    if matrix[j][i].isalpha():
		        result += (matrix[j][i])

    print(result)

decode_mat_by_columns(matrix_1)
