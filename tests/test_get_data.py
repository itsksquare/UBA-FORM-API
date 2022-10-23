import unittest
# from API.services.DBManipulation import fetch_from_db



class MyGetTestCase(unittest.TestCase):
    def test_get_fromdb(self):
        import requests

        url = "https://ubaformapi-git-prod-fastapis-build.vercel.app/api/get_data"
        retreive=requests.get(url,'string')
        # print(retreive.json()["detail"])
        self.assertEqual(isinstance(retreive.json(),dict),True)

if __name__=="__main__":
    unittest.main()        