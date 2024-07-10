import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user_invalid


@pytest.mark.QaseIO(9)
def test():
    head = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer e91cd771350a43675d8778d2ffae8369de707d4c962c53611b374782346b9fb7"
    }
    req = requests.get(api_user_invalid, headers=head)

    # VALIDATION
    status_code = req.status_code

    # ASSERT
    assert_that(status_code).is_equal_to(404)
