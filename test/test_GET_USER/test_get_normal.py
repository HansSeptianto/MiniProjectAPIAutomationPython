import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user


@pytest.mark.QaseIO(10)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer e91cd771350a43675d8778d2ffae8369de707d4c962c53611b374782346b9fb7"
    }
    req = requests.get(api_user, headers=head)

    # VALIDATION
    status_code = req.status_code
    resp_id = req.json()[0]["id"]
    resp_name = req.json()[0]["name"]
    resp_email = req.json()[0]["email"]
    resp_gender = req.json()[0]["gender"]
    resp_status = req.json()[0]["status"]

    # ASSERT
    assert_that(status_code).is_equal_to(200)

    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_gender).is_not_none()
    assert_that(resp_status).is_not_none()

    assert_that(resp_id).is_type_of(int)
    assert_that(resp_name).is_type_of(str)
    assert_that(resp_email).is_type_of(str)
    assert_that(resp_gender).is_type_of(str)
    assert_that(resp_status).is_type_of(str)

    assert_that(resp_email).contains("@")
    assert_that(resp_gender).is_in("male", "female")
    assert_that(resp_status).is_in("active", "inactive")
