// Function to show the product details overlay
function showProductDetails(productId) {
    // Hide all the product details containers
    var productContainers = document.getElementsByClassName("product-container");
    for (var i = 0; i < productContainers.length; i++) {
        productContainers[i].style.display = "none";
    }

    // Show the overlay
    document.getElementById("product-details-overlay").style.display = "block";
    // Show the respective product details container
    document.getElementById("product-details-" + productId).style.display = "block";
}

// Function to hide the product details overlay
function hideProductDetails() {
    // Hide the overlay
    document.getElementById("product-details-overlay").style.display = "none";
    // Hide all the product details containers
    var productContainers = document.getElementsByClassName("product-container");
    for (var i = 0; i < productContainers.length; i++) {
        productContainers[i].style.display = "none";
    }
}