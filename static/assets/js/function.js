const monthNames = [
  "Jan",
  "Feb",
  "Mar",
  "April",
  "May",
  "June",
  "July",
  "Aug",
  "Sept",
  "Oct",
  "Now",
  "Dec",
];

$("#commentForm").submit(function (e) {
  e.preventDefault();

  let dt = new Date();
  let time =
    dt.getDay() + " " + monthNames[dt.getUTCMonth()] + ", " + dt.getFullYear();

  $.ajax({
    data: $(this).serialize(),

    method: $(this).attr("method"),

    url: $(this).attr("action"),

    dataType: "json",

    success: function (res) {
      console.log("Comment saved to DB...");
      if (res.bool == true) {
        $("#review-res").html("Review Added Successfully");
        $(".hide-comment-form").hide();
        $(".add-review").hide();

        let _html =
          '<div class="single-comment justify-content-between d-flex mb-30">';
        _html += '<div class="user justify-content-between d-flex">';
        _html += '<div class="thumb text-center">';
        _html += '<img src="assets/imgs/blog/author-2.png" alt="" />';
        _html +=
          '<a href="#" class="font-heading text-brand"> ' +
          res.context.user +
          " </a>";
        _html += "</div>";

        _html += '<div class="desc">';
        _html += '<div class="d-flex justify-content-between mb-10">';
        _html += '<div class="d-flex align-items-center">';
        _html += '<span class="font-xs text-muted"> ' + time + " </span>";
        _html += "</div>";

        for (var i = 1; i < res.context.rating; i++) {
          _html += '<i class="fas fa-star text-warning"> </i>';
        }
        _html += "</div>";
        _html += '<p class="mb-10"> ' + res.context.review + " </p>";
        _html += "</div>";
        _html += "</div>";
        _html += "</div>";

        $(".comment-list").prepend(_html);
      }
    },
  });
});

$(document).ready(function () {
  $(".filter-checkbox, #price-filter-btn").on("click", function () {
    console.log("A checkbox have been clicked");

    let filter_object = {};

    let min_price = $("#max_price").attr("min");
    let max_price = $("#max_price").val();

    filter_object.min_price = min_price;
    filter_object.max_price = max_price;

    $("filter-checkbox").each(function () {
      let filter_value = $(this).val();
      let filter_key = $(this).data("filter");

      // console.log("filter value is:", filter_value);
      // console.log("filter key is:", filter_key)

      filter_object[filter_key] = Array.from(
        document.querySelectorAll(
          "input[data-filter=" + filter_key + "]:checked"
        )
      ).map(function (element) {
        return element.value;
      });
    });
    console.log("filter object is: ", filter_object);
    $.ajax({
      url: "/filter-products",
      data: filter_object,
      dataType: "json",
      beforeSend: function () {
        console.log("Trying to filter product...");
      },
      success: function (response) {
        console.log(response);
        console.log("Data filtered successfully...");
        $("#filtered-product").html(response.data);
      },
    });
  });

  $("#max_price").on("blur", function () {
    let min_price = $(this).attr("min");
    let max_price = $(this).attr("max");
    let current_price = $this().val();

    // console.log('current price is: ', current_price)
    // console.log('Max price is: ', max_price)
    // console.log('min price is: ', min_price)

    if (
      current_price < parseInt(min_price) ||
      current_price > parseInt(max_price)
    ) {
      min_price = Math.round(min_price * 100) / 100;
      max_price = Math.round(max_price * 100) / 100;

      alert("Price must between $" + min_price + "and $" + max_price);
      $(this).val(min_price);
      $("#range").val(min_price);

      $(this).focus();

      return false;
    }
  });
});

$(".add-to-cart-btn").on("click", function () {
  let this_val = $(this);
  let index = this_val.attr("data-index");

  let quantity = $(".product-quantity-" + index).val();
  let product_title = $(".product-title-" + index).val();
  let product_id = $(".product-id-" + index).val();
  let product_price = $(".current-product-price-" + index).text();
  let product_pid = $(".product-pid-" + index).val();
  let product_image = $(".product-image-" + index).val();

  $.ajax({
    url: "/add-to-cart",
    data: {
      'id': product_id,
      'pid': product_pid,
      'image': product_image,
      'qty': quantity,
      'title': product_title,
      'price': product_price,
    },
    dataType: "json",
    beforeSend: function () {
      console.log("product added to cart");
    },
    success: function (response) {
      this_val.html("✓");
      $(".cart-items-count").text(response.totalcartitems);
    },
  });
});

