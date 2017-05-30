INPUT_FILE = 'English.to.Chinese'
HTML_1ST_HALF = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    font-family: -apple-system, BlinkMacSystemFont, arial, sans-serif;
    table-layout: fixed;
    width: 100%;
}

td, th {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #b5e5b5;
}
</style>
</head>
<body>

<table>
  <tr>
    <th width="33%">English</th>
    <th width="34%">Annotation</th>
    <th width="33%">Chinese</th>
  </tr>
"""
TR_TEMPLATE = """
  <tr>
    <td>{english}</td>
    <td>{annotation}</td>
    <td>{chinese}</td>
  </tr>
"""
HTML_2ND_HALF = """
</table>

</body>
</html>
"""


html = HTML_1ST_HALF

with open(INPUT_FILE, 'r') as f_r:
    for line in f_r:
        english, annotation, chinese = line.strip().split(':')
        html += TR_TEMPLATE.format(
            english=english,
            annotation=annotation,
            chinese=chinese,
        )
html += HTML_2ND_HALF

with open('index.html', 'w') as f_w:
    f_w.write(html)
