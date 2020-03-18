function checkSubject() {
  if (document.getElementById("subject").value == "Select") {
    document.getElementById("course").style.display = "none";
  } else {
    document.getElementById("course").style.display = "inline-block";
  }
}

function checkCourse() {
  if (document.getElementById("course").value == "Select") {
    document.getElementById("section").style.display = "none";
  } else {
    document.getElementById("section").style.display = "inline-block";
  }
}

document.getElementById('subject').addEventListener('change', function (){
  checkSubject();
}, false);

document.getElementById('course').addEventListener('change', function (){
  checkCourse();
}, false);

checkCourse();
checkSubject();