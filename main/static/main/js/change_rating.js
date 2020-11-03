$(document).ready(function () {
    $("#faculty").change(facultyChange);
    $("#student").change(studentChange);
    $("#change_rating").click(changeRating);
    studentChange();
});

function facultyChange() {
    let faculty = $("#faculty").val();
    $.ajax({
        type: 'GET',
        url: 'change-rating',
        data: "faculty=" + faculty,
        success: function (response) {
            let data = JSON.parse(response);
            let elem = $('#student');
            elem.empty();
            for (let i = 0; i < data.length; i++) {
                elem.append(`<option value="${data[i]['pk']}">
                                        ${(data[i]['fields']['group'])} ${data[i]['fields']['full_name']}</option>`);
            }
            studentChange()
        },
        dataType: 'json',
    });
}

function studentChange() {
    let student = $("#student").val();
    $.ajax({
        type: 'GET',
        url: 'change-rating',
        data: "student=" + student,
        success: function (response) {
            let data = JSON.parse(response);
            $("#session").val(data[0]['fields']['session']);
            $("#extra_points").val(data[0]['fields']['extra']);
            $("#change_rating").val(data[0]['pk']);
            if (data[0]['fields']['extra'] === 10) {
                $("#add_points_button").prop("disabled", true);
            } else {
                $("#add_points_button").prop("disabled", false);
            }
            $('#collapseExample').attr("class", "collapse");
            $("#added_points").val(0);
            $("#activity").val("");
            $("#certificate").val("");
        },
        dataType: 'json',
    });
}

function changeRating() {
    if ($("#added_points").val()) {
        $("#activity").attr("required", true);
    }
    let now = parseInt($("#extra_points").val())
    let add = parseInt($("#added_points").val())
    if (now + add > 10) {
        alert('Не может быть больше 10 доп.баллов');
        return false;
    }
}