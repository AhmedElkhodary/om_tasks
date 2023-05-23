from odoo import models, fields, api


class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    test = fields.Char(
        string='Test',
    )