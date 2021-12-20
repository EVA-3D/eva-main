(function(funcName, baseObj) {
    "use strict";
    // The public function name defaults to window.docReady
    // but you can modify the last line of this function to pass in a different object or method name
    // if you want to put them in a different namespace and those will be used instead of 
    // window.docReady(...)
    funcName = funcName || "docReady";
    baseObj = baseObj || window;
    var readyList = [];
    var readyFired = false;
    var readyEventHandlersInstalled = false;

    // call this when the document is ready
    // this function protects itself against being called more than once
    function ready() {
        if (!readyFired) {
            // this must be set to true before we start calling callbacks
            readyFired = true;
            for (var i = 0; i < readyList.length; i++) {
                // if a callback here happens to add new ready handlers,
                // the docReady() function will see that it already fired
                // and will schedule the callback to run right after
                // this event loop finishes so all handlers will still execute
                // in order and no new ones will be added to the readyList
                // while we are processing the list
                readyList[i].fn.call(window, readyList[i].ctx);
            }
            // allow any closures held by these functions to free
            readyList = [];
        }
    }

    function readyStateChange() {
        if (document.readyState === "complete") {
            ready();
        }
    }

    // This is the one public interface
    // docReady(fn, context);
    // the context argument is optional - if present, it will be passed
    // as an argument to the callback
    baseObj[funcName] = function(callback, context) {
        if (typeof callback !== "function") {
            throw new TypeError("callback for docReady(fn) must be a function");
        }
        // if ready has already fired, then just schedule the callback
        // to fire asynchronously, but right away
        if (readyFired) {
            setTimeout(function() { callback(context); }, 1);
            return;
        } else {
            // add the function and context to the list
            readyList.push({ fn: callback, ctx: context });
        }
        // if document already ready to go, schedule the ready function to run
        // IE only safe when readyState is "complete", others safe when readyState is "interactive"
        if (document.readyState === "complete" || (!document.attachEvent && document.readyState === "interactive")) {
            setTimeout(ready, 1);
        } else if (!readyEventHandlersInstalled) {
            // otherwise if we don't have event handlers installed, install them
            if (document.addEventListener) {
                // first choice is DOMContentLoaded event
                document.addEventListener("DOMContentLoaded", ready, false);
                // backup is window load event
                window.addEventListener("load", ready, false);
            } else {
                // must be IE
                document.attachEvent("onreadystatechange", readyStateChange);
                window.attachEvent("onload", ready);
            }
            readyEventHandlersInstalled = true;
        }
    }
})("docReady", window);


Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        box: {
            version: docsVersion,
            items: {}
        }
    },
    getters: {
        items: state => {
            return state.box.items;
        },
        itemsCount: (state, getters) => {
            return Object.keys(getters.items).length;
        },
        satisfaction: (state, getters) => {
            var satisfaction = {
                drive: false,
                hotend: false,
                endstop: false,
                bed_probe: false,
            };
            for (const [name, item] of Object.entries(getters.items)) {
                for (satisfies of item.satisfies) {
                    satisfaction[satisfies] = true;
                }
            }
            return satisfaction
        },
    },
    mutations: {
        initialiseStore: (store) => {
            if (localStorage.box !== undefined) {
                let box = JSON.parse(localStorage.box);
                if (docsVersion === box.version) {
                    store.box = box;
                } else {
                    console.info("Old version of a box found, purging!");
                    localStorage.removeItem("box");
                }
            }
        },
        add: (state, item) => {
            state.box.items = {...state.box.items, ...item };
            localStorage.setItem("box", JSON.stringify(state.box));
        },
        remove: (state, item_name) => {
            Vue.delete(state.box.items, item_name);
            localStorage.setItem("box", JSON.stringify(state.box));
        }
    }
});

