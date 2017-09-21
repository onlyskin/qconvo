class DataPopulator {
    constructor(model) {
        this.model = model;
    }

    populateUsers(nativeLanguage, learningLanguage) {
        var that = this;
        m.request({
            method: 'GET',
            url: 'api/profiles',
            data: {n: nativeLanguage, l: learningLanguage},
        })
        .then(function(result) {
            that.model.users = result;
        });
    }
    
    populate(callback) {
        this._populateData('api/languages', 'languages', callback);
        this._populateData('api/countries', 'countries', callback);
    }
    
    _populateData(url, modelFieldName, callback) {
        var that = this;
        m.request({
            method: 'GET',
            url: url
        })
        .then(function(result) {
            that.model[modelFieldName] = result;
            callback();
        });
    }
}
