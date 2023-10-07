       // Function to navigate to a new page
       function navigateTo(url) {
        window.location= url;
    }
    function navigateToPage1() {
        // Use window.location to navigate to the desired HTML file
        window.location= 'template/create_form.html';
    }
        // Function to animate the boxes on page load
    function animateBoxes() {
        const boxes = document.querySelectorAll('.box');
        let delay = 0;

        boxes.forEach((box, index) => {
            setTimeout(() => {
                box.classList.add('active');
            }, delay);
            delay += 500; // Adjust the delay between boxes (in milliseconds)
        });
    }

    // Call the animateBoxes function when the page loads
    window.addEventListener('load', animateBoxes);