var boxApp = new Vue({
    el: '#boxPage',
    store: store,
    beforeCreate() { this.$store.commit('initialiseStore'); },
    data: {
        satisfiesMap: {
            drive: "Drive",
            hotend: "Hotend",
            endstop: "Endstop",
            bed_probe: "Bed probe",
        }
    },
    filters: {
        join: function(value) {
            if (!value) return ''
            return value.join(', ')
        }
    },
    computed: {
        items() {
            return this.$store.getters.items
        },
        itemsCount() {
            return Object.keys(this.items).length;
        },
        parts() {
            var parts = {};
            for (const [name, item] of Object.entries(this.items)) {
                for (part of item.parts) {
                    if (parts.hasOwnProperty(part.slug)) {
                        parts[part.slug].qty += part.qty;
                    } else {
                        parts[part.slug] = part;
                    }
                }
            }
            return parts;
        },
        satisfaction() {
            return this.$store.getters.satisfaction
        },
        satisfactionList() {
            var satisfcation = [];
            for (const [name, state] of Object.entries(this.satisfaction)) {
                if (state === true) {
                    satisfcation.push(name);
                }
            }
            return satisfcation
        },
        missing() {
            var missing = false;
            for (const [name, state] of Object.entries(this.satisfaction)) {
                if (state === false) {
                    missing = true;
                }
            }
            return missing
        }
    },
    methods: {
        remove(name) {
            this.$store.commit("remove", name)
        }
    }
})

var superboxApp = new Vue({
    el: "#superboxPage",
    store: store,
    beforeCreate() { this.$store.commit('initialiseStore'); },
    data: {
        satisfiesMap: {
            drive: "Drive",
            hotend: "Hotend",
            endstop: "Endstop",
            bed_probe: "Bed probe",
        }
    },
    filters: {
        join: function(value) {
            if (!value) return ''
            return value.join(', ')
        }
    },
    computed: {
        items() {
            return this.$store.getters.items
        },
        itemsCount() {
            return Object.keys(this.items).length;
        },
        parts() {
            var parts = {};
            for (const [name, item] of Object.entries(this.items)) {
                for (part of item.parts) {
                    if (parts.hasOwnProperty(part.slug)) {
                        if (part.qty > parts[part.slug].qty) {
                            parts[part.slug].qty = part.qty;
                        }
                    } else {
                        parts[part.slug] = part;
                    }
                }
            }
            return parts;
        },
        satisfaction() {
            return this.$store.getters.satisfaction
        },
        satisfactionList() {
            var satisfcation = [];
            for (const [name, state] of Object.entries(this.satisfaction)) {
                if (state === true) {
                    satisfcation.push(name);
                }
            }
            return satisfcation
        },
        missing() {
            var missing = false;
            for (const [name, state] of Object.entries(this.satisfaction)) {
                if (state === false) {
                    missing = true;
                }
            }
            return missing
        }
    },
    methods: {
        remove(name) {
            this.$store.commit("remove", name)
        }
    }
});

var boxLink = new Vue({
    el: '#boxLink',
    store: store,
    beforeCreate() { this.$store.commit('initialiseStore'); },
    computed: {
        itemsCount() {
            return this.$store.getters.itemsCount
        }
    }
});

const delay = ms => new Promise(res => setTimeout(res, ms));

Vue.component('email-button', {
    props: ["seconds"],
    template: '#email-button-template',
    data: function () {
        return {
            clicked: false,
            loading: false,
            loaded: false,
            first_name: "pawel",
            last_name: "kucmus",
            href: "",
            seconds_left: 99,
        }
    },
    methods: {
        async load() {
            let seconds = parseInt(this.seconds);
            this.seconds_left = seconds;
            this.loading = true;
            this.clicked = true;
            for (let i=0; i < seconds; i++) {
                await delay(1000);
                this.seconds_left = this.seconds_left - 1;
            }
            this.loading = false;
            this.loaded = true;
            this.href = "mailto:" + this.first_name[0] + this.last_name + "@gmail.com"
        }
    }
});

Vue.component('add-bom-button', {
    props: ['name'],
    template: "#add-to-box-template",
    beforeCreate() { this.$store.commit('initialiseStore');},
    computed: {
        inBox () {
            return this.$store.getters.items.hasOwnProperty(this.name)
        },
    },
    methods: {
        add () {
            var item = {};
            item[this.name] = JSON.parse(atob(this.$slots.default[0].text));
            this.$store.commit('add', item);
        },
    },
});


var drivePage = new Vue({
    el: '#drivePage',
    store: store,
});


var hotendPage = new Vue({
    el: '#hotendPage',
    store: store,
});


var addonPage = new Vue({
    el: '#addonPage',
    store: store,
});


var page = new Vue({
    el: '#Page',
});

docReady(function() {
    window.CI360.init();
    var tables = document.querySelectorAll("article table");
    tables.forEach(function(table) {
        new Tablesort(table);
    })
});
