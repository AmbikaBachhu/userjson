import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userjosn2.settings')
import django

django.setup()
from app.models import user, activity, duplicate
from faker import Faker
from random import *
from datetime import datetime, timedelta

faker = Faker()
startDate = timedelta(hours=randint(8, 11), minutes=randint(0, 59))
endDate = timedelta(hours=randint(12, 19), minutes=randint(0, 59))
date1 = datetime(year=randint(2019, 2020), month=randint(2, 4), day=randint(1, 28))


def new():
    z = duplicate.objects.get_or_create(ok=True)[0]
    z.save()
    return z


def dummy():
    for entry in range(3):
        # Create Fake Data for entry
        fake_ok = new()
        fake_id = faker.bothify(text='??#?##?##')
        fake_name = faker.name()
        fake_tz = faker.timezone()
        # Create new user Entry

        # Create new user Entry
        usr = user.objects.get_or_create(members=fake_ok, id=fake_id, real_name=fake_name, tz=fake_tz)[0]
        usr.save()
        return usr


def addson(n):
    for entry in range(2):
        s = faker.date_time_between(start_date=startDate, end_date=endDate)
        return s


addson(2)


def add(n):
    for x in range(n):
        fake_act = dummy()
        Faker.seed(0)
        for _ in range(3):
                fake_start = addson(1)
                fake_end = addson(2)

                act = activity.objects.get_or_create(user_activity=fake_act, start_time=fake_start,
                                                     end_time=fake_end)[0]


add(3)
