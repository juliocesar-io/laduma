from django import template

from moneyed import Money
from djmoney_rates.utils import convert_money


register = template.Library()

@register.simple_tag
def convert_currency(amount, form, to):
    c = convert_money(amount, form, to)
    return c