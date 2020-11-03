$(document).ready(function () {
    $("#invite_key_form").submit(generateRequest);
    $("#password_form").submit(validatePasswords);
    showSuccess();
});

function validatePasswords() {
    if ($("#new_passwd").val() !== $("#repeat_passwd").val()) {
        alert('Passwords do not match!');
        return false;
    } else {
        return true;
    }
}

function generateRequest(e) {
    //отмена действия по умолчанию для кнопки submit
    e.preventDefault();
    let $form = $(this)
    $.ajax({
        type: 'POST',
        url: 'profile',
        data: $form.serialize()
    }).done(function (response) {
        console.log('success');
        $("#invite_key").val(response['invite_key']);
    }).fail(function () {
        console.log('fail');
    });
}

function showSuccess() {
    let success = $("#success").val()
    if(success.length !== 0){
        alert(success)
    }
}