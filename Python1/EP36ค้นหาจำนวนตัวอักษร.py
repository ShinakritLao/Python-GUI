message = ["aa","aab","cba","bba","aba","cca","aaaaaa"]
result = []

for item in message :
    result.append(item.count("a"))
print(result)