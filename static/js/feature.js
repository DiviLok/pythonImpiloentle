{
    console.log("test the file");

    let language = window.navigator.language;
    // var lang= document.getElementById("demo").innerHTML = "Browser language: " + language;
    //alert(language);

    (function () {
        console.log("test the file");

        var currentLanguage;
        var section = document.querySelector("section.languagemain");
        var updateLayout = function () {
            currentLanguage = section.getAttribute("lang").toLowerCase();
            section.classList.add(currentLanguage === language ? 'section-anim-rtl' : 'section-anim');
            console.log("test the file");

        }

    })

};

{
    var vid = document.getElementById("bgvid");
    if (window.matchMedia('(prefers-reduced-motion)').matches) {
        vid.removeAttribute("autoplay");
        vid.pause();
        pauseButton.innerHTML = "Paused";
    }
    
    function vidFade() {
      vid.classList.add("stopfade");
    }
    
    vid.addEventListener('ended', function()
    {
    // only functional if "loop" is removed 
    vid.pause();
    // to capture IE10
    vidFade();
    }); 
}

