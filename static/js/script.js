
//for preloader

window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        preloader.style.display = 'none';
    }
});

document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Retrieve form data
    const input1 = document.getElementById('input1').value;
    const input2 = document.getElementById('input2').value;
    const input3 = document.getElementById('input3').value;

    // Perform prediction (this is where you'd integrate your machine learning model)
    const prediction = `Predicted Disease: ${input1}, ${input2}, ${input3}`; // Replace this with actual prediction logic

    // Display the result
    document.getElementById('result').innerText = prediction;
});
 

$(document).ready(function(){
    $("#carouselExampleIndicators").owlCarousel({
        items: 1, // Number of items to display
        loop: true, // Loop through items
        margin: 10, // Margin between items
        autoplay: true, // Enable autoplay
        autoplayTimeout: 3000, // Autoplay interval (3 seconds)
        autoplayHoverPause: true, // Pause on hover
        nav: true, // Show next/prev buttons
        dots: true // Show pagination dots
    });
});

    // Form submission logic
    $("#predictionForm").on("submit", function(event) {
        event.preventDefault();
        var input1 = $("#input1").val();
        var input2 = $("#input2").val();
        var input3 = $("#input3").val();
        
        $("#result").html("Inputs received: " + input1 + ", " + input2 + ", " + input3);
    });



document.getElementById("book-appointment-btn").addEventListener("click", function(event) {
    event.preventDefault();
    document.querySelector("#appointment").scrollIntoView({ behavior: "smooth" });
});



