function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {

            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {

                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );

                break;
            }
        }
    }

    return cookieValue;
}


// ================================
// Back To Top
// ================================

const backToTop =
    document.getElementById("backToTop");

if (backToTop) {

    window.addEventListener("scroll", function () {

        if (window.scrollY > 300) {

            backToTop.classList.add("show");

        } else {

            backToTop.classList.remove("show");

        }

    });


    backToTop.addEventListener("click", function () {

        window.scrollTo({

            top: 0,
            behavior: "smooth"

        });

    });

}


// ================================
// Product Quantity
// ================================

let quantity = 1;

const quantityDisplay =
    document.getElementById("quantity");

const increaseButton =
    document.getElementById("increase");

const decreaseButton =
    document.getElementById("decrease");


if (
    quantityDisplay &&
    increaseButton &&
    decreaseButton
) {

    increaseButton.addEventListener("click", function () {

        quantity++;

        quantityDisplay.textContent =
            quantity;

    });


    decreaseButton.addEventListener("click", function () {

        if (quantity > 1) {

            quantity--;

            quantityDisplay.textContent =
                quantity;

        }

    });

}


// ================================
// Product Add To Cart
// ================================

const cartButton =
    document.getElementById("add-cart");

const cartMessage =
    document.getElementById("cart-message");

const sizeButtons =
    document.querySelectorAll(".size-btn");

let selectedSize = "";


// ================================
// Size Selection
// ================================

sizeButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        sizeButtons.forEach(function(item) {

            item.classList.remove("selected");

        });

        button.classList.add("selected");

        selectedSize =
            button.dataset.size;

        // Clear size warning after selecting
        if (cartMessage) {

            cartMessage.textContent = "";

            cartMessage.classList.remove("show");

        }

    });

});


// ================================
// Small Cart Message
// ================================

function showCartMessage(message) {

    if (!cartMessage) {
        return;
    }

    cartMessage.textContent = message;

    cartMessage.classList.add("show");

}


// ================================
// Check Product Already In Cart
// ================================

if (cartButton) {

    const productId =
        cartButton.dataset.productId;

    fetch(
        "/cart/check/" +
        productId +
        "/"
    )

    .then(function(response) {

        return response.json();

    })

    .then(function(data) {

        if (
            data.success &&
            data.in_cart
        ) {

            cartButton.innerHTML =
                "✓ ADDED TO CART";

            cartButton.classList.add(
                "added-to-cart"
            );

            showCartMessage(
                "✓ In cart · Quantity: " +
                data.quantity
            );

        }

    })

    .catch(function(error) {

        console.error(error);

    });

}


// ================================
// Add Product To Cart
// ================================

if (cartButton) {

    cartButton.addEventListener(
        "click",
        function() {

            const productId =
                cartButton.dataset.productId;

            const quantityValue =
                document.getElementById(
                    "quantity"
                ).textContent;


            // ----------------------------
            // Check Size
            // ----------------------------

            if (!selectedSize) {

                showCartMessage(
                    "Please select a size"
                );

                return;

            }


            // ----------------------------
            // Prepare Data
            // ----------------------------

            const formData =
                new FormData();

            formData.append(
                "product_id",
                productId
            );

            formData.append(
                "size_label",
                selectedSize
            );

            formData.append(
                "quantity",
                quantityValue
            );


            // ----------------------------
            // Disable Button While Saving
            // ----------------------------

            cartButton.disabled = true;


            // ----------------------------
            // Send To Django
            // ----------------------------

            fetch(
                "/cart/add/",
                {

                    method: "POST",

                    headers: {

                        "X-CSRFToken":
                            getCookie(
                                "csrftoken"
                            )

                    },

                    body: formData

                }
            )

            .then(function(response) {

                return response.json();

            })

            .then(function(data) {

                if (data.success) {

                    cartButton.innerHTML =
                        "✓ ADDED TO CART";

                    cartButton.classList.add(
                        "added-to-cart"
                    );


                    showCartMessage(
                        "✓ Added to cart · Quantity: " +
                        quantityValue
                    );


                    // Check actual quantity
                    // from cart after adding

                    fetch(
                        "/cart/check/" +
                        productId +
                        "/"
                    )

                    .then(function(response) {

                        return response.json();

                    })

                    .then(function(cartData) {

                        if (
                            cartData.success &&
                            cartData.in_cart
                        ) {

                            showCartMessage(
                                "✓ In cart · Quantity: " +
                                cartData.quantity
                            );

                        }

                    });

                } else {

                    showCartMessage(
                        data.message
                    );

                }

            })

            .catch(function(error) {

                console.error(error);

                showCartMessage(
                    "Something went wrong"
                );

            })

            .finally(function() {

                cartButton.disabled = false;

            });

        }
    );

}


