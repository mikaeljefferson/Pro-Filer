from pro_filer.actions.main_actions import show_preview


# testa saida arquivos
def test_show_preview(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )


# testa se esta o contexto vazio
def test_show_preview_is_empty_context(capsys):
    empty_context = {"all_files": [], "all_dirs": []}

    show_preview(empty_context)

    captured = capsys.readouterr()
    output = captured.out

    assert "Found 0 files and 0 directories" in output
# testa se que exibem mais do que 5 arquivos e/ou diretórios


def test_show_preview_rejet_more_five(capsys):
    context = {
        "all_files": [
            "file1.txt",
            "file2.txt",
            "file3.txt",
            "file4.txt",
            "file5.txt",
            "file6.txt",
        ],
        "all_dirs": ["dir1", "dir2", "dir3"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    output = captured.out

    assert "Found 6 files and 3 directories" in output
    assert "First 5 files: ['file1.txt', 'file2.txt', 'file3.txt', " \
           "'file4.txt', 'file5.txt']" in output
    assert "First 5 directories: ['dir1', 'dir2', 'dir3']" in output
