import re

content1 = '2020-07-14 11:00'
content2 = '2020-06-15 12:00'
content3 = '2020-05-16 13:00'
pattern = re.compile(r'\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)