from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class Material(models.Model):
    _name = 'material'
    _description = 'Material'

    code = fields.Char(string='Material Code')
    name = fields.Char(string='Material Name')
    type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], string='Material Type')
    buy_price = fields.Float(string='Material Buy Price')
    supplier_id = fields.Many2one('material.supplier', string='Related Supplier')

    @api.constrains('buy_price')
    def check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise UserError("Harga tidak boleh kurang dari 100!")

class Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Material Supplier'

    name = fields.Char(string='Supplier Name')