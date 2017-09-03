var inputsView = function() {
    return m('.inputs', [
        m('input[type=text]', {oninput: m.withAttr('value', ctrl.setNativeSearch.bind(ctrl)),
            value: ctrl.nativeSearch}),
        m('input[type=text]', {oninput: m.withAttr('value', ctrl.setLearningSearch.bind(ctrl)),
            value: ctrl.learningSearch}),
        m('button', {onclick: ctrl.userSearch.bind(ctrl)})
    ]);
}
