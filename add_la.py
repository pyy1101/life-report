with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the unlock box line in genReport and add lucky action before it
# Replace the </div></div> that closes lucky section to include action text
old = "h+='</div></div>';h+='<div class=unlock-box>"
new = "h+='</div><p style=text-align:center;margin-top:12px;color:rgba(200,190,170,.5)> * '+pk(LA||[],r)+'</p></div>';h+='<div class=unlock-box>"

html = html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
