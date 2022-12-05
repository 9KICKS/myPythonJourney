

from pathlib import Path

fake_path = Path("c:/kellogs/hello.txt")
cwd_path = Path.cwd() / "Folahan" / "numbers" / "green.csv"
print(cwd_path)
#print("Parent -", fake_path.parent)
#print(Path.parents)
#print(list(fake_path.parents))
#print("Anchor - ", fake_path.anchor)
#print("Name - ", fake_path.name)
#print("Suffix - ", fake_path.suffix)
#print("Stem - ", fake_path.stem)

#cwd_path.mkdir()
#cwd_path.mkdir(exist_ok=True)
#new_file_path = cwd_path / "private.txt"
#new_file_path.touch()
#print(fake_path.exists())
#print(cwd_path.exists())
#print("isDir - ", cwd_path.is_file())
#print("isDir - ", cwd_path.is_dir())

cwd_path.parent.mkdir()

