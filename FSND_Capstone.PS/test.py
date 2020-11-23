import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Skaters, Goalies

class BoxScoreTestCase(unittest.TestCase):
    
    def setupTest(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.fan_token = os.environ['fan_token']
        self.GM_token = os.environ['GM_token']
        self.invalid_token = 'invalidtoken'
        setup_db(self.app)

        self.valid_new_skater = {
            'name': 'Patrick Kane',
            'pos': 'RW',
            'pts': 84,
            'gls': 33
            }

        self.invalid_new_skater = {
            'name': '',
            'pos': ''
            }

        self.valid_update_skater = {
            'name': 'Dominik Kubalik'
            }

        self.invalid_update_skater = {}

        self.valid_new_goalie = {
            'name': 'Robin Lehner',
            'gaa': 0.977,
            'so': 5,
            'w': 25
            }

        self.invalid_new_goalie = {
            'name': ''
            }

        self.valid_update_goalie = {
            'name': 'Henrik Lundvist'
            }

        self.invalid_update_goalie = {}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """"Excecuted after each test"""
        pass

    def test_home(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

#Below are the fan tokens, which allow users to view the short version of the stats
    def test_get_short_skaters_info(self):
        res = self.client().get('/skaters', headers={
            'Authorization': "Bearer {}".format(self.fan_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_short_goalies_info(self):
        res = self.client().get('/goalies', headers={
            'Authorization': "Bearer {}".format(self.fan_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_401_get_skaters_without_token(self):
        res = self.client().get('/skaters')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_get_goalies_without_token(self):
        res = self.client().get('/goalies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_get_short_skaters_info(self):
        res = self.client().get('/skaters', headers={
            'Authorization': "Bearer {}".format(self.invalid_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_get_short_goalies_info(self):
        res = self.client().get('/goalies', headers={
            'Authorization': "Bearer {}".format(self.invalid_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

#These are the GM Token tests, which allows GM role to view/add/alter/delete all of skaters stats
    def test_get_long_skaters_info_by_id(self):
        res = self.client().get('/skaters/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_skater(self):
        res = self.client().post('/skaters', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.valid_new_skater)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_get_long_goalies_info_by_id(self):
        res = self.client().get('/goalies/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_create_goalie(self):
        res = self.client().post('/goalies', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.valid_new_goalie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_422_create_skater(self):
        res = self.client().post('/skaters', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.invalid_new_skater)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_422_create_goalie(self):
        res = self.client().post('/goalies', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.invalid_new_goalie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_update_skater(self):
        res = self.client().patch('/skaters/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.valid_update_skater)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_update_goalie(self):
        res = self.client().patch('/goalies/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.valid_update_goalie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_422_update_skater(self):
        res = self.client().patch('/skaters/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.invalid_update_skater)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_422_update_goalie(self):
        res = self.client().patch('/goalies/1', headers={
            'Authorization': "Bearer {}".format(self.GM_token)
            }, json=self.invalid_update_goalie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_delete_skater(self):
        res = self.client().delete('/skaters/2', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_delete_goalie(self):
        res = self.client().delete('/goalies/2', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_404_delete_skater(self):
        res = self.client().delete('/skaters/200', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertTrue(data['success'])

    def test_404_delete_goalie(self):
        res = self.client().delete('/goalies/200', headers={
            'Authorization': "Bearer {}".format(self.GM_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

#so the tests can be easily executed:
if __name__ == "__main__":
    unittest.main()
