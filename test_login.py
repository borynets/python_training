# -*- coding: utf-8 -*-

import unittest

import pytest

from application import Application
from vacancy import Vacancy

def test_login_test_case(app):
    app.open_home_page()
    app.login(username="romanovaua189@gmail.com", password="123456")
    vacancy = Vacancy(title="Test tile", description="Test decsiprtion", minExperience=2)
    app.create_new_vacancy(vacancy)
    app.logout()
    app.destroy()

def tearDown(app):
    app.destroy()

@pytest.fixture()
def app(request):
    fixture = Application()
    return fixture

