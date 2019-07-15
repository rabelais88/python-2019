import re

mystr = "I'm in the woods all alone"

searched = re.search("woods", mystr)
matched = re.match("woods", mystr)  # match is automatically anchored to the start

result = {"searched": searched, "matched": matched}
print(result["searched"])

print(matched == None) # None object == null object in JS, java

matched_two = re.search(r"WOODS", mystr, re.IGNORECASE)
print(matched_two)

replaced = re.sub(r"[ao]", "e", mystr);
print(replaced)