function copyText() {
  var copyText = document.getElementById("invite_key");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
}