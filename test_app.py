import unittest
import app
from flask import Flask
from flask import render_template


def create_app(cfg=None):
    app = Flask(__name__)
    # app.config['DEBUG'] = True
    # app.config['SERVER_NAME'] = 'localhost'
    return app


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('mytest')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        self.client = self.app.test_client()

        @self.app.route("/spotlist_list")
        def spotlist():
            return render_template('spotlist.html')

        self.assertTrue(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()   
    
    
  