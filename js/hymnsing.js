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
    var heart = $(this);
    var label = heart.next();
    var likes = parseInt(label.text().split());
    var num = heart.attr("num");

    function addLikes(update) {
      likes += update;
      heart.toggleClass("liked");
      label.text(likes + " like" + (likes != 1 ? "s" : ""));
    }

    if (!(heart.hasClass("liked"))) {
      $.post("/like/" + num, () => {heart.toggleClass("is_animating"); addLikes(1)}).fail(() => alert("Could not update like"));
    } else {
      $.post("/unlike/" + num, () => addLikes(-1)).fail(() => alert("Could not update like"));
    }
  });

  $(".heart").on("animationend", function(){
    $(this).toggleClass("is_animating");
  });
});
