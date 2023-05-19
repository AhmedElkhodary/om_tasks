from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'  # inherit SaleOrder Model from Sales Module

    test = fields.Char(string="Test")  # added new field {test} in sale.order model.
