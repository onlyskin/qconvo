var inputsView = function() {
    return m('.inputs', [
        m('datalist', {id: 'languages'}, model.languages.map(l => m('option', {value: l}))),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        ctrl.setNativeSearch(value);
                        ctrl.profileSearch(value);
                    }),
                    value: ctrl.getNativeSearch()}),
        m('input', {list: 'languages',
                    oninput: m.withAttr('value', function(value) {
                        ctrl.setLearningSearch(value);
                        ctrl.profileSearch(value);
                    }),
                    value: ctrl.getLearningSearch()}),
        m('input', {type: 'number',
                        min: 0,
                        max: 200,
                        oninput: m.withAttr('value', function(value) {
                        ctrl.setMinAge(value);
                    }),
                    value: ctrl.getMinAge()}),
    ]);
}
