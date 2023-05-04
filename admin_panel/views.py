import json

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.db import utils

from education.models import *


admin_tables = [
    {
        'table_name': 'Test',
        'table_url': reverse_lazy('tests'),
    },
    {
        'table_name': 'Lesson',
        'table_url': reverse_lazy('lessons'),
    },
    {
        'table_name': 'User',
        'table_url': reverse_lazy('users'),
    },
]


@login_required
@user_passes_test(lambda user: user.is_superuser)
def admin_home(request: HttpRequest):
    return render(request, 'admin_panel/admin_home.html', {'tables': admin_tables})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def records_list(request: HttpRequest, **kwargs):
    return render(request, 'admin_panel/records_list.html', kwargs)


@login_required
@user_passes_test(lambda user: user.is_superuser)
def test_update(request: HttpRequest, id: int):
    return render(request, 'admin_panel/test.html', {'test': Test.objects.get(pk=id)})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def test_add(request: HttpRequest):
    if request.method == 'POST':
        post = json.loads(request.body)
        try:
            test = Test(
                topic=post.get('title'),
                test_json=post.get('questions'),
                visible=post.get('visible')
            )
            test.save()
        except utils.Error as er:
            print(f"{er=}")
        # возврат json с сообщением: "успех"/"не успех"
        return redirect(reverse_lazy('tests'))
    return render(request, 'admin_panel/test.html')
