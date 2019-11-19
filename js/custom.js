$(document).ready(function () {
  $("#hymn-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#hymn-tables tr.hymns").each(function () {
      $(this).toggleClass("hidden", $(this).text().toLowerCase().indexOf(value) === -1)
    });

    $("#hymn-tables thead.hymns-section-head").each(function () {
      $(this).parent().toggle(($(this).siblings().children("tr.hymns:not(.hidden)")).length > 0)
    });
  });

  $(".heart").on("click", function() {
    var heart = $(this);
    var label = heart.next();
    var likes = parseInt(label.text().split());
    var num = heart.attr("num");

    if (!(heart.hasClass("liked"))) {
      $.post("/like/" + num, function() {
        heart.toggleClass("is_animating");
        likes++;
        heart.toggleClass("liked");
        label.text(likes + " like" + (likes != 1 ? "s" : ""));
      });
    } else {
      $.post("/unlike/" + num, function() {
        likes--;
        heart.toggleClass("liked");
        label.text(likes + " like" + (likes != 1 ? "s" : ""));
      });
    }
  });

  $(".heart").on("animationend", function(){
    $(this).toggleClass("is_animating");
  });
});
