
function playmusic(id, piece, composer, movement, title, performers) {

  console.log("pooing music");
  
  n = document.getElementById("nowplaying");
  n.innerHTML = 
    "<span class='piece'>"+piece+"</span>" +
    "<span class='composer'>"+composer+"</span>" +
    "<span class='movement'>"+movement+". </span>" +
    "<span class='title'>"+title+"</span> <br />" +
    "<span class='performers'>"+performers+"</span>";

  a = document.getElementById("theaudio");
  a.innerHTML = "<source src=http://localhost:8337/item/"+id+"/file>";
  a.load();
  a.play();

}
