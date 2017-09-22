var model = new Model();
var profileFetcher = new ProfileFetcher(model);
var dataPopulator = new DataPopulator(model, profileFetcher);
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
