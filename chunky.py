import re

EXTRA_HEADINGS = [
    "Safety philosophy & systems",
    # ...the rest you harvest
]

with open("Alsatian_Vehicle_Safety_Brief_Session_text") as f:
    lines =  f.readlines()

print(f"{len(lines)} lines read")

def is_title(line):
    return (re.match(r"^\d+\s+—\s+", line) is not None
           or re.match(r"^\d+\.\s+\S", line) is not None)
#for i, line in enumerate(lines):
#    if is_title(line):
#        print(f"line {i}: {line.strip()}")

chunks = []
current = None

for line in lines:
    if is_title(line) or line.strip() in EXTRA_HEADINGS:
        if current is not None:
            chunks.append(current)
        current = {"title": line.strip(), "text": ""} 
        print(current)
    elif current is not None:
        current["text"] += line

if current is not None:
    chunks.append(current)

print(f"{len(chunks)} chunks created")
for c in chunks:
    print(f"  {c['title']} ({len(c['text'])} chars)")
    print(chunks[-1]["text"][-600:])