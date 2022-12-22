
// function playtrack() {
//     var track = document.querySelector("#"+this.dataset.ref);
//     track.play();
//     }
//     function triggertrack(element) {
//     element.addEventListener('mouseover', playtrack, false);
//     }
//     var musictriggers = [].slice.call(document.querySelectorAll("#equalizer audio"));
//     musictriggers.forEach(triggertrack);



Audio.prototype.play = (function(play) {
    return function () {
      var audio = this,
          args = arguments,
          promise = play.apply(audio, args);
      if (promise !== undefined) {
        promise.catch(_ => {
          // Autoplay was prevented. This is optional, but add a button to start playing.
          var el = document.createElement("button");
          el.innerHTML = "Play";
          el.addEventListener("click", function(){play.apply(audio, args);});
          this.parentNode.insertBefore(el, this.nextSibling)
        });
      }
    };
    })(Audio.prototype.play);
    
    // Try automatically playing our audio via script. This would normally trigger and error.
    document.getElementById('MyAudioElement').play()