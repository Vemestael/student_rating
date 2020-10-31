$(document).ready(function () {
    $('form').submit(submit_form);
    $('[name=\'add\']').click(add_action);
    $('[name=\'reject\']').click(reject_action);
});

function submit_form(e) {
    let $form = $(this);
    let id = $form.prop('id')
    let now = parseInt($('#extra_points' + id).val())
    let added = parseInt($('#added_points' + id).val())
    if ((now + added) <= 10) {
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize()
        }).done(function () {
            console.log('success');
            $form.remove();
        }).fail(function () {
            console.log('fail');
        });

    } else {
        alert('Не может быть больше 10 доп.баллов')
    }
    //отмена действия по умолчанию для кнопки submit
    e.preventDefault();
}

function add_action() {
    let id = $(this).val();
    $('#action' + id).val('add');
    $('#activity' + id).prop('required', true);
}

function reject_action() {
    let id = $(this).val();
    $('#action' + id).val('reject');
}