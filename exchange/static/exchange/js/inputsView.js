var inputsView = function() {
    return m('.inputs', [
        m('datalist', {id: 'languages'}, model.languages.map(l => m('option', {value: l}))),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        model.nativeSearch = value;
                        profileFetcher.populateUsers();
                    }),
                    value: model.nativeSearch}
        ),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        model.learningSearch = value;
                        profileFetcher.populateUsers();
                    }),
                    value: model.learningSearch}
        ),
        m('input', {type: 'number',
                        min: 0,
                        max: 200,
                        oninput: m.withAttr('value', function(value) {
                            ctrl.minAge = value;
                    }), value: ctrl.minAge}
        ),
        m('input', {type: 'number',
                        min: 0,
                        max: 200,
                        oninput: m.withAttr('value', function(value) {
                            ctrl.maxAge = value;
                    }), value: ctrl.maxAge}
        ),
        m('datalist', {id: 'countries'}, model.countries.map(c => m('option', {value: c}))),
        m('input', {list: 'countries',
                    oninput: m.withAttr('value', function(value) {
                        ctrl.country = value;
                    }),
                    value: ctrl.country}
        ),
    ]);
}
