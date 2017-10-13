var model = new Model();
var profileFetcher = new ProfileFetcher(model);
var dataPopulator = new DataPopulator(model, profileFetcher);
var ctrl = new Ctrl(model, dataPopulator);

dataPopulator.initialise();

var Header = {
    view: function() {
        return m('#header', [
            m("a[href=/search]", {oncreate: m.route.link}, 'search'),
            m("a[href=/profile]", {oncreate: m.route.link}, 'profile'),
        ]);
    }
}

var Search = {
    view: function () {
        return m('',
            m(Header),
            inputsView(),
            resultsView(model.users)
        );
    }
}

var Profile = {
    view: function() {
        return m('',
            m(Header),
            profileView(model.profile)
        );
    }
}
