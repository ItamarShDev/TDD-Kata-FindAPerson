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
            if loc == "Bangkok":
                return True
        return False

    # def check_for_incosistencies(self):
