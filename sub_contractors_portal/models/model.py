from odoo import models, fields

class SubContractors(models.Model):
    _name = 'sub.contractor'
    _description = 'Defining'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    abn = fields.Char(string='ABN')
    phone_no = fields.Char(string='Phone No')