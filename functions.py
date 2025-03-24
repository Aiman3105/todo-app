import zipfile
import pathlib
FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def make_archive(filepaths, dest_dir):
    dest_path=pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def unpack_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(dest_dir)

if __name__== "__main__":
    make_archive(filepaths=["todos.txt", "test2.py"], dest_dir="Zip")


