var languages={en:{Home:"home",Videos:"videos",Pictures:"pictures",About:"about",Autoplay:"autoplay",Download_Videos_Here:"Download Videos here"},xh:{Home:"Ekhaya",Videos:"Iividiyo",Pictures:"Imifanekiso",About:"Malunga",Autoplay:"Iyazidlalela",Download_Videos_Here:"Khuphela iividiyo apha"}};!function(){var e,t=!1,o=document.querySelector("section.main"),a=function(){t=!0,e=o.getAttribute("lang").toLowerCase(),languages[e]||(console.warn(e+": this language is not supported."),e="en"),o.querySelectorAll("[data-field]").forEach((function(t){const o=t.getAttribute("data-field");languages[e][o]?t.textContent=languages[e][o]:console.warn("Error: Field with type '"+o+"' is not supported.")})),setTimeout((function(){o.classList.remove("section-anim"),o.classList.remove("section-anim-rtl"),t=!1}),500)};document.querySelector("button.change-language").onclick=function(){if(!t){if("en"===e)return o.setAttribute("lang","xh"),void a();o.setAttribute("lang","en"),a()}},o.style.display="inline",a()}();