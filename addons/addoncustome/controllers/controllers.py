# -*- coding: utf-8 -*-
# from odoo import http


# class Addoncustome(http.Controller):
#     @http.route('/addoncustome/addoncustome', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addoncustome/addoncustome/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addoncustome.listing', {
#             'root': '/addoncustome/addoncustome',
#             'objects': http.request.env['addoncustome.addoncustome'].search([]),
#         })

#     @http.route('/addoncustome/addoncustome/objects/<model("addoncustome.addoncustome"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addoncustome.object', {
#             'object': obj
#         })