// ================================
// Always Start Page At Top
// ================================

window.addEventListener("pageshow", function() {

    window.scrollTo(0, 0);

});


// ================================
// Cart Quantity
// ================================

const minusButtons =
    document.querySelectorAll(".quantity-minus");

const plusButtons =
    document.querySelectorAll(".quantity-plus");


function updateCartQuantity(
    cartItemId,
    quantity
) {

    const formData =
        new FormData();

    formData.append(
        "cart_item_id",
        cartItemId
    );

    formData.append(
        "quantity",
        quantity
    );


    fetch(
        "/cart/update-quantity/",
        {

            method: "POST",

            headers: {

                "X-CSRFToken":
                    getCookie(
                        "csrftoken"
                    )

            },

            body: formData

        }
    )

    .then(function(response) {

        return response.json();

    })

    .then(function(data) {

        if (!data.success) {

            alert(data.message);

        }

    })

    .catch(function(error) {

        console.error(error);

        alert("Something went wrong.");

    });

}


// ================================
// Plus Button
// ================================

plusButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        const cartItemId =
            button.dataset.cartItemId;

        const quantityDisplay =
            button.parentElement.querySelector(
                ".item-quantity"
            );

        let quantity =
            parseInt(
                quantityDisplay.textContent
            );

        quantity++;

        quantityDisplay.textContent =
            quantity;

        updateCartQuantity(
            cartItemId,
            quantity
        );

        updateCartTotal();

    });

});


// ================================
// Minus Button
// ================================

minusButtons.forEach(function(button) {

    button.addEventListener("click", function() {

        const cartItemId =
            button.dataset.cartItemId;

        const quantityDisplay =
            button.parentElement.querySelector(
                ".item-quantity"
            );

        let quantity =
            parseInt(
                quantityDisplay.textContent
            );

        if (quantity > 1) {

            quantity--;

            quantityDisplay.textContent =
                quantity;

            updateCartQuantity(
                cartItemId,
                quantity
            );

            updateCartTotal();

        }

    });

});


console.log(
    "CART SCRIPT LOADED - NEW"
);


// ================================
// Cart Price Calculation
// ================================

function updateCartTotal() {

    let subtotal = 0;

    const cartItems =
        document.querySelectorAll(
            ".cart-item"
        );


    cartItems.forEach(function(item) {

        const quantity =
            parseInt(
                item.querySelector(
                    ".item-quantity"
                ).textContent
            );

        const priceElement =
            item.querySelector(
                ".item-total-price"
            );

        const unitPrice =
            parseFloat(
                priceElement.dataset.unitPrice
            );

        const itemTotal =
            unitPrice * quantity;


        priceElement.textContent =
            "₹" +
            itemTotal.toFixed(2);


        subtotal += itemTotal;

    });


    const summaryRows =
        document.querySelectorAll(
            ".summary-row span:last-child"
        );


    if (summaryRows.length >= 1) {

        summaryRows[0].textContent =
            "₹" +
            subtotal.toFixed(2);

    }


    const total =
        document.querySelector(
            ".summary-total span:last-child"
        );


    if (total) {

        total.textContent =
            "₹" +
            subtotal.toFixed(2);

    }

}


updateCartTotal();


// ================================
// Remove Cart Item
// ================================

const removeButtons =
    document.querySelectorAll(
        ".remove-item"
    );


removeButtons.forEach(function(button) {

    button.addEventListener(
        "click",
        function() {

            const cartItemId =
                button.dataset.cartItemId;


            const formData =
                new FormData();

            formData.append(
                "cart_item_id",
                cartItemId
            );


            fetch(
                "/cart/remove/",
                {

                    method: "POST",

                    headers: {

                        "X-CSRFToken":
                            getCookie(
                                "csrftoken"
                            )

                    },

                    body: formData

                }
            )

            .then(function(response) {

                return response.json();

            })

            .then(function(data) {

                if (data.success) {

                    const cartItem =
                        button.closest(
                            ".cart-item"
                        );

                    cartItem.remove();

                    updateCartTotal();

                } else {

                    alert(data.message);

                }

            })

            .catch(function(error) {

                console.error(error);

                alert(
                    "Something went wrong."
                );

            });

        }
    );

});