from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
<head>
	<title>BS4 Testing</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text</p>
	</div>
	<ol>
		<li class="special"> Hi </li>
		<li class="special"> Hi </li>
		<li> nonspitem </li>
	</ol>
	<div>bye</div>
</body>
</html>
"""
#soup.find returns an object ( first one that appears )
#soup.find_all gives a list
#soup.select also gives a list
#How to find things
soup = BeautifulSoup(html, "html.parser")
print(soup.find_all(class_="special")) #Gets two itens in a list
d = soup.select('.special') #gets a list from elements which id is first
print(d)


