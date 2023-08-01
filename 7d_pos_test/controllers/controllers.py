# -*- coding: utf-8 -*-
# from odoo import http


# class Witforms(http.Controller):
#     @http.route('/witforms/witforms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/witforms/witforms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('witforms.listing', {
#             'root': '/witforms/witforms',
#             'objects': http.request.env['witforms.witforms'].search([]),
#         })

#     @http.route('/witforms/witforms/objects/<model("witforms.witforms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('witforms.object', {
#             'object': obj
#         })
