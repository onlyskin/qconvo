o.spec("Results", function() {
        o("returns a div", function() {
                    var users = [
                        {
                            'name': 'Sam',
                            'country': 'United Kingdom',
                            'age': 25,
                            'native': ['english'],
                            'learning': [
                                {'name': 'polish', 'level': 'b'},
                                {'name': 'italian', 'level': 'b'},
                             ]
                        },
                        {
                            'name': 'Joanna',
                            'country': 'Poland',
                            'age': 28,
                            'native': ['polish', 'italian'],
                            'learning': [
                                {'name': 'english', 'level': 'b'},
                             ]
                        },
                    ];
                    var vnode = resultsView(users);

                    o(vnode.tag).equals('div');
                    o(vnode.children.length).equals(users.length);
                    o(vnode.children[0].children.length).equals(5);
                    o(vnode.children[0].children[0].text).equals(users[0].name);
                    o(vnode.children[0].children[1].text).equals(users[0].country);
                    o(vnode.children[0].children[2].text).equals(users[0].age);
                    o(vnode.children[1].children[3].children[0].text).equals(users[1].native[0]);
                    o(vnode.children[1].children[3].children[1].text).equals(users[1].native[1]);
                    o(vnode.children[0].children[4].children[0].children[0].text).equals(users[0].learning[0].name);
                    o(vnode.children[0].children[4].children[1].children[0].text).equals(users[0].learning[1].name);
                    o(vnode.children[0].children[4].children[0].children[1].text).equals(users[0].learning[0].level);
                    o(vnode.children[0].children[4].children[1].children[1].text).equals(users[0].learning[1].level);
                })
})
