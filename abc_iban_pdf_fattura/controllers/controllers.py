# -*- coding: utf-8 -*-
# from odoo import http


# class AbcIbanPdfFattura(http.Controller):
#     @http.route('/abc_iban_pdf_fattura/abc_iban_pdf_fattura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_iban_pdf_fattura/abc_iban_pdf_fattura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_iban_pdf_fattura.listing', {
#             'root': '/abc_iban_pdf_fattura/abc_iban_pdf_fattura',
#             'objects': http.request.env['abc_iban_pdf_fattura.abc_iban_pdf_fattura'].search([]),
#         })

#     @http.route('/abc_iban_pdf_fattura/abc_iban_pdf_fattura/objects/<model("abc_iban_pdf_fattura.abc_iban_pdf_fattura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_iban_pdf_fattura.object', {
#             'object': obj
#         })
