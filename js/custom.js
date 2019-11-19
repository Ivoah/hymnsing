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
    if (!($(this).hasClass("liked"))) {
      $(this).toggleClass("is_animating");
    }
    $(this).toggleClass("liked");
  });
  $(".heart").on("animationend", function(){
    $(this).toggleClass("is_animating");
  });
});