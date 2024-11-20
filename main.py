import re 
test_str = "Coding"
res = []
for i in range(len(test_str)):
    for j in range(i+1, len(test_str)+1):
        res.append(re.sub(r'\W+', '', test_str[i:j]))
print("All substrings of string are: " + str(res)) 