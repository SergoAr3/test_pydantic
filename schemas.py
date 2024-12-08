from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict


class Address(BaseModel):
    region: str
    city: str
    street_type: Optional[str]
    street: Optional[str]
    house_type: Optional[str]
    house: Optional[str]
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
    contacts: Dict[str, str | dict]
    coordinates: Dict[str, float]
    description: str
    experience: Dict[str, str] = {"id": "noMatter"}
    html_tags: bool
    image_url: str = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: int
    salary_range: Dict[str, int]
    schedule: Dict[str, str] = {"id": "fullDay"}