$(document).ready(function () {
    $('.page').each(function () {
        let url = window.location.href
        url = url.replace(/[?|&]page=\d*/gm, "");
        if (url.includes('?'))
            url = url + $(this).attr('href').replace("?", "&")
        else
            url = url + $(this).attr('href')
        $(this).attr('href', url)
    });
});

function uploadCertificate(elem) {
    document.getElementById('student_fullname').value = document.getElementById('full_name' + elem.id).textContent;
    document.getElementById('student_id').value = elem.id;
}

function getDetailsTable(id, rows) {
    return '<table class="ml-5 table table-details table-bordered table-sm" id="details_table' + id + '">\n' +
        '<thead>\n' +
        '   <tr>\n' +
        '       <th scope="col">#</th>\n' +
        '       <th scope="col">Количество</th>\n' +
        '       <th scope="col" class="col-1">Активность</th>\n' +
        '       <th scope="col">Сертификат</th>\n' +
        '   </tr>\n' +
        '</thead>\n' +
        '<tbody>\n' +
        rows +
        '</tbody>\n' +
        '</table>'
}

function showDetails(elem) {
    let id = $(elem).prev().attr('id')
    if ($(elem).val() === "▼") {
        $(elem).val("▲")
        if (!$("#details_table" + id).length && !$("#no_data_available" + id).length) {
            // Table or div does not exists
            let rows = '';
            $.ajax({
                type: 'GET',
                url: '/get-details',
                data: "student=" + id,
                success: function (response) {
                    let parse_data = JSON.stringify(response);
                    let data = JSON.parse(parse_data);
                    if (data.length === 0) {
                        $("#details_about" + id).append('<div id="no_data_available' + id + '">Данные отсутствуют</div>');
                    } else {
                        for (let i = 0; i < data.length; i++) {
                            let point = data[i]['point'];
                            let action = data[i]['description']
                            let certificate = ''
                            if (data[i]['certificate'] === null) {
                                certificate = 'Отсутствует'
                            } else {
                                certificate = '<a  onclick="showCertificate(this)" data-toggle="modal" data-target="#certificateModal" href=\"' +
                                    data[i]['certificate'] + '\">Просмотреть</a>'
                            }
                            let row = '<tr>\n' +
                                '   <th>' + (i + 1) + '</th>\n' +
                                '   <td class="text-center">' + point + '</td>\n' +
                                '   <td>' + action + '</td>\n' +
                                '   <td>' + certificate + '</td>\n' +
                                '</tr>'
                            rows += row
                        }
                        $("#details_about" + id).append(getDetailsTable(id, rows));
                    }

                },
                dataType: 'json',
            });
        }
    } else {
        $(elem).val("▼")
    }
}

function showCertificate(elem) {
    let href = $(elem).prop('href');
    href = href.slice(22);
    $("#certificate").attr('src', href);
}