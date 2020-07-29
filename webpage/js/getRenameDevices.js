function pullListDevices(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('pullListDevices').innerHTML = this.responseText.replace(/\n/g, "<br />");
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}

function pullRemoveDevices(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('pullRemoveDevices').innerHTML = this.responseText.replace(/\n/g, "<br />");
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}

function pullResetDevices(url) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById('pullResetDevices').innerHTML = this.responseText.replace(/\n/g, "<br />");
    }
  };
  xhttp.open("GET", url + '?_=' + new Date().getTime(), true);
  xhttp.send();
}
