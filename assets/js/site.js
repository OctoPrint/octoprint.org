$(function() {
  // make code pretty
  window.prettyPrint && prettyPrint();

  // init slick slide shows
  $(".slick-container").slick();

  // init smooth scrolling
  smoothScroll.init();

  // cookie helpers - based on https://stackoverflow.com/a/27370319
  function setCookie(c_name, value, exdays, path) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays === null) ? "" : "; expires=" + exdate.toUTCString()) + ((path === null) ? "" : "; path=" + path) + "; SameSite=Strict";
    document.cookie=c_name + "=" + c_value;
  }
  function getCookie(c_name) {
    var c_value = document.cookie;
    var c_start = c_value.indexOf(" " + c_name + "=");
    if (c_start === -1){
      c_start = c_value.indexOf(c_name + "=");
    }
    if (c_start === -1){
      c_value = null;
    } else {
      c_start = c_value.indexOf("=", c_start) + 1;
      var c_end = c_value.indexOf(";", c_start);
      if (c_end === -1){
        c_end = c_value.length;
      }
      c_value = unescape(c_value.substring(c_start,c_end));
    }
    return c_value;
  }
  function delCookie(name, path) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;' + ((path === null) ? "" : "; path=" + path) + "; SameSite=Strict";
  }

  // scroll sensitive stuff
  var header = $("#navigation").offset().top;
  var evalHeader = function() {
    header = $("#navigation").offset().top;
  };

  var evalScroll = function() {
    var buttons = $(".to-top");
    var navigation = $("#navigation");
    var wrap = $("#wrap");

    var offset = $(window).height() * 0.5;

    var duration = 200;
    var scrollTop = $(this).scrollTop();

    if (scrollTop > header) {
      navigation
          .removeClass("unfixed");
      wrap
          .removeClass("wrap-navbar-top")
          .addClass("wrap-navbar-fixed-top");
    } else {
      navigation
          .addClass("unfixed");
      wrap
          .removeClass("wrap-navbar-fixed-top")
          .addClass("wrap-navbar-top");
    }

    if (scrollTop > offset) {
      buttons.fadeIn(duration);
    } else {
      buttons.fadeOut(duration);
    }

  };
  $(window).scroll(evalScroll);
  evalScroll();

  $("#banner .close-banner").click(function() {
      $("#banner").slideUp({complete: function() {
        evalHeader();
        plausible("Banner closed");
      }});
  });

  if (!getCookie("banner_shown") || /[?&]sb/.test(location.search)) {
    window.setTimeout(function() {
      if (window.innerWidth < 768 && $("div[aria-label='cookieconsent']").is(":visible")) return;
      $("#banner").slideDown({
          complete: function() {
            evalHeader();
            plausible("Banner shown");
          }
      });
      setCookie("banner_shown", true, 14, "/");
    }, 2000);
  }

  if (window.location.pathname === "/support-octoprint/") {
    setCookie("banner_shown", true, 60, "/");
  }
});
