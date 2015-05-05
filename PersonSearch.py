__author__ = 'itamar'
import unittest


class CrowdMap (object):
    def get_all_post(self,param):
     pass

class PersonSearch (unittest.TestCase):
    def setUp(self):
        self.crowdmap = CrowdMap()

    def test_getAllPostsForName(self):
        posts = self.crowdmap.get_all_post_for("Or")
        self.assertIn("Or",posts)

if __name__ == '__main__':
    unittest.main()