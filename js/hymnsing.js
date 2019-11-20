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

    function fail() {
      $("#alert").html(`
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          <strong>Error</strong> couldn't update like.
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      `);
    }

    if (!(heart.hasClass("liked"))) {
      $.post("/like/" + num, () => {heart.toggleClass("is_animating"); addLikes(1)}).fail(fail);
    } else {
      $.post("/unlike/" + num, () => addLikes(-1)).fail(fail);
    }
  });

  $(".heart").on("animationend", function(){
    $(this).toggleClass("is_animating");
  });
});
