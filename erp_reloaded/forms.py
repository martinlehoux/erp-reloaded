from dataclasses import dataclass


@dataclass
class Field:
    name: str
    template: str
    label: str = None


@dataclass
class InputField(Field):
    type: str = "text"
    template: str = "form/widget/input.html"


@dataclass
class SelectField(Field):
    options: list = None
    template: str = "form/widget/select.html"
    clearable: bool = False


@dataclass
class CountrySelectField(SelectField):
    template: str = "form/widget/select-country.html"


@dataclass
class SubmitField:
    label: str = "Submit"
    template: str = "form/widget/submit.html"
    icon: str = None


@dataclass
class Form:
    fields: list
    inline: bool = False


@dataclass
class SearchForm(Form):
    inline: bool = True
    template: str = "form/search.html"
    submit_field = SubmitField("Search", icon="search")
