function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

function addToCart(pizza_id, size) {
  $.ajax({
      url: "/add_to_cart/",
      type: "POST",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      data: {
          "pizza_id": pizza_id,
          "size": size
      },
      dataType: "json",
      success: () => {
        alert("Dodano do koszyka");
      },
      error: () => {
        alert("Coś poszło nie tak...");
      }
    });  
  }

function deleteFromCart(order_item_id) {
  $.ajax({
      url: "/delete_item/",
      type: "POST",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      data: {
          "order_item_id": order_item_id,
      },
      dataType: "json",
      success: () => {
        alert("Usunięto");
        location.reload();
      },
      error: () => {
        alert("Coś poszło nie tak...");
      }
    });  
}

function completeOrder(order_id) {
    $.ajax({
        url: "/make_order_done/",
        type: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
          },
        data: {
            "order_id": order_id,
        },
        dataType: "json",
        success: () => {
          alert("Oznaczono jako dostarczone");
          location.reload();
        },
        error: () => {
          alert("Coś poszło nie tak...");
        }
      });  
  }