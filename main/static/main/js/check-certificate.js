function check_extra(elem) {
    let id = elem.id;
    let current_extra = parseInt(document.getElementById('current_extra' + id).value);
    let add_extra = parseInt(document.getElementById('add_extra' + id).value);
    if((current_extra + add_extra) > 10){
        window.alert('There cannot be more than 10 additional points')
    }
}