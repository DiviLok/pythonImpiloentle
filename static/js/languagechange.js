var languages = {
    en: {
        Home: "Home",
        Videos: "Videos",
        Pictures: "Pictures",
        About: "About",
        // Autoplay: "autoplay",
        Dashboard: "Dashboard",
        Login: "Login",
        Logout: "Logout",
        Upload:"Upload",
        Download_Videos_Here: "Download Videos here",
        Dashboard:"Dashboard",
        Upload:"Upload",
        Download:"Download",
        About_1: "The Philani Maternal, Child Health and Nutrition Trust has been addressing maternal, child health and nutrition problems in the informal settlements surrounding Cape Town since 1979. Philani's mandate is sustainable community health, and, over the years, we have developed programmes to meet the needs of the communities we serve. As an organisation we aim to improve health outcomes by combining our skills and resources with the knowledge and resources that exist in the community.",
        About_2: "This web application is a pilot study financed by <a href=\"https://www.sasuf.org/\">SASUF</a> to distribute health information made by students (Magnus Hansson and Carolin Gull) and <a href=\"mailto:william.jobe@hv.se\">Dr. William Jobe</a> at University West in Trollhättan, Sweden as part of a research project headed by Stellenbosch University in cooperation with <a href=\"mailto:linnea.stansert@gmail.com\">Linnea Stansert Katzen</a> and <a href=\"mailto:karlleroux@gmail.com\">Dr. Karl Le Roux</a>. Please feel free to contact any of us with questions and/or comments.",
    },
    xh: {
        Home: "Ekhaya",
        Videos: "Iividiyo",
        Pictures: "Imifanekiso",
        About: "Malunga",
        // Autoplay: "Iyazidlalela",
        Dashboard: "kwideshibhodi",
        Login: "Ngena",
        Logout: "Phuma",
        Upload:"Layisha",
        Download:"Khuphela",
        Download_Videos_Here: "Khuphela iividiyo apha",
        About_1: "I-Philani Maternal, Child Health and Nutrition Trust ibilungisa iingxaki zoomama, impilo yabantwana kunye nesondlo kumatyotyombe angqonge iKapa ukusukela ngo-1979. Umyalelo kaPhilani yimpilo yoluntu ezinzileyo, kwaye, ekuhambeni kweminyaka, siye saqulunqa iinkqubo zokuhlangabezana neemfuno zoluntu esilusebenzelayo. Njengombutho sijolise ekuphuculeni iziphumo zempilo ngokudibanisa izakhono kunye nezibonelelo zethu kunye nolwazi kunye nezibonelelo ezikhoyo kuluntu.",
        About_2: "Esi sicelo sewebhu sisifundo esilingwayo esixhaswa ngemali ngu <a href=\"https://www.sasuf.org/\">SASUF</a> ukusasaza ulwazi lwezempilo olwenziwe ngabafundi (Magnus Hansson kwaye Carolin Gull) kwaye <a href=\"mailto:william.jobe@hv.se\">Dr. William Jobe</a> kwiYunivesithi yaseWest Trollhättan, Sweden njengenxalenye yeprojekthi yophando ekhokelwa Stellenbosch University ngentsebenziswano ne <a href=\"mailto:linnea.stansert@gmail.com\">Linnea Stansert Katzen</a> kwaye <a href=\"mailto:karlleroux@gmail.com\">Dr. Karl Le Roux</a>. Nceda uzive ukhululekile ukuqhagamshelana nabani na kuthi ngemibuzo kunye/okanye izimvo."
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
      if (window.NodeList && !NodeList.prototype.forEach) {
        NodeList.prototype.forEach = Array.prototype.forEach;
    }
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