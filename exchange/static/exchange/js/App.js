var model = {
    languages: [],
    users: [
        {'name': 'Sam',
         'country': 'United Kingdom',
         'age': 25,
         'native': ['english'],
         'learning': ['polish', 'italian']},
        {'name': 'Joanna',
         'country': 'Poland',
         'age': 28,
         'native': ['polish', 'italian'],
         'learning': ['english']},
    ],
}

var ctrl = {
    setNativeSearch: function(language) { this._nativeSearch = language; },
    setLearningSearch: function(language) { this._learningSearch = language; },
    userSearch: function() {
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
        return model.languages.includes(this._nativeSearch) && model.languages.includes(this._learningSearch);
    },
    _nativeSearch: '',
    _learningSearch: '',
}

m.request({
    method: 'GET',
    url: 'api/languages',
})
.then(function(result) {
    model.languages = result;
});

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
