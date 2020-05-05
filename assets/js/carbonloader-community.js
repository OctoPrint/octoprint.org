(function() {
    if (document.getElementById("_carbonads_js") === null && document.getElementById("carbonads") === null) {
        var serve = "CK7DT2QE";
        var placement = "discourseoctoprintorg";

        var po = document.createElement("script");
        po.type = "text/javascript";
        po.async = true;
        po.src = "//cdn.carbonads.com/carbon.js?serve=" + serve + "&placement=" + placement;
        po.id = "_carbonads_js";

        var s = document.currentScript;
        s.parentNode.insertBefore(po, s);
    }
})();
