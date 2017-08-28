import json

class ProfileSerializer():
    
    def serialize(self, profile):
        output = {}
        output['name'] = profile.name
        output['native'] = [l.name for l in profile.nativelangs.all()]
        output['learning'] = [l.name for l in profile.learninglangs.all()]
        return output
