var resultsView = function(users) {
    return m('.container', users.map(user => m('.user', user.name)));
}
