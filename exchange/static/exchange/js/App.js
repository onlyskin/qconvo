var model = {
    languages: [],
    countries: [],
    users: [],
    isValidLanguage: function(language) {
        return this.languages.includes(language);
    },
}

var dataPopulator = new DataPopulator(model);
var ctrl = new Ctrl(model, dataPopulator);

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
