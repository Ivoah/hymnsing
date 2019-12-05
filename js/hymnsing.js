function adminLogin() {
  var pw = $("#input").val();
  $.post("/login", {
    "password": pw
  }).done(function() {
    window.location.href = "/admin";
  }).fail(function() {
    alert("Invalid login");
  });
}

$(document).ready(function () {
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
