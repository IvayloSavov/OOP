class EmailParser:
    def __init__(self, email):
        self.__email = email
        username, tail = self.__email.split("@", maxsplit=1)
        mail, domain = tail.split(".", maxsplit=1)
        self.__username = username
        self.__mail = mail
        self.__domain = domain

    @property
    def username(self):
        return self.__username

    @property
    def mail(self):
        return self.__mail

    @property
    def domain(self):
        return self.__domain


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        parsed_email = EmailParser(email)
        return self.__validate_name(parsed_email.username) and self.__validate_domain(parsed_email.domain) \
               and self.__validate_mail(parsed_email.mail)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

