import random
import string

class PasswordGenerator:

    def run(self):
        self.read_inputs()
        self.password = self.generate_password()
        self.display_output(self.password)

    def __init__(self):
        self.form_upper = js.document.getElementById('form-upper')
        self.form_lower = js.document.getElementById('form-lower')
        self.form_digit = js.document.getElementById('form-digit')
        self.form_special = js.document.getElementById('form-special')
        self.output_elem = js.document.getElementById('output');
        self.is_password_hidden = False

    def read_inputs(self):
        self.upper_num = int(self.form_upper.value)
        self.lower_num = int(self.form_lower.value)
        self.digit_num = int(self.form_digit.value)
        self.special_num = int(self.form_special.value)

    def generate_password(self):
        uppers = random.choices(string.ascii_uppercase, k=self.upper_num)
        lowers = random.choices(string.ascii_lowercase, k=self.lower_num)
        digits = random.choices(string.digits, k=self.digit_num)
        specials = random.choices(string.punctuation, k=self.special_num)
        password_chars = uppers + lowers + digits + specials
        random.shuffle(password_chars)
        password_final = ''.join(password_chars)
        return password_final

    def display_output(self, password):
        self.output_elem.innerText = password

    def toggle_hide_password(self):
        if self.is_password_hidden:
            self.display_output(self.password)
            self.is_password_hidden = False
        else:
            self.display_output('*'*len(self.password))
            self.is_password_hidden = True
    
    def copy_password(self):
        js.navigator.clipboard.writeText(self.password)
        js.alert('Password copied to the clipboard!')
