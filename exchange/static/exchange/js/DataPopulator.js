class DataPopulator {
    constructor(model) {
        this._nativeSearch = 'english';
        this._learningSearch = 'polish';
        this.model = model;
    }

    get nativeSearch() { return this._nativeSearch; }
    set nativeSearch(language) { this._nativeSearch = language; }
    get learningSearch() { return this._learningSearch; }
    set learningSearch(language) { this._learningSearch = language; }

    populateUsers() {
        if (this._isValidSearch()) {
            var that = this;
            m.request({
                method: 'GET',
                url: 'api/profiles',
                data: {n: that.nativeSearch, l: that.learningSearch},
            })
            .then(function(result) {
                that.model.users = result;
            });
        }
    }
    
    initialise(callback) {
        this._populateData('api/languages', 'languages');
        this._populateData('api/countries', 'countries');
    }
    
    _isValidSearch() {
        return this.model.isValidLanguage(this.nativeSearch) &&
            this.model.isValidLanguage(this.learningSearch);
    }

    _populateData(url, modelFieldName) {
        var that = this;
        m.request({
            method: 'GET',
            url: url
        })
        .then(function(result) {
            that.model[modelFieldName] = result;
            that.populateUsers();
        });
    }
}
