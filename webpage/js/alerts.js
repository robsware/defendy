function loadAlerts(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('alerts').innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}