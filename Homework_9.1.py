"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.
"""

my_list = ['masha', 'bob', 'mark', 'max', 'julia']
print('\n'.join('{} - {}'.format(*i) for i in enumerate(my_list)))