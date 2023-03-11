f = open("contacts.vcf", "r")
updatedContacts = ""
cnt = 0
for line in f:
    if "TEL;" in line:
        cnt += 1
        numStartIndex = line.rfind(":")+1
        number = line[numStartIndex:]
        newNumber = number
        if number[:1] == '0':
            newNumber = "+91" + number[1:]
        elif number[:1] != "+":
            newNumber = "+91" + number
        updatedContacts += line[:numStartIndex] + newNumber
    else:
        updatedContacts += line

f = open("updatedContacts.vcf", "w")
f.write(updatedContacts)
f.close()
