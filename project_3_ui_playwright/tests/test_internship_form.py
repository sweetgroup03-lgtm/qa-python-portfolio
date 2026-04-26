import os
from pathlib import Path

from pages.internship_form_page import InternshipFormPage


def get_ui_target() -> str:
    env_url = os.getenv("UI_BASE_URL")
    if env_url:
        return env_url
    local_html = Path(__file__).resolve().parents[1] / "app" / "index.html"
    return local_html.as_uri()


def test_submit_valid_form(page):
    form = InternshipFormPage(page)
    form.open(get_ui_target())
    form.fill_valid_form()
    form.submit()
    assert form.success.is_visible()
    assert form.error.text_content() == ""


def test_submit_with_invalid_email(page):
    form = InternshipFormPage(page)
    form.open(get_ui_target())
    form.direction.select_option("python-qa")
    form.last_name.fill("Petrov")
    form.first_name.fill("Ivan")
    form.email.fill("not-an-email")
    form.telegram.fill("@valid_name")
    form.submit()
    assert form.error.text_content() == "Email is invalid."


def test_submit_empty_form_shows_required_error(page):
    form = InternshipFormPage(page)
    form.open(get_ui_target())
    form.submit()
    assert form.error.text_content() == "All fields are required."


def test_submit_with_invalid_telegram(page):
    form = InternshipFormPage(page)
    form.open(get_ui_target())
    form.direction.select_option("python-qa")
    form.last_name.fill("Petrov")
    form.first_name.fill("Ivan")
    form.email.fill("ivan.petrov@example.com")
    form.telegram.fill("wrong_telegram")
    form.submit()
    assert form.error.text_content() == "Telegram is invalid."
