from bs4 import BeautifulSoup
#Finding parents, siblings and etc

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
		<li class="super-mega special"> Hi </li>
		<li class="special"> Hi </li>
		<li> nonspitem </li>
	</ol>
	<div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
data = soup.find(class_="super-mega")

print(data) # li
print(data.parent) # ol
print(data.find_next_sibling()) # gets the next li


