from odoo.tests import common

class MaterialTestCase(common.TransactionCase):

    def setUp(self):
        super(MaterialTestCase, self).setUp()

    def test_material_creation(self):
        fabric_supplier_id = self.env['material.supplier'].create({'name': 'fabric supplier'})
        material = self.env['material'].create({
            'code': '001',
            'name': 'Soft Fabric',
            'type': 'fabric',
            'buy_price': 145.0,
            'supplier_id': fabric_supplier_id.id,
        })
        self.assertEqual(material.code, '001')
        self.assertEqual(material.name, 'Soft Fabric')
        self.assertEqual(material.type, 'fabric')
        self.assertEqual(material.buy_price, 145.0)
        self.assertEqual(material.supplier_id.name, 'fabric supplier')



    def test_material_filter(self):
        fabric_materials = self.env['material'].search([('type', '=', 'fabric')])
        self.assertTrue(fabric_materials)
        for fabric in fabric_materials:
            self.assertEqual(fabric.type, 'fabric')