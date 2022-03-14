from odoo import fields, api, models

class Auction(models.Model):
    _name = "moduletest.auction"
    _description = "Vente"

    name = fields.Char(string="Vente")
    lot_ids = fields.One2many(string="Lots", comodel_name="moduletest.lot", inverse_name="auction_id")