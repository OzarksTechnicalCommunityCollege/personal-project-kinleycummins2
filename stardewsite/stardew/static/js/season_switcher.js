// JavaScript for making a button that will shift which season to view

document.addEventListener("DOMContentLoaded", function () {
  const seasonCards = document.querySelectorAll(".season-card");
  const seasons = ["Spring", "Summer", "Fall", "Winter"];

  // button container
  const nav = document.createElement("div");
  nav.id = "season-nav";

  seasons.forEach(function (season) {
    const btn = document.createElement("button");
    btn.textContent = season;
    btn.dataset.season = season.toLowerCase();
    btn.classList.add("season-btn");

    // Event listener to show only matching card
    btn.addEventListener("click", function () {
      // Update active button
      document.querySelectorAll(".season-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      // Show or hide season cards
      seasonCards.forEach(function (card) {
        if (card.classList.contains(season.toLowerCase())) {
          card.style.display = "";
        } else {
          card.style.display = "none";
        }
      });
    });

    nav.appendChild(btn);
  });

  // Insert the nav before the first season card's parent content
  const firstCard = seasonCards[0];
  firstCard.parentNode.insertBefore(nav, firstCard);

  // Spring is the default season
  document.querySelector('.season-btn[data-season="spring"]').click();
});
