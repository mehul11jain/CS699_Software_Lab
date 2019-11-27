$("span").click(function() {
      div = document.createElement('div');
      $(div).addClass("inner").html("new inner div");
      $(".container").append(div);
    });