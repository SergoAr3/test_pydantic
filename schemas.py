import re

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, HttpUrl, Field, field_validator


class Address(BaseModel):
    region: str
    city: str
    street_type: str | None
    street: str | None
    house_type: str | None
    house: str | None
    value: str
    lat: float
    lng: float


class Salary(BaseModel):
    from_: int = Field(alias="from")
    to: int
    currency: str
    gross: bool


class Contacts(BaseModel):
    fullName: str
    phone: str = '79999999999'
    email: EmailStr

    @field_validator('phone')
    @classmethod
    def phone_validate(cls, value):
        if value[0] == '+':
            return value[1:]

        if not re.fullmatch(r'[78]\d{10}', value):
            raise HTTPException(422, "Phone number must start with 7 or 8 and be 11 digits long")

        return value


class InputData(BaseModel):
    description: str
    employment: str
    address: Address
    name: str
    salary: Salary
    contacts: Contacts


class OutputData(BaseModel):
    address: str
    allow_messages: bool = True
    billing_type: str = 'packageOrSingle'
    business_area: int = 1
    contacts: dict[str, str | dict]
    coordinates: dict[str, float]
    description: str
    experience: dict[str, str] = {"id": "noMatter"}
    html_tags: bool
    image_url: HttpUrl = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: int
    salary_range: dict[str, int]
    schedule: dict[str, str]
