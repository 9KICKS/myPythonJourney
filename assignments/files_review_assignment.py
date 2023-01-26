import pathlib

path = pathlib.Path.cwd()
my_folder = path / "my_folder/"
my_folder.mkdir(exist_ok=True)
print(path)

images = my_folder / "images/"
images.mkdir(parents=True, exist_ok=True)

file_path = [
    my_folder / "file1.txt",
    my_folder / "file2.txt",
    my_folder / "image1.png"
]

for path in file_path:
    path.touch()
print(path)

source = my_folder / "image1.png"
destination = images / "image1.png"
source.replace(destination)

delete_file1 = my_folder / "file1.txt"
delete_file1.unlink(missing_ok=True)

delete_file2 = my_folder / "file2.txt"
delete_file2.unlink(missing_ok=True)

delete_file3 = images / "image1.png"
delete_file3.unlink(missing_ok=True)

delete_folder1 = my_folder / "images/"
delete_folder1.rmdir()

delete_folder2 = pathlib.Path.cwd() / "my_folder/"
delete_folder2.rmdir()
