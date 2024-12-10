from fastapi import FastAPI

from schemas import InputData, OutputData

app = FastAPI(docs_url='/')


@app.post("/convert", response_model=OutputData)
async def data_convert(data: InputData):
    phone_number = data.contacts.phone
    response = {
        'address': data.address.value,
        'contacts': {
            'email': data.contacts.email,
            'name': data.contacts.fullName,
            'phone': {
                'city': f'{phone_number[1:4]}',
                'country': f'{phone_number[0]}',
                'number': f'{phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:11]}'
            }
        },
        'coordinates': {
            'latitude': data.address.lat,
            'longitude': data.address.lng
        },
        'description': data.description,
        'html_tags': True,
        'name': data.name,
        'salary': data.salary.to,
        'salary_range': {
            "from": data.salary.from_,
            "to": data.salary.to
        },
        'schedule': {'id': data.employment}

    }

    return response
