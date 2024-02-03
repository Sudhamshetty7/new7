import re
mail_data="sudham <sudhamkshetty7@gmail.com>, ashish <ahmsagar@gmail.com>, sudhan <sudhamkshetty@gmail.com>"
val = re.findall("sudh", mail_data)
print (val)

mail_data="sudham <sudhamkshetty7@gmail.com>, ashish <ahmsagar@gmail.com>, sudhan <sudhamkshetty@gmail.com>"
val = re.search("sudh", mail_data)
print (val)
