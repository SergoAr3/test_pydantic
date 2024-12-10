import pytest
import json

from starlette.testclient import TestClient


@pytest.mark.parametrize(
    ['data', 'result'],
    [
        (
                {
                    "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
                    "employment": "fullDay",
                    "address": {
                        "region": "Кировская",
                        "city": "Киров",
                        "street_type": "",
                        "street": "",
                        "house_type": "",
                        "house": "",
                        "value": "г Киров, ул Володарского, д 157",
                        "lat": 58.593565,
                        "lng": 49.672739
                    },
                    "name": "Junior Backend-developer",
                    "salary": {
                        "from": 30000,
                        "to": 70000,
                        "currency": "RUR",
                        "gross": False
                    },
                    "contacts": {
                        "fullName": "Журавлев Илья",
                        "phone": "+79536762399",
                        "email": "ilya.zhuravlev@hrb.software"
                    }
                },
                {
                    "address": "г Киров, ул Володарского, д 157",
                    "allow_messages": True,
                    "billing_type": "packageOrSingle",
                    "business_area": 1,
                    "contacts": {
                        "email": "ilya.zhuravlev@hrb.software",
                        "name": "Журавлев Илья",
                        "phone": {
                            "city": "953",
                            "country": "7",
                            "number": "676-23-99"
                        }
                    },
                    "coordinates": {
                        "latitude": 58.593565,
                        "longitude": 49.672739
                    },
                    "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
                    "experience": {
                        "id": "noMatter"
                    },
                    "html_tags": True,
                    "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
                    "name": "Junior Backend-developer",
                    "salary": 70000,
                    "salary_range": {
                        "from": 30000,
                        "to": 70000
                    },
                    "schedule": {
                        "id": "fullDay"
                    }
                }
        )
    ]
)
def test_parser(client: TestClient, data, result):
    resp = client.post(f"/convert", json=data)
    response_data = json.loads(resp.content.decode('utf-8'))
    assert resp.status_code == 200
    assert response_data == result


@pytest.mark.parametrize(
    "data, expected_status",
    [
        (
                {
                    "description": "Test description",
                    "employment": "fullDay",
                    "address": {
                        "region": "Кировская",
                        "city": "Киров",
                        "value": "г Киров, ул Володарского, д 157",
                        "lat": 58.593565,
                        "lng": 49.672739
                    },
                    "name": "Junior Backend-developer",
                    "salary": {
                        "from": 30000,
                        "to": 70000,
                        "currency": "RUR",
                        "gross": False
                    },
                    "contacts": {
                        "fullName": "Иванов Иван",
                        "phone": "+1234567890",
                        "email": "ivanov@example.com"
                    }
                },
                422,
        ),

        (
                {
                    "description": "Test description",
                    "employment": "fullDay",
                    "address": {
                        "region": "Кировская",
                        "city": "Киров",
                        "value": "г Киров, ул Володарского, д 157",
                        "lat": 58.593565,
                        "lng": 49.672739
                    },
                    "name": "Junior Backend-developer",
                    "salary": {
                        "from": 30000,
                        "to": 70000,
                        "currency": "RUR",
                        "gross": False
                    },
                    "contacts": {
                        "fullName": "Иванов Иван",
                        "phone": "+79876543210987654321",
                        "email": "ivanov@example.com"
                    }
                },
                422,
        ),
    ]
)
def test_invalid_phone(client: TestClient, data, expected_status):
    resp = client.post("/convert", json=data)
    assert resp.status_code == expected_status
