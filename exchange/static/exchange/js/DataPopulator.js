class DataPopulator {
    constructor(model, profileFetcher) {
        this.model = model;
        this.profileFetcher = profileFetcher;
    }

    initialise() {
        this._populateData('api/languages', 'languages');
        this._populateData('api/countries', 'countries');
    }
    
    _populateData(url, modelFieldName) {
        var that = this;
        m.request({
            method: 'GET',
            url: url,
        })
        .then(function(result) {
            result = result.map(function(s) {
                return s.toLowerCase();
            });
            that.model[modelFieldName] = result;
            that.profileFetcher.populateUsers();
        });
    }
}
