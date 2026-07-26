with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The issue: class=rs locked is parsed as class="rs" + locked attribute
# Fix: use class="rs locked" with quotes
html = html.replace("class=rs locked", 'class="rs locked"')

# Also quote class=locked for consistency (though it works without)
# But class=locked (no space) IS already correct, keep as-is

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
