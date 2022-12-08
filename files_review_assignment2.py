import pathlib

package = pathlib.Path.cwd()
folder = package / "Practice Files folder"
folder.mkdir(exist_ok=True)

documents = folder / "documents/"
documents.mkdir(exist_ok=True)

sub_folder = documents / "Sub folder"
sub_folder.mkdir(exist_ok=True)

path = [
    documents / "images1.png",
    documents / "images2.gif",
    documents / "images3.png",
    documents / "images4.jpg",
]

for file in path:
    file.touch(exist_ok=True)

image = folder / "Images"
image.mkdir(exist_ok=True)

source = documents / "images1.png"
destination = image / "images1.png"
source.replace(destination)

source = documents / "images2.gif"
destination = image / "images2.gif"
source.replace(destination)

source = documents / "images3.png"
destination = image / "images3.png"
source.replace(destination)

source = documents / "images4.jpg"
destination = image / "images4.jpg"
source.replace(destination)
