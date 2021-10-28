from urllib.request import urlopen


html=urlopen("http://coderbook.top")
content=str(html.read())
filename='pygame.html'
with open(filename,'w',encoding='utf-8') as file_obj:
    file_obj.write(content)
