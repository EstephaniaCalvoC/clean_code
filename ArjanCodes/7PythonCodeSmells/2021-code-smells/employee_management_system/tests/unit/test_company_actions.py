import pytest
from cmd_app.main import EmployeeManagementSystem
from cmd_app.company import Company
from os import path

COMPANY = "MEGA SA"
SUCCESS_RESPONSE = "Success"
DATA_FILE_NAME = "mega_sa.csv"

COMPANY_DATA = [
            '"employee_id","name","role","type","payment"',
            '"c29123f2-e3e2-4445-a5e2-8af72ff95a54","Joe Spal","PRESIDENT","SALARY","15000"',
            '"a7f2a39d-3543-4220-a257-d5993f383cfd","Eduard Rosich","WORKER","SALARY","3000"',
            '"150fa941-c8cc-48b0-bfd6-529a7519a4fc","Clare Bonett","WORKER","HOURLY","15"',
            '"6e7a71b5-1b11-4622-9374-e7a24221bd89","Pedro Sanchéz","LEAD","SALARY","5000"',
            '"4a5d1d4a-2831-4bee-8744-1eb8359683d6","Lucrezia Jovanotti","LEAD","SALARY","5000"',
            '"6c1e0994-5c0e-4342-857c-e377d6289bbb","Arturo Calle","WORKER","HOURLY","15"',
            '"de1b0645-1760-48b7-b7b4-25ddd85a0a0e","Christin Stovall","WORKER","HOURLY","15"',
            '"933efa9a-25eb-412e-ba59-425d8153877c","Michel Curtis","MANAGER","SALARY","6000"',
            '"b35b3f84-3078-46d8-b123-7491f13405fc","Ali Aher","WORKER","HOURLY","15"',
            '"c8ac21b1-4635-40a8-b1ae-79c7f27898b6","Daniel Komissarov","VICEPRESIDENT","SALARY","10000"'
        ]


@pytest.fixture
def ems():
    return EmployeeManagementSystem()


@pytest.fixture
def data_file_path(tmp_path):
    data_file_path = f"{tmp_path}/{DATA_FILE_NAME}"
    with open(data_file_path, "w") as f:
        [f.write(line) for line in COMPANY_DATA]

    return data_file_path


def validate_logs(output_text, error_text, messages):
    return all([message in output_text for message in messages]) and error_text == ""


def test_create_company(tmp_path, capsys, ems):
    abs_path = str(tmp_path.absolute())

    ems.do_create_company(f"{COMPANY}, {abs_path}")

    out, err = capsys.readouterr()

    assert validate_logs(out, err, [SUCCESS_RESPONSE, abs_path, DATA_FILE_NAME])

    assert path.exists(f"{abs_path}/{DATA_FILE_NAME}")


def test_load_data(capsys, ems, data_file_path):
    number_of_records = len(COMPANY_DATA) - 1

    ems.do_load(f"{COMPANY} {data_file_path}")

    out, err = capsys

    assert validate_logs(out, err, [SUCCESS_RESPONSE, data_file_path, number_of_records])
    # TODO: Validate the ids as keys of the dictionary employess
    assert len(ems.company.get_employess()) == number_of_records
