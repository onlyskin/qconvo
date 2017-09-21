import json

class ProfileSerializer():
    
    def serialize(self, profile):
        output = {}
        output['name'] = profile.name
        output['country'] = profile.country.name
        output['age'] = profile.age
        output['native'] = [l.name for l in profile.nativelangs.all()]
        output['learning'] = [{
            'name': l.name,
            'level': l.link_set.get().level,
            } for l in profile.learninglangs.all()]
        return output
