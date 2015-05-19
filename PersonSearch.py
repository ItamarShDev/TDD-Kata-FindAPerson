__author__ = 'itamar'
import unittest
from crowdmap import CrowdMap

class test_Find_Person (object):
    def get_all_post(self,param):
     pass

class PersonSearch (unittest.TestCase):
    def setUp(self):
        self.crowdmap = CrowdMap()

    def test_getAllPostsForName(self):
        return_value = False
        posts = self.crowdmap.get_all_post_for("Or")
        for post in posts:
            if "Or" in post:
                return_value = True
            else:
                return_value = False
        self.assertTrue(return_value)

    def test_getAllPostsForName_for_missing_name(self):
        name = "not existed"
        return_value = False
        posts = self.crowdmap.get_all_post_for(name)
        for post in posts:
            if name in post:
                return_value = True
            else:
                return_value = False
        self.assertFalse(return_value)

    #Given a name, check if the map includes a location information (place or geo. location)
    def test_if_map_includes_location(self):
        reply = self.crowdmap.geo_location_existed("Or")
        self.assertTrue(reply)

    def test_if_map_includes_location_for_missing_location(self):
        reply = self.crowdmap.geo_location_existed("Not Existed")
        self.assertFalse(reply)
    #Check if there are map inconsistencies, e.g., the same name with different locations.
    def test_for_map_incosistencies(self):
        return_value = self.crowdmap.check_for_incosistencies("Or")
        self.assertTrue(return_value)




if __name__ == '__main__':
    unittest.main()