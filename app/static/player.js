let playBtn = document.getElementById("play");

playBtn.addEventListener("click", function() {
    event.preventDefault();
    fetch('/play', {   // assuming the backend is hosted on the same server
        method: 'POST',
    }).then(function(response) {
        // do something with the response if needed.
        // If you want the table to be built only after the backend handles the request and replies, call buildTable() here.
        console.log(response);
    });
  }); 