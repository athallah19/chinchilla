const nav = document.querySelector("#nav");

const onScroll = (event) => {
  const scrollPosition = event.target.scrollingElement.scrollTop;
  if (scrollPosition > 10) {
    if (!nav.classList.contains("scrolled-down")) {
      nav.classList.add("scrolled-down");
    }
  } else {
    if (nav.classList.contains("scrolled-down")) {
      nav.classList.remove("scrolled-down");
    }
  }
};

// document.addEventListener("scroll", onScroll);

// document.onreadystatechange = function () {
//   if (document.readyState !== "complete") {
//     document.querySelector(
//       "body").style.visibility = "hidden";
//     document.querySelector(
//       "#loader").style.visibility = "visible";
//   } else {
//     document.querySelector(
//       "#loader").style.display = "none";
//     document.querySelector(
//       "body").style.visibility = "visible";
//   }
// };

