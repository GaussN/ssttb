from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy

from education.models import Test


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
        'table_name': 'Exercises',
        'table_url': reverse_lazy('exercises'),
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
def test_view(request: HttpRequest, id):
    return render(request, 'admin_panel/test.html', {'test': Test.objects.get(pk=id)})
