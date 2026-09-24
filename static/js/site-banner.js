document.addEventListener("DOMContentLoaded", function(event) {
    // cookie helpers - based on https://stackoverflow.com/a/27370319
    function setCookie(c_name, value, exdays, path) {
        var exdate = new Date();
        exdate.setDate(exdate.getDate() + exdays);
        var c_value =
            escape(value) +
            (exdays === null ? "" : "; expires=" + exdate.toUTCString()) +
            (path === null ? "" : "; path=" + path) +
            "; SameSite=Strict";
        document.cookie = c_name + "=" + c_value;
    }
    function getCookie(c_name) {
        var c_value = document.cookie;
        var c_start = c_value.indexOf(" " + c_name + "=");
        if (c_start === -1) {
            c_start = c_value.indexOf(c_name + "=");
        }
        if (c_start === -1) {
            c_value = null;
        } else {
            c_start = c_value.indexOf("=", c_start) + 1;
            var c_end = c_value.indexOf(";", c_start);
            if (c_end === -1) {
                c_end = c_value.length;
            }
            c_value = unescape(c_value.substring(c_start, c_end));
        }
        return c_value;
    }
    function delCookie(name, path) {
        document.cookie =
            name +
            "=; expires=Thu, 01 Jan 1970 00:00:01 GMT;" +
            (path === null ? "" : "; path=" + path) +
            "; SameSite=Strict";
    }

    const banner = document.getElementById("banner");
    if (!banner) return;

    const closeButton = document.querySelector("#banner a.site-banner__close");
    closeButton.addEventListener("click", () => {
        banner.classList.remove("active");
    })

    if (window.location.pathname === "/support-octoprint/") {
        setCookie("banner_shown", true, 60, "/");
    }

    if (!getCookie("banner_shown") || /[?&]sb/.test(location.search)) {
        banner.style.display = "flex";
        window.setTimeout(() => {
            banner.classList.add("active");
            setCookie("banner_shown", true, 14, "/");
        }, 2000);
    }
});
