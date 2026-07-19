from pypdf import PdfReader

reader = PdfReader("Alsatian_Vehicle_Safety_Brief_Session_1_22.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("Alsatian_Vehicle_Safety_Brief_Session_text", "w") as f:
    f.write(text)

print(f"Extracted {len(reader.pages)} pages, {len(text)} characters")


