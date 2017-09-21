var model = {
    languages: [],
    countries: [],
    users: [],
}

var ctrl = {
    setNativeSearch: function(language) { this._nativeSearch = language; },
    getNativeSearch: function(language) { return this._nativeSearch; },
    setLearningSearch: function(language) { this._learningSearch = language; },
    getLearningSearch: function(language) { return this._learningSearch; },
    setMinAge: function(age) { this._minAge = age; },
    getMinAge: function(age) { return this._minAge; },
    _populateData: function(url, modelFieldName) {
        that = this;
        m.request({
            method: 'GET',
            url: url
        })
        .then(function(result) {
            model[modelFieldName] = result;
            that.profileSearch();
        });
    },
    populateLanguages: function() {
        this._populateData('api/languages', 'languages');
    },
    populateCountries: function() {
        this._populateData('api/countries', 'countries');
    },
    profileSearch: function() {
        if (this._isValidSearchParams()) {
            var that = this;
            m.request({
                method: 'GET',
                url: 'api/profiles',
                data: {n: that._nativeSearch, l: that._learningSearch},
            })
            .then(function(result) {
                model.users = result;
            });
        }
    },
    profileFilter: function(user) {
        return user.age > this._minAge;
    },
    _isValidSearchParams: function() {
        return (model.languages.includes(this._nativeSearch) &&
            model.languages.includes(this._learningSearch));
    },
    _nativeSearch: 'english',
    _learningSearch: 'polish',
    _minAge: 0,
}

ctrl.populateLanguages();
ctrl.populateCountries();

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
