function addMusician() {
  console.log("add musician");

  $('#upload_form').append(
    '<input type="hidden" name="addMusician" value="new">'
  );

  $('#upload_form').submit();
}

function addMovement() {
  console.log("add movement");

  $('#upload_form').append(
    '<input type="hidden" name="addMovement" value="new">'
  );

  $('#upload_form').submit();
}
