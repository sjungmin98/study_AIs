py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

# 구분 위한 type 확인
type(py_list)
# <class 'list'>
type(np_array)

#병합
np_array_second = np.array(py_list)
type(np_array_second)
# <class 'numpy.ndarray'>
np.concatenate((np_array, np_array_second), axis=0) # row 단위 병합
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array, np_array_second), axis=1) # column 단위 병합
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])

pass