from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string="Test")

