import unittest
import os
import json
from ..app import create_app, db

class SectionTests(unittest.TestCase):
    """
    Sections Test Case
    """

    def setUp(self):
        """
        Test SetUp
        """
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.section = {
            'title': 'Test Title',
            'contents': 'Some test content'
        }
        with self.app.app_context():
            db.create_all()

    def test_section_save(self):
        """test section is created"""
        res = self.client().post('/api/v1/sections/', headers={'Content-Type': 'application/json'},
        data=json.dumps(self.section))
        self.assertEqual(res.status_code, 201)

    def test_section_is_correct(self):
        """test section can be retrieved correctly"""
        res = self.client().post('/api/v1/sections/', headers={'Content-Type': 'application/json'},
                               data=json.dumps(self.section))
        get_res = self.client().get('api/v1/sections/', headers={'Content-Type': 'application/json'})
        records = json.loads(get_res.data)
        self.assertEqual(records[0]['title'], 'Test Title')

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()