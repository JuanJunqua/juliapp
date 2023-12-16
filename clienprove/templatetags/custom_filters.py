from django import template

register = template.Library()

@register.filter
def calculate_total_cost(facturas):
    total_cost = sum(factura.total for factura in facturas)
    return total_cost