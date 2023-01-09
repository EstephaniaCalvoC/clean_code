from os import system, getenv, path


COMPANY_NAME = "Mega SA"
FILE_NAME = "mega_sa.csv"


def run_command(command):
    """Run the indicated command in the system"""
    program_location = getenv("EMS_LOCATION")
    exit_code = system(f'echo "{command}\nclose" | {program_location}')
    return exit_code


def test_create_company(tmp_path):
    abs_path = tmp_path.absolute()
    exit_code = run_command(f"create_company {COMPANY_NAME}, {abs_path}")

    assert exit_code == 0
    assert path.exists(f"{abs_path}/{FILE_NAME}")

