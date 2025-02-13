visibleMenu = document.querySelectorAll(".visible");
hiddenMenu = document.querySelectorAll(".hidden");
lasthiddenMenu = document.querySelectorAll(".last_hidden");



if (window.innerWidth >= 768) {
visibleMenu.forEach((item) => {
    item.addEventListener("mouseover", () => {
      // filter함수를 사용하여 hiddenMenu 중 key값이 item의 key값과 같은 것만 보여줌
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "block";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "block";
      });
    });
  });

  visibleMenu.forEach((item) => {
    item.addEventListener("mouseout", () => {
      // filter함수를 사용하여 hiddenMenu 중 key값이 item의 key값과 같은 것만 보여줌
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "none";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "none";
      });
    });
  });

  
  hiddenMenu.forEach((item) => {
    item.addEventListener("mouseover", () => {
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "block";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      showa.forEach((h) => {
        h.style.display = "block";
      });
    });
  });
  
  hiddenMenu.forEach((item) => {
    item.addEventListener("mouseout", () => {
      show = Array.from(hiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });

      show.forEach((h) => {
        h.style.display = "none";
      });

      showa = Array.from(lasthiddenMenu).filter((menu) => {
        return item.attributes.key.value === menu.attributes.key.value;
      });
      
      showa.forEach((h) => {
        h.style.display = "none";
      });
    });
  });
}







  document.addEventListener("DOMContentLoaded", () => {
    const menu = document.querySelector(".taskbar-container");
    const hamburger = document.querySelector(".hamburger");

    hamburger.addEventListener("click", () => {
        menu.classList.toggle("active");
    });

    document.addEventListener("click", (event) => {
        if (!menu.contains(event.target) && event.target !== hamburger) {
            menu.classList.remove("active");
        }
    });
});


  