import json

class UserSerializer():
    
    def serialize(self, user):
        output = {}
        output['username'] = user.username
        output['name'] = user.profile.name
        return output
