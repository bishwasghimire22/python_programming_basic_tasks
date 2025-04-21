from pathlib import Path
my_dict = {}
data = "postcodes.csv"
script_dir = Path(__file__).parent
file_path = script_dir / data
contents = file_path.read_text(encoding="UTF-8")
lines = contents.splitlines()

for line in lines:
    fields = line.split(';')
    my_dict[fields[0]]= (fields[1], fields[2])
print(my_dict)