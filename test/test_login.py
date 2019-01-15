# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.vacancy import Vacancy

def test_login_test_case(app):
    app.open_home_page()
    app.session.login(username="romanovaua189@gmail.com", password="123456")
    vacancy = Vacancy(title="Test tile", description="Test decsiprtion", minExperience=2)
    app.vacancy.create(vacancy)
    app.session.logout()
    app.destroy()

def tearDown(app):
    app.destroy()

@pytest.fixture()
def app(request):
    fixture = Application()
    return fixture

