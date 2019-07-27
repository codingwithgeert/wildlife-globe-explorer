import unittest
import app
from flask import Flask
from flask import render_template



class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.client = self.app.test_client()
    def test_get_animals(self):
        result = self.client.get('/spotlist_list')
        self.assertTrue(result.status_code == 200)
        self.assertIn(b'Boar', result.data)
     

        
if __name__ == '__main__':
    unittest.main()   
    
    
  