var model = {
    languages: [],
    countries: [],
    users: [],
    isValidLanguage: function(language) {
        return this.languages.includes(language);
    },
}

var ctrl = new Ctrl(model);

var dataPopulator = new DataPopulator(model);
dataPopulator.populate(function() {
    ctrl.profileSearch();
});

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
