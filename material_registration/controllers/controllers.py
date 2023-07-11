from odoo import http
from odoo.http import request
from odoo.exceptions import UserError, ValidationError

class MaterialController(http.Controller):

    @http.route('/material/create', type='http', auth='user', website=False)
    def create_material(self, **post):
        code = post.get('code')
        name = post.get('name')
        material_type = post.get('type')
        buy_price = float(post.get('buy_price'))
        supplier_id = int(post.get('supplier_id'))

        if code and name and material_type and buy_price and supplier_id:
            material = request.env['material'].create({
                'code': code,
                'name': name,
                'type': material_type,
                'buy_price': buy_price,
                'supplier_id': supplier_id
            })

            # Menampilkan pesan sukses atau error
            if material:
                return "Material created successfully."
            else:
                return "Failed to create material."
        else:
            return "Failed to create material."

    @http.route('/material/update/<int:material_id>', type='http', auth='user', website=False)
    def update_material(self, material_id, **post):
        material = request.env['material'].browse(material_id)

        material.write(post)

        return "Material updated successfully."

    @http.route('/material/delete/<int:material_id>', type='http', auth='user', website=False)
    def delete_material(self, material_id):
        material = request.env['material'].browse(material_id)
        material.unlink()

        return "Material deleted successfully."

    @http.route('/material', type='http', auth='user', website=True)
    def view_materials(self, **kw):
        materials = request.env['material'].search([])
        # return materials

        return request.render('material_registration.material_template', {'materials': materials})
