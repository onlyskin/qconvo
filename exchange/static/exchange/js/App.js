var model = {
    users: [{'name': 'sam'}, {'name': 'hex'}],
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
            data: {n: that.nativeSearch, l: that.learningSearch}
        })
        .then(function(result) {
            model.users = result;
        });
    },
}

var App = {
    view: function () {
        return m('',
            inputsView(),
            resultsView(model.users)
        );
    }
}
