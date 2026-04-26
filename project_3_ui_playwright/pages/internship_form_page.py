class InternshipFormPage:
    def __init__(self, page):
        self.page = page
        self.direction = page.locator("#direction")
        self.last_name = page.locator("#last_name")
        self.first_name = page.locator("#first_name")
        self.email = page.locator("#email")
        self.telegram = page.locator("#telegram")
        self.submit_button = page.locator("#submit-btn")
        self.error = page.locator("#error")
        self.success = page.locator("#success")

    def open(self, base_url: str):
        self.page.goto(base_url)

    def fill_valid_form(self):
        self.direction.select_option("python-qa")
        self.last_name.fill("Petrov")
        self.first_name.fill("Ivan")
        self.email.fill("ivan.petrov@example.com")
        self.telegram.fill("@ivan_petrov")

    def submit(self):
        self.submit_button.click()

