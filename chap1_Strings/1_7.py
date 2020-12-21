import numpy as np
    
def main():
    matrix_ = np.random.rand(10,5)
    matrix_[0,0], matrix_[3,2], matrix_[5,4] = 0, 0, 0
    print(matrix_)
    print(func(matrix_=matrix_))
    
def func(matrix_):
    for row_index in range(matrix_.shape[0]):
        row = matrix_[row_index, :]
        if 0 in row:
            matrix_[row_index, :] = [np.nan if i != 0 else 0 for i in row]
    for col_index in range(matrix_.shape[1]):
        col = matrix_[:, col_index]
        if 0 in col:
            matrix_[:, col_index] = [np.nan if i != 0 else 0 for i in col]
    matrix_[np.isnan(matrix_)] = 0
    return matrix_
            
if __name__ == "__main__":
    main()