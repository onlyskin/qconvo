import json

class UserSerializer():
    
    def serialize(self, user):
        output = {}
        output['username'] = user.username
        output['name'] = user.profile.name
        links = user.profile.link_set.all().filter(level='n')
        output['native'] = [link.language.name for link in links]
        links = user.profile.link_set.all().exclude(level='n')
        output['learning'] = [link.language.name for link in links]
        return output

        # print u.profile.language_set.all()[0].name
