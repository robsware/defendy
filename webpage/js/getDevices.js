function loadDoc(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('devices').innerHTML = this.responseText.replace(/\n/g, "<br />");
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}

