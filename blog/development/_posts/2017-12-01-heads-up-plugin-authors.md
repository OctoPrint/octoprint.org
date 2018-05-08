---

layout: post
title: "Heads-up plugin authors! Potentially breaking change with 1.3.6"
author: foosel
date: 2017-12-01 10:15:00 +0100
excerpt: A change to solve issues with plugins bundling JS assets causing interference with others  might 
    cause errors for some plugins that go a bit further than just run-off-the-mill view models. Read on 
    to learn if your maintained plugin might be affected and if so what to do against that.
comments: false

---

A change to solve issues with plugins bundling JS assets that cause interference with other plugins (e.g. through
the declaration of `"use strict"`) and in general to add better isolation and error handling might cause errors 
for some plugins that go beyond your run-off-the-mill view model and also implicitly declare new globals. 

This post will tell you what will change, what plugins are even affected and how to quickly fix the possible issues with a 
simple plugin update.

### What will change?

OctoPrint by default will no longer bundle the JS assets provided by plugins just one after the other like this:

``` javascript
/* contents of plugin_a_1.js */

;

/* contents of plugin_a_2.js */

;

/* contents of plugin_b.js */

;

/* and so on */
```

Instead it will wrap each plugin's assets into its own IIFE (immediately invoked function expression) and 
try-catch-block to isolate it better and thus reduce potential issues like unexpectedly enabled strict mode
or other such hard to debug issues:

``` javascript
(function() {
    try {
        // source: plugin/a/plugin_a_1.js
        /* contents of plugin_a_1.js */
        
        ; 
        
        // source: plugin/a/plugin_a_2.js
        /* contents of plugin_a_2.js */
        
        ;
    } catch (error) {
        log.error("Error in JS assets for plugin a:", (error.stack || error));
    }
})();
(function() {
    try {
        // source: plugin/b/plugin_b.js
        /* contents of plugin_b.js */
        
        ; 
        
    } catch (error) {
        log.error("Error in JS assets for plugin b:", (error.stack || error));
    }
})();
/* and so on */
```

The way scoping in JavaScript works, this means that any functions or variables that you declare in your JS file
without a scope limiting keyword like e.g. `var` will no longer just be pushed to the global namespace but instead
only be declared locally inside the IIFE. That means they won't be accessible globally either unless you explicitly
attach them to `window` yourself. This is not a problem (especially not if you did it accidentally) unless you try 
to use those identifiers outside of your JS files, e.g. in a template your plugin also provides.

### What plugins are affected?

Only `AssetPlugin` plugins whose JavaScript files contain implicit global declarations of functions or variables 
they then try to access outside of their JavaScript files are affected. 

Let's look at an example. If you have something like this `myHelper` function in your plugin's JS asset: 

``` javascript
$(function() {
    function YourViewModel(parameters) {
        var self = this;
        self.value = ko.observable("value");
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: YourViewModel,
        dependencies: [],
        elements: ["#mySpan"]
    });
});

function myHelper(value) {
    return "formattedValue: " + value;
}
```

and then use it in your plugin's template:

``` html
<span id="mySpan" data-bind="text: myHelper(value)"></span>
```

then your plugin will run into an error with OctoPrint 1.3.6 since your `myHelper` will no longer be automatically 
available on the global namespace and an error will be thrown when your view model is bound to your template.

If you just accidentally forgot to make your `myHelper` function local and are only using it inside your own JS
assets however there won't be any problems.

### How do I solve this?

#### The quick and dirty solution

Instead of implicitly declaring your global function or variable that you need outside of your JS assets, 
do it explicitly by setting it on `window`:

``` javascript
$(function() {
    function YourViewModel(parameters) {
        var self = this;
        self.value = ko.observable("value");
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: YourViewModel,
        dependencies: [],
        elements: ["#mySpan"]
    });
});

window.myHelper = function(value) {
    return "formattedValue: " + value;
}
```

That's fully backwards compatible to earlier versions of OctoPrint too - you are really just doing something
explicitly that before you were doing implicitly.

#### A possibly cleaner solution

**But even better yet** is to avoid global functions in general and instead see if you can't adjust your plugin 
to instead bind to a helper function or even a `computed`/`pureComputed` defined on your view model if it's bound to 
the template in question anyhow:

``` javascript
$(function() {
    function YourViewModel(parameters) {
        var self = this;
        self.value = ko.observable("value");
        
        self.formattedValue = ko.pureComputed(function() {
            return "formattedValue: " + self.value();
        });
        
        /* OR MAYBE */
        
        self.myHelper = function(value) {
            return "formattedValue: " + value;
        }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: YourViewModel,
        dependencies: [],
        elements: ["#mySpan"]
    });
});
``` 

``` html
<span id="#mySpan" data-bind="text: formattedValue"></span>

<!-- OR MAYBE -->

<span id="#mySpan" data-bind="text: myHelper(value)"></span>
```

#### And then?

**In any case**, if your plugin is affected, just push an update of your plugin with this change in place and 
once your users update your plugin all should be fine again.

<div class="alert alert-warning">
If your plugin is affected but cannot update itself automatically due to issues with its software update config, please
fix that as well, then 
<a href="https://github.com/OctoPrint/plugins.octoprint.org/issues" target="_blank">open an issue on the plugin repository</a>
and request the push of a notification about your plugin to your users to tell them that they should update manually. Don't
forget to state what plugin and what version(s) the notification should be sent for!
</div>

### What can my users do until I've updated my plugin?

Since it's only logical that not all affected plugins will already be adjusted at public release of OctoPrint 1.3.6,
I've added a small feature toggle that allows to force the old bundling approach if set:

<a href="/assets/img/blog/2017-12/2017-12-01-legacy-setting.png" data-lightbox="{{ page.id }}" data-title="Settings > Features > Enable legacy plugin asset bundling"><img alt="Settings > Features > Enable legacy plugin asset bundling" src="/assets/img/blog/2017-12/2017-12-01-legacy-setting.png"></a>

To make plugins that broke due to the change work again, simply checking 
"Settings > Features > Enable legacy plugin asset bundling", saving and restarting the server will have 
OctoPrint use the old method of asset bundling again and work around the problem (with the downside of having the
same potential compatibility issues with other plugins again that made it necessary to introduce this change in the
first place).

Please note however that this flag will only be available for a limited period of time. I currently plan to remove it
again in OctoPrint 1.3.8. This should leave you enough time to do the minimal adjustment 
necessary in your plugin.

### Why was this introduced now?

Some users and plugin authors started running into seriously hard to debug problems caused by other plugins 
declaring strict mode or otherwise interfering. That's something that in all likelihood would have gotten only 
more worse the longer a stricter isolation of plugins wasn't in place.

Considering that the change needed to get affected plugins going again is a very simple on, not many plugins should
even be affected and a better isolation and error handling has huge benefits, I decided that the advantages here
certainly outweigh the disadvantages.

If you want even more details, feel free to read the [related ticket](https://github.com/foosel/OctoPrint/issues/2200) 
that led to the introduction of this change.
