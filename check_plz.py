import re
from pathlib import Path

folder = Path(r"C:\Users\m.rahman\MyThesis_v4\2-MainMattar")
files = folder.glob("thChap*.tex")
pattern = re.compile(r'(?<!["\'])\b\d{4,}\b(?!["\'])')

results = {}
for file in files:
    text = file.read_text(encoding="utf-8", errors="ignore")
    matches = pattern.findall(text)
    results[file.name] = matches

for fname, nums in results.items():
    print(f"{fname}: {nums}")
