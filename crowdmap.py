__author__ = 'itamar'

class CrowdMap():

    def get_all_post_namefor(self):
        return ["Or"]

    def geo_location_existed(self,name):
        posts = self.get_all_post_for(name)
        for loc in posts:
            if loc == "Bangkok":
                return True

        return False

    def check_for_incosistencies(self):
        return False