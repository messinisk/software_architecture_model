from software_architecture_model_python.utils.fs import (
    ensure_directory,
    read_text,
    write_text,
)


def test_ensure_directory(tmp_path):
    target = tmp_path / "subdir"

    result = ensure_directory(target)

    assert result.exists()
    assert result.is_dir()


def test_write_and_read_text(tmp_path):
    file_path = tmp_path / "sample.txt"

    write_text(file_path, "hello")

    assert file_path.exists()
    assert read_text(file_path) == "hello"