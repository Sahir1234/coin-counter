
const URL = 'http://127.0.0.1:5000/';

$(document).ready(function() {

  function updateView(counts) {

      if (counts.total < 0) {
        counts.total = 0;
      }
      $( "#count" ).html(counts.coins);
      $( "#total" ).html(counts.total.toFixed(2));
      $( "#pen" ).html(counts.p);
      $( "#nick" ).html(counts.n);
      $( "#dim" ).html(counts.d);
      $( "#quart" ).html(counts.q);
  }

  function basicCall(route) {
    $.ajax(
      {
        url: URL.concat(route),
        type: 'GET',
        success: function(result) {
          updateView(result);
        }
      }
    );
  }

  function updateCall(coin) {
    $.ajax(
      {
        url: URL.concat("update/").concat(coin),
        type: 'GET',
        success: function(result) {
          updateView(result);
        }
      }
    );
  }

  basicCall("get");

  $('button').click(function(){
    $(this).fadeOut(25).fadeIn(25);
    if (this.id == "undo") {
      basicCall("undo");
    } else {
      updateCall(this.value);
    }
  });
});
