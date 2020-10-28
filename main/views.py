from uuid import uuid4
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import django.contrib.auth as da
import main.models as model
from django.conf import settings
import main.forms as forms
from django.core.paginator import Paginator

from openpyxl import load_workbook


def winter(year):
    start = str(int(year) - 1) + "-31-01",
    end = year + "-02-28"
    return [start, end]


def summer(year):
    start = year + "05-01"
    end = year + "08-01"
    return [start, end]


def now(year):
    start = year + "-09-01"
    end = datetime.today().strftime('%Y-%m-%d')
    return [start, end]


def get_rating(faculty: int, session, year):
    date = []
    if session == "summer":
        date = summer(year)
    else:
        date = winter(year)
    rating = model.Rating.objects.filter(date__range=now(year), faculty=faculty).values('id', 'full_name', 'group',
                                                                                        'session', 'extra', 'total')
    return rating


def index(request):
    form = forms.FilterForm(request.GET)
    if form.is_valid():
        faculty = form.cleaned_data.get('faculty')
        session = form.cleaned_data.get('session')
        year = form.cleaned_data.get('year_picker')
        rating = get_rating(faculty, session, year)
    else:
        form = forms.FilterForm(initial={'year_picker': str(datetime.now().year)})
        faculty = form['faculty'].initial
        session = form['session'].initial
        year = form['year_picker'].initial
        rating = get_rating(faculty, session, year)

    paginator = Paginator(rating, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "form": form}
    return render(request, 'main/index.html', context)


def upload_certificate(request):
    content_type = ["image/jpeg", "image/jpg", "image/png"]
    file = request.FILES['upload_file']
    print(file)
    print(request.POST['student_id'])
    if file.content_type in content_type:
        student = model.Rating.objects.get(pk=request.POST['student_id'])
        table_entry = model.Certificate(uploaded_by_student=student, certificate_file=file)
        table_entry.save()
    return redirect('/')


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
    username = request.user.username
    content_type = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    "application/vnd.ms-excel"]
    if request.method == "POST":
        if 'upload_rating' in request.POST:
            file = request.FILES['upload_file']
            if file.content_type in content_type:
                table_entry = model.ExelFile(uploaded_by_user=username, excel_file=file)
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
