// Set the date we're counting down to (January 1, next year)
  const countDownDate = new Date(new Date().getFullYear() + 1, 0, 1, 0, 0, 0, 0).getTime();

  // Update the countdown every 1 second
  const x = setInterval(function() {
    // Get the current date and time
    const now = new Date().getTime();

    // Calculate the time remaining
    const distance = countDownDate - now;

    // Calculate days, hours, minutes, and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the countdown in the "countdown" div
    document.getElementById("countdown").innerHTML = "<span class = day>" + days + "</span" + "<span class = kun>" + "-kun " + "</span>" + "<span class = hours>" + hours + "</span>" + "<span class = soat>" + "-soat " + "</span>" + "<span class = minutes>" + minutes + "</span>" + "<span class = minut>" + "-minut " + "</span>" + "<span class = seconds>" + seconds + "</span>" + "<span class = sekund>"  + "-sekund " + "</span>";

    // If the countdown is over, display a message
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("countdown").innerHTML = "Happy New Year!";
    }
  }, 1000);