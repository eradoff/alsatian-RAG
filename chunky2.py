import re

LANDMARKS = {
    "The safety innovations": "innovation",
    "Safety philosophy & systems": "philosophy",
    "Open engineering problems": "problem",
}

with open("Alsatian_Vehicle_Safety_Brief_Session_text") as f:
    lines = f.readlines()

print(f"{len(lines)} lines read")

def is_title(line):
    return (re.match(r"^\d+\s+—\s+", line) is not None
           or re.match(r"^\d+\.\s+\S", line) is not None)


def seal(chunk, pile):
    if chunk["text"].strip() == "":
        chunk["text"] = chunk["title"]
    pile.append(chunk)

chunks = []
current = None
mode = None

for line in lines:
    stripped = line.strip()
    if stripped in LANDMARKS:
        mode = LANDMARKS[stripped]
        if current is not None:
            seal(current, chunks)
        current = {"title": stripped, "kind": mode, "text": ""} 
        continue
    if is_title(line):
        if current is not None:
            seal(current, chunks)
        current = {"title": stripped, "kind" : mode, "text": ""}
        continue  

    elif current is not  None:
        current["text"] += line
        
if current is not None:
    seal(current, chunks)
#    print(chunks)
print(f"{len(chunks)} chunks created")
for c in chunks:
    print(f" [{c['kind']}] {c['title']} ({len(c['text'])} chars)")
   # print(chunks[14]["text"])
