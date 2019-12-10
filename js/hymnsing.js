function adminLogin() {
  var pw = $("#input").val();
  $.post("/login", {
    "password": pw
  }).done(function () {
    window.location.href = "/";
  }).fail(function () {
    alert("Invalid login");
  });
}

function addHymn(num) {
  var date = $("#datepicker").val();
  if (Date.parse(date)) {
    if (Date.parse(date) < new Date()) {
      $.post("/addHymn", {
        date: date,
        hymn: num
      }).done(function () {
        // if ($("table").children().size() == 0) {
        //   $("table").html(`
        //     <tr>
        //       <td><a href="/history#${date.toISOString()}">${date}</a></td>
        //     </tr>
        //   `);
        // } else {
        //   var top = $("table");
        // }
        location.reload();
      }).fail(function () {
        alert("Could not add hymn");
      });
    } else {
      alert("Please enter a date that is not in the future")
    }
  } else {
    alert("Invalid date")
  }
}

function offsetAnchor() {
  if (location.hash.length !== 0) {
    window.scrollTo(window.scrollX, window.scrollY - 80);
  }
}

$(document).ready(function () {
  $("#datepicker").datepicker();
  $("#datepicker").datepicker("option", "dateFormat", "yy-mm-dd");

  $("input[type=search]").on("keyup", function () {
    var query = $(this).val().toLowerCase();
    $("#hymn-tables tbody>tr").each(function () {
      $(this).toggleClass("hidden", $(this).find("td.searchable").text().toLowerCase().indexOf(query) === -1);
    });

    $("#hymn-tables table").each(function () {
      $(this).toggleClass("hidden", $(this).find("tbody tr:not(.hidden)").length === 0);
    });
  });

  $(".heart").on("click", function () {
    var num = $(this).attr("num");
    var hearts = $(`.heart[num="${num}"]`);
    var labels = hearts.next();
    var likes = parseInt(labels.text().split());

    function addLikes(update) {
      likes += update;
      hearts.toggleClass("liked");
      labels.text(likes + " like" + (likes != 1 ? "s" : ""));
    }

    if (!($(this).hasClass("liked"))) {
      $.post("/like/" + num, () => { $(this).toggleClass("is_animating"); addLikes(1) }).fail(() => alert("Could not update like"));
    } else {
      $.post("/unlike/" + num, () => addLikes(-1)).fail(() => alert("Could not update like"));
    }
  });

  $(".heart").on("animationend", function () {
    $(this).toggleClass("is_animating");
  });

  // CREDIT: https://stackoverflow.com/questions/17534661/make-anchor-link-go-some-pixels-above-where-its-linked-to
  // Captures click events of all <a> elements with href starting with #
  $(document).on('click', 'a[href^="#"]', function (event) {
    // Click events are captured before hashchanges. Timeout
    // causes offsetAnchor to be called after the page jump.
    window.setTimeout(function () {
      offsetAnchor();
    }, 0);
  });

  // Set the offset when entering page with hash present in the url
  window.setTimeout(offsetAnchor, 0);
});
