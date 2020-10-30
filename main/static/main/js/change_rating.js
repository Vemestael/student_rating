$(document).ready(function () {
    $("#faculty").change(faculty_change);
    $("#student").change(student_change);
    $("#change_rating").click(change_rating);
    student_change();
});

function faculty_change() {
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
            student_change()
        },
        dataType: 'json',
    });
}

function student_change() {
    let student = $("#student").val();
    $.ajax({
        type: 'GET',
        url: 'change-rating',
        data: "student=" + student,
        success: function (response) {
            let data = JSON.parse(response);
            $("#session").val(data[0]['fields']['session']);
            $("#extra").val(data[0]['fields']['extra']);
            if ($("#extra").val() === "10") {
                $("#add_points_button").prop("disabled", true);
            }
            else{
                $("#add_points_button").prop("disabled", false);
            }
        },
        dataType: 'json',
    });
}

$(document).ready(function () {

});

function change_rating() {
    if ($("#added_extra").val()) {
        $("#activity").attr("required", true);
    }
}