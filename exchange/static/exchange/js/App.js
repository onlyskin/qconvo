var model = {
    languages: [],
    users: [],
}

var ctrl = {
    setNativeSearch: function(language) { this._nativeSearch = language; },
    getNativeSearch: function(language) { return this._nativeSearch; },
    setLearningSearch: function(language) { this._learningSearch = language; },
    getLearningSearch: function(language) { return this._learningSearch; },
    populateLanguages: function() {
        that = this;
        m.request({
            method: 'GET',
            url: 'api/languages',
        })
        .then(function(result) {
            model.languages = result;
            that.profileSearch();
        });
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
    _isValidSearchParams: function() {
        return (model.languages.includes(this._nativeSearch) &&
            model.languages.includes(this._learningSearch));
    },
    _nativeSearch: 'english',
    _learningSearch: 'polish',
}

ctrl.populateLanguages();

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
