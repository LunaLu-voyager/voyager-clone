(function () {
  var header = document.querySelector(".site-header");
  var menuBtn = document.querySelector(".menu-btn");
  var nav = document.querySelector(".nav");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 40);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      nav.classList.toggle("open");
      menuBtn.textContent = nav.classList.contains("open") ? "\u00d7" : "\u2630";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        menuBtn.textContent = "\u2630";
      }
    });
  }
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var btn = form.querySelector("button[type=submit]");
      var old = btn.textContent;
      btn.textContent = btn.getAttribute("data-done") || "\u63d0\u4ea4\u6210\u529f";
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = old;
        btn.disabled = false;
        form.reset();
      }, 2400);
    });
  }
})();

  var vbox = document.querySelector(".video-box");
  var vbtn = document.querySelector(".video-box .play-btn");
  var vvid = document.querySelector(".video-box video");
  if (vbox && vbtn && vvid) {
    vbtn.addEventListener("click", function () {
      vbox.classList.add("playing");
      vvid.setAttribute("controls", "true");
      vvid.play().catch(function(){});
    });
    vvid.addEventListener("pause", function () {
      if (vvid.currentTime === 0 || vvid.ended) { vbox.classList.remove("playing"); }
    });
  }

  var fHeads = document.querySelectorAll(".fold-head");
  fHeads.forEach(function (fHead) {
    var fBody = fHead.nextElementSibling;
    if (!fBody || !fBody.classList.contains("fold-body")) return;
    fHead.addEventListener("click", function () {
      var open = fBody.classList.toggle("open");
      fHead.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });


  var hcs = document.querySelectorAll(".honor-carousel");
  hcs.forEach(function (hc) {
    var slides = hc.querySelectorAll(".hc-slide");
    var dots = hc.querySelectorAll(".hc-dot");
    if (!slides.length) return;
    var cur = 0;
    var timer = null;
    function go(n) {
      slides[cur].classList.remove("active");
      if (dots[cur]) dots[cur].classList.remove("active");
      cur = (n + slides.length) % slides.length;
      slides[cur].classList.add("active");
      if (dots[cur]) dots[cur].classList.add("active");
    }
    function play() { timer = setInterval(function () { go(cur + 1); }, 4000); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    var prev = hc.querySelector(".hc-prev");
    var next = hc.querySelector(".hc-next");
    if (prev) prev.addEventListener("click", function () { stop(); go(cur - 1); play(); });
    if (next) next.addEventListener("click", function () { stop(); go(cur + 1); play(); });
    dots.forEach(function (d, i) {
      d.addEventListener("click", function () { stop(); go(i); play(); });
    });
    play();
  });
