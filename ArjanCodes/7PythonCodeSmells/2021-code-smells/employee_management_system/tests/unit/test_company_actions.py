import pytest
from cmd_app.main import EmployeeManagementSystem
from os import path

COMPANY = "MEGA SA"
SUCCESS_RESPONSE = "Success:"


@pytest.fixture
def ems():
    return EmployeeManagementSystem()


@pytest.fixture()
def file_name():
    return "_".join(COMPANY.lower().split(" ")) + ".csv"


def test_create_company(tmp_path, capsys, ems, file_name):
    abs_path = str(tmp_path.absolute())

    ems.do_create_company(f"{COMPANY}, {abs_path}")

    out, err = capsys.readouterr()

    assert all([message in out for message in [SUCCESS_RESPONSE, abs_path, file_name]])
    assert err == ""
    assert path.exists(f"{abs_path}/{file_name}")

