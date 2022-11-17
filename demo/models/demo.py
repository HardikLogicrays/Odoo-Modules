from odoo import fields, models


class Demo(models.Model):
    _name = "demo.model"
    _description = "Demo Model"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email", required=True)