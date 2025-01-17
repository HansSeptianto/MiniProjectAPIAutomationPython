import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker

fake = Faker()


@pytest.mark.QaseIO(7)
def test():
    random_name = fake.name()
    random_email = fake.email()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer e91cd771350a43675d8778d2ffae8369de707d4c962c53611b374782346b9fb7"
    }
    payload = {
        "name": random_name,
        "gender": "male",
        "email": random_email,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    resp_name = req.json().get("name")
    resp_email = req.json().get("email")

    # ASSERT
    assert_that(status_code).is_equal_to(201)
    assert_that((resp_name)).is_equal_to(random_name)
    assert_that((resp_email)).is_equal_to(random_email)
