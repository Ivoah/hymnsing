function adminLogin() {
  var pw = $("#input").val();
  $.post("/login", {
    "password": pw
  }).done(function() {
    window.location.href = "/";
  }).fail(function() {
    alert("Invalid login");
  });
}

function addHymn(num) {
  var date = $("#datepicker").val();
  $.post("/addHymn", {
    date: date,
    hymn: num
  }).done(function() {
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
  }).fail(function() {
    alert("Could not add hymn");
  });
}

$(document).ready(function () {
  $("#datepicker").datepicker();
  $("#datepicker").datepicker("option", "dateFormat", "yy-mm-dd");

  $("input[type=search]").on("keyup", function() {
    var query = $(this).val().toLowerCase();
    $("#hymn-tables tbody>tr").each(function() {
      $(this).toggleClass("hidden", $(this).text().toLowerCase().indexOf(query) === -1);
    });

    $("#hymn-tables table").each(function() {
      $(this).toggleClass("hidden", $(this).find("tbody tr:not(.hidden)").length === 0);
    });
  });

  $(".heart").on("click", function() {
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
      $.post("/like/" + num, () => {$(this).toggleClass("is_animating"); addLikes(1)}).fail(() => alert("Could not update like"));
    } else {
      $.post("/unlike/" + num, () => addLikes(-1)).fail(() => alert("Could not update like"));
    }
  });

  $(".heart").on("animationend", function(){
    $(this).toggleClass("is_animating");
  });
});
