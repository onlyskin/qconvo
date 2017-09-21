var model = {
    languages: [],
    countries: [],
    users: [],
    isValidLanguage: function(language) {
        return this.languages.includes(language);
    },
    isValidCountry: function(country) {
        return this.countries.includes(country);
    },
}

var dataPopulator = new DataPopulator(model);
var ctrl = new Ctrl(model, dataPopulator);

dataPopulator.initialise();

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
