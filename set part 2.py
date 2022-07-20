# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b))    # true
# print(b.issubset(a))      # false
# print(a.issubset(c))    # false
# print(b.issubset(c))      #false
# print(c.issubset(b))       # true

# print(dir(set))  # all methods
'''1.difference_update'''
# a={5,12,15,18,20}
# b={15,18,21,25}
# print(a.update(b))      # none {5,12,15,18,20,21,25}
# print(a)
# c=a.difference_update(b)
# print(c)                  # none
# print(a-b)
# print(a)               # {12,20,5}
# b.difference_update(a)
# print(b)                     #{21,25}
# a.difference_update(b)
# print(a)                    #{20,5,12}
'''2.copy'''
# a={1,2,3,4,5}
# a.copy()
# print(a)
'''3.symmetric_difference_update'''
# a={5,12,15,18,20}
# b={15,18,21,25}
# a.symmetric_difference(b)
# print(a)                  # {18,20,5,12,15}
# b.symmetric_difference(a)
# print(b)                    #  {25,18,21,15}
# a.symmetric_difference_update(b)
# print(a)                       #  {20,5,21,25,12}
# b.symmetric_difference_update(b)
# print(b)                         # settofff set()
'''4.intersection_update'''
# a={5,12,15,18,20}
# b={15,18,21,25}
# a.intersection(b)
# print(a)            #{18,20,5,12,15}
# b.intersection(a)
# print(b)              #{25,18,21,15}
# a.intersection_update(b)
# print(a)                 #{18,15}
# b.intersection_update(a)
# print(b)                  #{15,18}
'''6.remove'''
# a={8,9,10,12,14}
# a.remove(147)
# print(a)             # keyError:147
# a.remove(10)
# print(a)               # {8,9,12,14}
'''7.issuperset'''
# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))     # false
# print(b.issuperset(a))       #  false 
# a={8,9,10,12,14}
# b={8,9,10}
# print(a.issuperset(b))       # true
# print(b.issuperset(a))         # false
'''subset'''
# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b))       # true
# print(a.issubset(c))         # false
# print(b.issubset(a))         #false
# print(b.issubset(c))         #false
# print(c.issubset(a))           # false
# print(c.issubset(b))           # true