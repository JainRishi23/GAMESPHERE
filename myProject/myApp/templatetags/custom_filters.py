# from django import template

# register = template.Library()

# @register.filter
# def get_color(value):
#     red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
#     black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    
#     if value in red_numbers:
#         return 'red'
#     elif value in black_numbers:
#         return 'black'
#     else:
#         return 'green'

# @register.simple_tag
# def get_range(start, end):
#     return range(start, end)

from django import template

register = template.Library()

@register.filter(name='range')
def range_filter(start, end):
    return range(start, end)

