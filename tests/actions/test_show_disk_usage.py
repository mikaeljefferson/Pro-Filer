from pro_filer.actions.main_actions import show_disk_usage


def test_file_empty(capsys):
    context = {
        "all_files": []
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_output = ("Total size: 0\n")
    assert captured.out == expected_output


def test_show_disk_usage_multipli_files(tmp_path, capsys):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    path1 = str(file1)
    path2 = str(file2)

    with open(path1, "w") as file1:
        file1.write("this is the first file to test")
    with open(path2, "w") as file2:
        file2.write("another file")

    context = {"all_files": [path1, path2]}

    first_line1 = f"'{path1[:27]}...{path1[-30:]}':".ljust(71)
    first_line2 = f"30 ({int(30 / 42 * 100)}%)"
    second_line1 = f"'{ path2[:27]}...{ path2[-30:]}':".ljust(71)
    second_line2 = f"12 ({int(12 / 42 * 100)}%)"
    first_result = f"{first_line1}{first_line2}\n"
    second_result = f"{second_line1}{second_line2}\n"
    result = first_result + second_result + "Total size: 42\n"

    show_disk_usage(context)
    captured = capsys.readouterr()

    assert captured.out == result
