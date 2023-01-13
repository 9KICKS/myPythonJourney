import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1 / "folder_a"
folder_a.mkdir(exist_ok=True)
print(path1)
# The above syntax will create a folder in current directory

file_paths = [
    folder_a / "private.ing",
    folder_a / "my eys only.jpg",
    folder_a / "lyrics.txt",
    folder_a / "alone.vid",
    folder_a / "inside.csv",
    folder_a / "bible.txt"
]
for path in file_paths:
    path.touch()
print(path1)
# The above syntax will create files in the folder

print(list(folder_a.iterdir()))
# The above syntax will show the path of the folder

print()

for file in folder_a.iterdir():
    print(file.name)
# The above syntax will print out all the files in the folder

print()

for files in path1.iterdir():
    print(files.name)
# The above syntax will print out all the files in cohort14_projects except the newly created folder_a folder

print()

for files in folder_a.glob("*txt"):
    print(files.name)
# The above .glob syntax filters or get the files

print()

for files in path1.glob("**/*.txt"):
    print(files.name)
# The above syntax shows all the files with .txt in the current directory

print()

source = path1 / "folder_a" / "lyrics.txt"
destination = path1 / "files_example_folder" / "lyrics.txt"
source.replace(destination)
# The above syntax moves a file from one folder to another folder

# .unlink() - to delete a file
# .rmdir() - to remove directory

