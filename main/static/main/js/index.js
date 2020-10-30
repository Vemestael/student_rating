function myFunction(elem) {
    document.getElementById('student_fullname').value = document.getElementById('full_name' + elem.id).textContent;
    document.getElementById('student_id').value = elem.id;
}