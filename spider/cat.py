import urllib.request as request

# response = request.urlopen("http://www.fishc.com")

# html = response.read()

# html = html.decode("utf-8")

# print(html)

response = request.urlopen("http://placekitten.com/g/200/300")
cat_image = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_image)
