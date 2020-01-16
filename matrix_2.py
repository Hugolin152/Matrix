# -*- coding: utf-8 -*-
  # 把...改成代的代码，使得“测试”部位的代码能正确运行并输出显示。
    # 1. 了解面向对象编程；
    # 2. 了解Python的特征方法（以__开头和结尾的方法，如：__add__）；
    # 3. 判断输入数据的类型。
    # 4. @property的使用。
import copy
class Matrix(object):
    def __init__(self,matrix):
        self.matrix = matrix
        
    def __add__(self,other):
        if isinstance(other,(int,float)):
            c = copy.deepcopy(self.matrix)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix [0])):
                    c [i][j] += other
            return c
        c = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix [0])):
                c[i][j] = self.matrix [i][j] + other.matrix [i][j]
        return c
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        if isinstance(other,(int,float)):
            return self.__add__(-other)
        else:
            return self.__add__(Matrix(other.__mul__(-1)))
        
    def __rsub__(self,other):
        if isinstance(other,(int,float)):
            c = copy.deepcopy(self.matrix)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix [0])):
                    c [i][j] = other - c[i][j]
            return c
        
    def __mul__(self,other):
        if isinstance (other,(int,float)):
            c = copy.deepcopy(self.matrix)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix [0])):
                    c [i][j] = self.matrix [i][j] * other
            return c
        else :
            c = [[0] * len(other.matrix[0]) for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        c[i][j] =c[i][j] + self.matrix[i][k] * other.matrix[k][j]
            return c                  
      
    def __rmul__(self,other):
        return self.__mul__(other)
        
    @property
    def det(self):
        if len(self.matrix)<=0:
            return None
        elif len(self.matrix) == 2:
            return self.matrix [0][0] * self.matrix [1][1] - self.matrix [0][1] * self.matrix [1][0]
        if len(self.matrix) != len(self.matrix [0]):
            raise ValueError('输入的不是n阶矩阵')
        matrix_det = 0
        for i in range(len(self.matrix)):
            m = [[row[j] for j in range(len(self.matrix)) if j != i] for row in self.matrix [1:]]
            matrix_det = matrix_det + (-1)**(i) * self.matrix [0][i] * det(m)
        return matrix_det

    @property
    def shape(self):
        return (len(self.matrix),len(self.matrix[0]))

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[1, 0], [0, 1]])
u = Matrix([[1, 2]])
v = Matrix([[1], [2]])
a = 4

print('A + B =',A + B)
print('a + A =',a + A)
print('A - B =',A - B)
print('a - A = ',a - A)
print('A - a =',A - a)
print('a * A =',a * A)
print('A * a =',A * a)
print('u * A =',u * A)
print('B * v =',B * v)
print('A * B =',A * B)
print(A.det)  # 行列式
#print(A.eigen_values())  # 特征值
print(A.shape)  # 矩阵的维数，如A，输出(2, 2)
