function loadIP(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('publicip').innerHTML = "Public IP: " + this.responseText;
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}