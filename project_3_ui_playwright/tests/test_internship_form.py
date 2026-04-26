import os

from pages.internship_form_page import InternshipFormPage


def test_submit_valid_form(page):
    form = InternshipFormPage(page)
    form.open(os.getenv("UI_BASE_URL", "http://127.0.0.1:5500"))
    form.fill_valid_form()
    form.submit()
    assert form.success.is_visible()
    assert form.error.text_content() == ""


def test_submit_with_invalid_email(page):
    form = InternshipFormPage(page)
    form.open(os.getenv("UI_BASE_URL", "http://127.0.0.1:5500"))
    form.direction.select_option("python-qa")
    form.last_name.fill("Petrov")
    form.first_name.fill("Ivan")
    form.email.fill("not-an-email")
    form.telegram.fill("@valid_name")
    form.submit()
    assert form.error.text_content() == "Email is invalid."

