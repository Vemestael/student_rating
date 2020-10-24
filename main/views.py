from uuid import uuid4

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as da
import main.models as model
from django.conf import settings
import main.forms as forms

from openpyxl import load_workbook


def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {'username': username}
    return render(request, 'main/index.html', context)


def login(request):
    context = {'error': ''}
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = da.authenticate(request, username=username, password=password)
        if user is not None:
            da.login(request, user)
            return redirect('/')
        else:
            context = {'error': 'invalid login'}
    return render(request, 'main/sign_in.html', context)


def sign_up(request):
    da.logout(request)
    invite_key_status = ""
    error = ""
    if request.method == 'POST':
        if request.POST['invite_key_status'] != 'OK':
            invite_key = request.POST['invite_key']
            if model.InviteKey.objects.filter(invite_key__exact=invite_key).count():
                invite_key_status = "OK"
            else:
                error = 'invalid key'
        else:
            full_name = request.POST['full_name'].split(' ')
            first_name = full_name[0]
            last_name = ''
            if len(full_name) > 1:
                last_name = full_name[1]
            if len(first_name) == 0 or len(last_name) == 0:
                error = 'enter your full name'
                context = {"invite_key": "OK", "error": error}
                return render(request, 'main/sign_up.html', context)

            faculty = request.POST.get('faculty')
            if faculty is None:
                error = 'enter your faculty'
                context = {"invite_key": "OK", "error": error}
                return render(request, 'main/sign_up.html', context)

            email = request.POST['email']
            login = request.POST['login']
            password = request.POST['password']

            user = User.objects.create_user(login, email, password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('/')
    context = {"invite_key": invite_key_status, "error": error}
    return render(request, 'main/sign_up.html', context)


def invite_key_gen(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            invite_key = ""
            if request.method == "POST":
                invite_key = uuid4()
                a_record = model.InviteKey(invite_key=invite_key)
                a_record.save()
            context = {"invite_key": invite_key}
            return render(request, 'admin/invite_key_gen.html', context)
    return redirect('/')


def add_rating(request):
    username = None
    username = request.user.username
    content_type = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "application/vnd.ms-excel"]
    if request.method == "POST":
        if 'upload_rating' in request.POST:
            print('test')
            file = request.FILES['upload_file']
            if file.content_type in content_type:
                table_entry = model.ExelFile(uploaded_by_user=username, exel_file=file)
                table_entry.save()
                read_workbook(file.name)
            return redirect('/add-rating')
        if 'add_rating' in request.POST:
            form = forms.AddRatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.total = form.cleaned_data.get('session') + form.cleaned_data.get('extra')
                rating.save()
                return redirect('/')
            else:
                context = {'username': username, "form": form}
                return render(request, 'main/add_rating.html', context)
    else:
        form = forms.AddRatingForm()
        context = {'username': username, "form": form}
        return render(request, 'main/add_rating.html', context)


def read_workbook(file_name):
    file_dir = str(settings.BASE_DIR) + "/files/excel/"
    workbook = load_workbook(file_dir + file_name)
    worksheet = workbook[workbook.sheetnames[0]]
    faculties = {
        "ФИТ": 1,
        "ФІТ": 1,
        "ЕкФ": 2,
        "ЕнФ": 3,
        "МФ": 4,
        "СГФ": 5,
        "ФМЗ": 6,
        "ФТТ": 7,
        "ФИМП": 8,
        "ФІМП": 8,
    }
    faculty = faculties.get(worksheet.cell(row=2, column=2).value)
    faculty = model.Faculty.objects.get(id=faculty)

    for row in worksheet.iter_rows(min_row=2):
        temp = []
        for cells in row:
            temp.append(cells.value)
        table_entry = model.Rating()
        table_entry.full_name = temp[0]
        table_entry.faculty = faculty
        table_entry.group = temp[2]
        table_entry.session = temp[3]
        table_entry.extra = temp[4]
        table_entry.total = temp[3] + temp[4]
        table_entry.save()
