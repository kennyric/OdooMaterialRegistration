from odoo import http
from odoo.http import request
from odoo.exceptions import UserError, ValidationError

class MaterialController(http.Controller):

    #Create
    @http.route('/material/create', type='json', auth='user')
    def create_material(self, **post):
        code = post.get('code')
        name = post.get('name')
        material_type = post.get('type')
        buy_price = float(post.get('buy_price'))
        supplier_id = post.get('supplier_id')
        print(supplier_id)

        if buy_price < 100:
            return "Harga tidak boleh kurang dari 100!"

        if code and name and material_type and buy_price and supplier_id:
            material = request.env['material'].create({
                'code': code,
                'name': name,
                'type': material_type,
                'buy_price': buy_price,
                'supplier_id': supplier_id
            })

            if material:
                return "Material berhasil didaftarkan."
            else:
                return "Material gagal didaftarkan."
        else:
            return "Material gagal didaftarkan."

    #Update
    @http.route('/material/update/<int:material_id>', type='json', auth="user")
    def update_material(self, material_id, **post):
        material = request.env['material'].browse(material_id)
        material.write(post)

        return "Material berhasil didaftarkan"

    #Delete
    @http.route('/material/delete/<int:material_id>', type='json', auth='user')
    def delete_material(self, material_id):
        material = request.env['material'].browse(material_id)
        material.unlink()

        return "Material berhasil dihapus."

    #Read
    @http.route('/get_material', type='http', auth='user')
    def get_materials(self, **kw):
        materials = request.env['material'].search([])
        items = []
        for line in materials:
            item = {
                'id': line.id,
                'code': line.code,
                'name': line.name,
                'type': line.type,
                'buy_price': line.buy_price,
                'supplier_id': line.supplier_id.id
            }
            items.append(item)
        return str(items)

    #get with filter
    @http.route('/get_material/<string:material_type>', type='http', auth='user')
    def get_materials_with_filter(self, material_type):
        materials = request.env['material'].search([('type','=',material_type)])
        items = []
        for line in materials:
            item = {
                'id': line.id,
                'code': line.code,
                'name': line.name,
                'type': line.type,
                'buy_price': line.buy_price,
                'supplier_id': line.supplier_id.id
            }
            items.append(item)
        return str(items)

    #Read returning view
    @http.route('/get_material_view', type='http', auth='user')
    def get_materials_view(self, **kw):
        materials = request.env['material'].search([])
        items = []
        for line in materials:
            item = {
                'id': line.id,
                'code': line.code,
                'name': line.name,
                'type': line.type,
                'buy_price': line.buy_price,
                'supplier_id': line.supplier_id.id
            }
            items.append(item)

        return request.render('material_registration.material_template', {'materials': materials})

