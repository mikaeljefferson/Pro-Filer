from pro_filer.actions.main_actions import show_details
import pytest
from datetime import date


@pytest.fixture
# testa os arquivos
def test_file(tmp_path):
    file = tmp_path / "xesque_file.txt"
    file.touch()
    return file


# testa com extensao
def test_show_details_existing_extension(capsys, test_file):
    context = {"base_path": str(test_file)}
    show_details(context)
    output = capsys.readouterr()

    today_date = date.today().strftime("%Y-%m-%d")
    expected_output = (
        f"File name: xesque_file.txt\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: .txt\n"
        f"Last modified date: {today_date}\n"
    )

    assert output.out == expected_output


# testa sem ter extensao
def test_show_details_no_existing_extension(capsys, tmp_path):
    file = tmp_path / "xesque_file"
    file.touch()
    context = {"base_path": str(file)}
    show_details(context)
    output = capsys.readouterr()

    today_date = date.today().strftime("%Y-%m-%d")
    expected_output = (
        f"File name: xesque_file\n"
        f"File size in bytes: 0\n"
        f"File type: file\n"
        f"File extension: [no extension]\n"
        f"Last modified date: {today_date}\n"
    )

    assert output.out == expected_output


# testa se arquivoi n existe
def test_show_details_file_not_exist(capsys):
    context = {"base_path": "/path/to/xesque/file.txt"}
    show_details(context)
    output = capsys.readouterr()
    expected_output = "File 'file.txt' does not exist\n"
    assert output.out == expected_output
