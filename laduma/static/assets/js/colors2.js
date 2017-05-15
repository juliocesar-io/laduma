/**
 * Created by JulioC on 5/14/17.
 */
function startIt() {

  var color1 = document.getElementById('color-1');
  var boo1 = document.getElementById('boo-1');

  boo1.onchange = function makeReadable() {
    color1.value = boo1.value;
  };

  var color2 = document.getElementById('color-2');
  var boo2 = document.getElementById('boo-2');

  boo2.onchange = function makeReadable() {
    color2.value = boo2.value;
  };

    var color3 = document.getElementById('color-3');
  var boo3 = document.getElementById('boo-3');

  boo3.onchange = function makeReadable() {
    color3.value = boo3.value;
  };
}

document.body.onload = startIt();