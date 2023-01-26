function submitForm(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById("myForm"));
    fetch('/test', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      // Handle the response from the server here
    });
}