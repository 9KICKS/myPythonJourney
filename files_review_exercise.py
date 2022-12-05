from pathlib import Path

#print(Path.home())
#file_path = Path.home() / "my_folder"
#file_path.mkdir(exist_ok=True)
#new_file_path = file_path / "my_file.txt"
#new_file_path.touch(exist_ok=True)
#print(new_file_path.name)
#print(new_file_path.parent.name)

file_path = Path.home() / "my_folder" / "my_file.txt"
file_path.parent.mkdir(exist_ok=True)
#file_path.parent.mkdir()
file_path.touch(exist_ok=True)
#file_path.touch()
print(file_path.parent.exists())
print(file_path.exists())
