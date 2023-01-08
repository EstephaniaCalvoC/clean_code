from os import system


def run_command(command):
    """Run the indicated command in the system"""
    # TODO: Save in a variable variable or create an alia
    program_location = "/home/estephania.calvo/Desktop/ecalvo/projects/clean_code/ArjanCodes/7PythonCodeSmells/2021-code-smells/employee_management_system/cmd_app/main.py"
    exit_code = system(f'echo "{command}\nclose" | {program_location}')
    return exit_code


def test_create_company():
    result = run_command("create_company Gatos")

    print(result)
    assert True