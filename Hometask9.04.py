"""
Дан список имен, отфильтровать все имена, где есть буква k
"""

my_list = filter(lambda x: 'k' in x, ['masha', 'katy', 'shelby', 'karin'])
print(list(my_list))