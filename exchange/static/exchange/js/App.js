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
    nativeSearch: '',
    learningSearch: '',
    setNativeSearch: function(language) { this.nativeSearch = language; },
    setLearningSearch: function(language) { this.learningSearch = language; },
    userSearch: function() {
        var that = this;
        m.request({
            method: 'GET',
            url: 'api/profiles',
            data: {n: that.nativeSearch, l: that.learningSearch},
        })
        .then(function(result) {
            model.users = result;
        });
    },
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
