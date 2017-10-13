var profileView = function(profile) {
    return m('', [
            m('', profile.name),
            m('', profile.country),
    ]);
}
