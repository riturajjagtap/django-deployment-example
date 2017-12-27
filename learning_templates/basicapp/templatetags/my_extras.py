from django import template

register=template.Library()

@register.filter(name='cut1')
def cut1(value,arg):#Cuts all values of 'arg' from string
    return value.replace(arg,'')

#register.filter('cut_filter',cut)


