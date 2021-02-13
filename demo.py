from urllib import parse

with open("demo.txt", "r", encoding="utf=8") as q:

    result = q.read()
    print(parse.unquote(result))
