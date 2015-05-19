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
        posts = self.crowdmap.get_all_post_for("Or")
        for _name in posts:
            if _name != "Or":
                return False
            else:
                return True

    #Given a name, check if the map includes a location information (place or geo. location)
    def test_if_map_includes_location(self):
        reply = self.crowdmap.geo_location_existed("Or")

    #Check if there are map inconsistencies, e.g., the same name with different locations.
    def test_for_map_incosistencies(self):
        self.crowdmap.check_for_incosistencies()




if __name__ == '__main__':
    unittest.main()