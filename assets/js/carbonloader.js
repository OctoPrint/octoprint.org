(function() {
    if (document.currentScript
            && document.getElementById("_carbonads_js") === null
            && document.getElementById("carbonads") === null) {
        var params = new URLSearchParams(location.search);
        var serve = document.currentScript.getAttribute("serve") || params.get("serve");
        var placement = document.currentScript.getAttribute("placement") || params.get("placement");

        var po = document.createElement("script");
        po.type = "text/javascript";
        po.async = true;
        po.src = "//cdn.carbonads.com/carbon.js?serve=" + serve + "&placement=" + placement;
        po.id = "_carbonads_js";

        var s = document.currentScript;
        s.parentNode.insertBefore(po, s);
    }
})();