$(".delete-product").on("click", function () {
  let product_id = $(this).attr("data-product");
  let this_val = $(this);

  $.ajax({
    url: "/delete-from-cart",
    data: {
      id: product_id,
    },
    dataType: "json",
    beforeSend: function () {
      this_val.hide();
    },
    success: function (response) {
      this_val.show();
      $(".cart-items-count").text(response.totalcartitems);
      $("#cart-list").html(response.data);
    },
  });
});


$(".update-product").on("click", function () {
    let product_id = $(this).attr("data-product");
    let this_val = $(this);
    let product_quantity = $(".product-qty-"+product_id).val()
  
    $.ajax({
      url: "/update-cart",
      data: {
        'id': product_id,
        'qty': product_quantity
      },
      dataType: "json",
      beforeSend: function () {
        this_val.hide();
      },
      success: function (response) {
        this_val.show();
        $(".cart-items-count").text(response.totalcartitems);
        $("#cart-list").html(response.data);
      },
    });
  });


$(document).on("click", ".make-default-address", function(){
  let id = $(this).attr("data-address-id")
  let this_val = $(this)

  $.ajax({
    url: "/make-default-address",
    data: {
      "id":id
    },
    dataType: "json",
    success: function(response){
      console.log("address made default")
      if (response.boolean == true) {
        $(".check").hide()
        $(".action_btn").show()

        $(".check"+id).show()
        $(".button"+id).hide()
      }
    }
  })

$(document).on("click", ".add-to-wishlist", function(){
  let product_id = $(this).attr("data-product-item")
  let this_val = $(this)

  $.ajax({
    url: "/add-to-wishlist",
    data: {
      "id": product_id
    },
    dataType: "json",
    beforeSend: function() {
      this_val.html('done')
    },
    success: function(response) {
      this_val.html('done')
      if(response.bool === true) {
        console.log('Added to wishlist')
      }
    }
  })
})

$(document).on("click", ".delete-wishlist-product", function(){
  let wishlist_id = $(this).attr("data-wishlist-product")
  let this_val = $(this)

  $.ajax({
    url: "/remove-from-wishlist",
    data: {
      "id": wishlist_id
    },
    dataType: "json",
    beforeSend: function(){
      console.log("deleting product from wishlist")
    },
    success: function(response){
      $("#wishlist-list").html(response.data)
    }
  })
})

$(document).on("submit", "#contact-form-ajax", function(e){
  e.preventDefault()
  console.log("Submitted")

  let full_name = $("#full_name").val()
  let email = $("#email").val()
  let phone = $("#phone").val()
  let subject = $("#subject").val()
  let message = $("#message").val()

  $.ajax({
    url: "/ajax-contact-form",
    data: {
      "full_name": full_name,
      "email": email,
      "phone": phone,
      "subject": subject,
      "message": message
    },
    dataType: "json",
    beforeSend:  function(){
      console.log("Sending data to server")
    },
    success: function(res){
      console.log("Sent data to server")
      // $("#contact-form-ajax").hide()
    }
  })
})

})



// $('.add-to-cart-btn').on("click", function(){
//     let quantity = $('#product-quantity').val()
//     let product_title = $('.product-title').val()
//     let product_id = $('.product-id').val()
//     let product_price = $('#current-product-price').text()
//     let this_val = $(this)

//     $.ajax({
//         url: '/add-to-cart',
//         data: {
//             'id': product_id,
//             'qty': quantity,
//             'title': product_title,
//             'price': product_price
//         },
//         dataType: 'json',
//         beforeSend: function() {
//             console.log('product added to cart')
//         },
//         success: function(response){
//             this_val.html('product added to cart')
//             $(".cart-items-count").text(response.totalcartitems)
//         }
//     })
// })
