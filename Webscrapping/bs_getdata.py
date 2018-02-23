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
		<li class="super-mega special"> Hi </li>
		<li class="special"> Hi </li>
		<li> nonspitem </li>
	</ol>
	<div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
el = soup.select(".special")[0] #first element with class special
for el in soup.select(".special"):
	print(el.name + el.get_text()) # li Hi
	print(el.attrs) # gives it attr on a dic

attr = soup.find("div")["id"] #directly access attributes
print(attr)