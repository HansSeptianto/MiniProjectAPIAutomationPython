import pytest

from setting.case_management import update_test_results


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    # BEFORE TEST
    print("====================== Before Test ======================")
    get_error = request.session.testsfailed

    yield
    # AFTER TEST
    print("====================== After Test ======================")
    test_status = request.session.testsfailed - get_error
    test_case_id = request.node.get_closest_marker("QaseIO").args[0]

    if test_status == 0:
        update_test_results(test_case_id, "passed")
    else:
        update_test_results(test_case_id, "failed")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE
    print("====================== Before All ======================")

    yield
    # AFTER SUITE
    print("====================== After All ======================")
