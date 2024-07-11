import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker

fake = Faker()


@pytest.mark.QaseIO(1)
def test():
    random_name = fake.name()
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer e91cd771350a43675d8778d2ffae8369de707d4c962c53611b374782346b9fb7"
    }
    payload = {
        "name": random_name,
        "gender": "male",
        "email": "",
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    resp_field = req.json()[0]["field"]
    resp_message = req.json()[0]["message"]

    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_field).is_equal_to("email")
    assert_that(resp_message).is_equal_to("can't be blank")
