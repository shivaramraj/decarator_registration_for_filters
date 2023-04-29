from django import template

register=template.Library()

@register.filter()
def Swap(value):
    return value.swapcase()
@register.filter(name='remove_chr')
def remove(value,arg):
    return value.replace(arg,'')
@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c

# register.filter('Swap',Swap)
# register.filter('remove',remove)
# register.filter('counting',counting)