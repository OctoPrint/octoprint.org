(function() {
    var placement = new URLSearchParams(location.search).get("placement");
    var po = document.createElement("script");
    po.type = "text/javascript";
    po.async = true;
    po.src = "//cdn.carbonads.com/carbon.js?serve=CK7DT2QE&placement=" + placement;
    po.id = "_carbonads_js";
    var s = document.currentScript;
    s.parentNode.insertBefore(po, s);
})();