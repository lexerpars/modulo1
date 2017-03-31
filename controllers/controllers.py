# -*- coding: utf-8 -*-
from odoo import http

# class Modulo2(http.Controller):
#     @http.route('/modulo2/modulo2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo2/modulo2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo2.listing', {
#             'root': '/modulo2/modulo2',
#             'objects': http.request.env['modulo2.modulo2'].search([]),
#         })

#     @http.route('/modulo2/modulo2/objects/<model("modulo2.modulo2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo2.object', {
#             'object': obj
#         })