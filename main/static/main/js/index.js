function myFunction(elem) {
    let full_name = document.getElementById('full_name'+elem.id).textContent;
    document.getElementById('student_fullname').value = full_name;
    document.getElementById('student_id').value = elem.id;
}


function tableSearch() {
    let phrase = document.getElementById('search-text');
    let table = document.getElementById('rating-table');
    let regPhrase = new RegExp(phrase.value, 'i');
    let flag = false;
    for (let i = 1; i < table.rows.length; i++) {
        flag = false;
        for (let j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }
    }
}
