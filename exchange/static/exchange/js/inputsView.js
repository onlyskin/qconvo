var inputsView = function() {
    return m('.inputs', [
        m('datalist', {id: 'languages'}, model.languages.map(l => m('option', {value: l}))),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        ctrl.setNativeSearch.bind(ctrl)(value);
                        ctrl.userSearch.bind(ctrl)(value);
                    }),
                    value: ctrl.nativeSearch}),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        ctrl.setLearningSearch.bind(ctrl)(value);
                        ctrl.userSearch.bind(ctrl)(value);
                    }),
                    value: ctrl.learningSearch}),
    ]);
}
