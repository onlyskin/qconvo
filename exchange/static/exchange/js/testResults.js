o.spec("Results", function() {
        o("returns a div", function() {
                    var vnode = Results.view()

                    o(vnode.tag).equals("div")
                    // o(vnode.children.length).equals(1)
                    // o(vnode.children[0].tag).equals("#")
                    // o(vnode.children[0].children).equals("Hello world")
                })
})
