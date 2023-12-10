# -*- coding: utf-8 -*-
# from odoo import http


# class Hairdresser(http.Controller):
#     @http.route('/hairdresser/hairdresser/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hairdresser/hairdresser/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hairdresser.listing', {
#             'root': '/hairdresser/hairdresser',
#             'objects': http.request.env['hairdresser.hairdresser'].search([]),
#         })

#     @http.route('/hairdresser/hairdresser/objects/<model("hairdresser.hairdresser"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hairdresser.object', {
#             'object': obj
#         })
