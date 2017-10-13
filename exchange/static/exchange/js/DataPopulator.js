class DataPopulator {
    constructor(model, profileFetcher) {
        this.model = model;
        this.profileFetcher = profileFetcher;
    }

    initialise() {
        this._populateData('api/languages', 'languages', true);
        this._populateData('api/countries', 'countries', true);
        this._populateData('api/profile', 'profile', false);
    }
    
    _populateData(url, modelFieldName, lowerCase) {
        var that = this;
        m.request({
            method: 'GET',
            url: url,
        })
        .then(function(result) {
            if (lowerCase) {
                result = that._lowerCaseArray(result)
            }
            that.model[modelFieldName] = result;
            that.profileFetcher.populateUsers();
        })
        .catch(function(error) {
            console.log('There was a request error in the DataPopulator (probably unlogged in user).');
        });
    }

    _lowerCaseArray(array) {
        return array.map(function(s) {
            return s.toLowerCase();
        });
    }
}
