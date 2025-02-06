visibleMenu = document.querySelectorAll(".visible");
hiddenMenu = document.querySelectorAll(".hidden");

visibleMenu.forEach((item) => {
  item.addEventListener("mouseover", () => {
    // filter함수를 사용하여 hiddenMenu 중 key값이 item의 key값과 같은 것만 보여줌
    show = Array.from(hiddenMenu).filter((menu) => {
      return item.attributes.key.value === menu.attributes.key.value;
    });
    show.forEach((h) => {
      h.style.display = "flex";
    });
    
  });
});

visibleMenu.forEach((item) => {
  item.addEventListener("mouseout", () => {
    show = Array.from(hiddenMenu).filter((menu) => {
      return item.attributes.key.value === menu.attributes.key.value;
    });
    show.forEach((h) => {
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
      h.style.display = "flex";
    });
  });
});

hiddenMenu.forEach((item) => {
  item.addEventListener("mouseout", () => {
    show = Array.from(hiddenMenu).filter((menu) => {
      return item.attributes.key.value === menu.attributes.key.value;
    });
    show.forEach((h) => {
      h.style.display = "flex";
    });
  });
});