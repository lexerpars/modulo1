# -*- coding: utf-8 -*-
from odoo import models, fields, api

class modulo1(models.Model):
    _name = 'modulo1.modulo1'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    @api.depends('value')
    def _values_pc(self):
        self.value2 = float(self.value)/100