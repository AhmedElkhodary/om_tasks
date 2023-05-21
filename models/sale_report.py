from odoo import models, fields, api


class SaleReport(models.Model):
    _inherit = 'sale.report'

    test = fields.Char(string="Test", readonly=True)

    def _select_additional_fields(self, fields):
        fields['test'] = ", s.test"
        return super()._select_additional_fields(fields)


