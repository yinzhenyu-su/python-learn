from urllib import request
name = "q"
resp = request.urlopen("http://mm.howkuai.com/wp-content/uploads/2017a/04/03/02.jpg", timeout=20)
data = resp.read()
with open(name + ".jpg", "wb") as file_obj:
    file_obj.write(data)