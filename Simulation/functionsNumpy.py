# import numpy as np

# def add(x,y):
#     return x+y
    
# add = np.frompyfunc(add, 2 ,1)

# print(add([1,2,3,4], [1,2,3,4]))

import numpy as np

a = np.array([1,2,3,4,5,6,7,8])

stir = np.frompyfunc(str, 1 ,1)

print(stir(a))

#################################################################################

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.add(a,b)
# print(c)

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.subtract(a,b)
# print(c)

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.multiply(a,b)
# print(c)

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.divide(a,b)
# print(c)

#################################################################################

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.power(a,b)
# print(c)

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.mod(a,b)
# print(c)

# import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([1,2,3,4])

# c = np.divmod(a,b)
# print(c)

# import numpy as np

# a = np.array([1,-2,-3,4])
# c = np.absolute(a)
# print(c)

# import numpy as np

# a = np.array([1,-2.3,-3.5,4.87])
# c = np.trunc(a)
# print(c)

# import numpy as np

# a = np.array([1,-2.3,-3.5,4.87])
# c = np.around(a)
# print(c)

# import numpy as np

# a = np.array([1,-2.3,-3.5,4.87])
# c = np.floor(a)
# print(c)

import numpy as np

a = np.array([1,-2.3,-3.5,4.87])
c = np.ceil(a)
print(c)
