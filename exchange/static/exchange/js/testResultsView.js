o.spec("Results", function() {
        o("returns a div", function() {
                    var users = [{'name': 'sam'}, {'name': 'hex'}];
                    var vnode = resultsView(users);

                    o(vnode.tag).equals('div');
                    o(vnode.children.length).equals(users.length);
                    o(vnode.children[0].text).equals(users[0].name);
                })
})
