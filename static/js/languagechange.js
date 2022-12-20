var languages = {
    en: {
        Home: "home",
        Videos: "videos",
        Pictures: "pictures",
        About: "about",
        Autoplay: "autoplay",
        Download_Videos_Here: "Download Videos here"
    },
    xh: {
        Home: "Ekhaya",
        Videos: "Iividiyo",
        Pictures: "Imifanekiso",
        About: "Malunga",
        Autoplay: "Iyazidlalela",
        Download_Videos_Here: "Khuphela iividiyo apha"
    }
  };
  
  (function() {
    var currentLanguage;
    var isButtonBlocked = false;
    var section = document.querySelector("section.main");
    var updateLayout = function() {
      isButtonBlocked = true;
      currentLanguage = section.getAttribute("lang").toLowerCase();
      //section.classList.add(currentLanguage === 'xh' ? 'section-anim-rtl' : 'section-anim');
  
      if (!languages[currentLanguage]) {
        console.warn(currentLanguage + ": this language is not supported.");
        currentLanguage = "en";
      }
  
      var fields = section.querySelectorAll("[data-field]");
      fields.forEach(function(el) {
        const type = el.getAttribute("data-field");
  
        if (!languages[currentLanguage][type]) {
          console.warn("Error: Field with type '" + type + "' is not supported.");
          return;
        }
  
        el.textContent = languages[currentLanguage][type];
      });
      setTimeout(function() {
        section.classList.remove('section-anim');
        section.classList.remove('section-anim-rtl');
        isButtonBlocked = false;
      }, 500);
    };
  
    var changeBtn = document.querySelector("button.change-language");
    changeBtn.onclick = function() {
      if (isButtonBlocked) {
        return;
      }
      
      if (currentLanguage === "en") {
        section.setAttribute("lang", "xh");
        //section.style.direction = "rtl"
        document.cookie = "lang_cookie=xh";
        updateLayout();
        return;
      }
      section.setAttribute("lang", "en");
      //section.style.direction = "ltr"
      document.cookie = "lang_cookie=en";
      updateLayout();
    };
    section.style.display='inline';
    //section.style.display = 'block';
    updateLayout();

    onload = function(){
    var lang_cookie = getCookie('lang_cookie');
    section.setAttribute('lang', lang_cookie);
    updateLayout();
    }
  })();
  

  function getCookie(name) {
    // get the list of cookies
    var cookies = document.cookie.split(';');
    // loop through the cookies
    for (var i = 0; i < cookies.length; i++) {
      // get the current cookie
      var cookie = cookies[i];
      // remove leading whitespace
      while (cookie.charAt(0) == ' ') {
        cookie = cookie.substring(1);
      }
      // check if the cookie name matches the specified name
      if (cookie.indexOf(name + "=") == 0) {
        // get the value of the cookie
        var value = cookie.substring(name.length + 1);
        // return the value
        return value;
      }
    }
    // if no matching cookie is found, return default 'xh'
    return 'xh';
  }