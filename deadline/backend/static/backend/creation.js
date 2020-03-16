function showPassword(x) {
  var x = document.getElementById(x);
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}