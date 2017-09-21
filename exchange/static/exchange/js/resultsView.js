var resultsView = function(users) {
    return m('.container', users.map(user => m('.user', [
        m('.name', user.name),
        m('.country', user.country),
        m('.age', user.age),
        m('.native', user.native.map(native => m('', native))),
        m('.learning', user.learning.map(learning => m('', [
            m('span', learning.name),
            m('span', learning.level),
        ]))),
    ])));
}
