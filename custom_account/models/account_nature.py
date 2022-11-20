from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"
        
    account_nature = fields.Selection(
        selection=[("SPA", "SPA")],
        string="Natureza",
    )