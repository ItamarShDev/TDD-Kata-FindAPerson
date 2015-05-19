__author__ = 'itamar'

class CrowdMap():
    posts = ["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"]
    def get_all_post_for(self,name):
        posts_list = []
        for l in self.posts:
            if name in l:
                posts_list.append(l)

        return posts_list

    def geo_location_existed(self,name):
        posts = self.get_all_post_for(name)
        for loc in posts:
            if "Bangkok" in loc:
                return True
        return False

    def check_for_incosistencies(self,name):
        posts = self.get_all_post_for(name)
        for l in posts:
            if self.check_city(l) is not True:
                return True
            else:
                return False

    def check_city(self,post):
        if "bangkok" in post:
            return True
        else:
            return False