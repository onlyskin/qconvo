class DataPopulator {
    constructor(model) {
        this.model = model;
    }

    populateUsers(native, learning) {
        if (this._isValidSearchParams(native, learning)) {
            var that = this;
            m.request({
                method: 'GET',
                url: 'api/profiles',
                data: {n: native, l: learning},
            })
            .then(function(result) {
                that.model.users = result;
            });
        }
    }
    
    populate(callback) {
        this._populateData('api/languages', 'languages', callback);
        this._populateData('api/countries', 'countries', callback);
    }
    
    _isValidSearchParams(native, learning) {
        return this.model.isValidLanguage(native) && this.model.isValidLanguage(learning);
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
