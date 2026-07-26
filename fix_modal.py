with open("index.html","r",encoding="utf-8") as f: html=f.read()
old='document.getElementById("landing").style.display="none";'
new='document.getElementById("modal").classList.remove("active");'+old
html=html.replace(old,new)
with open("index.html","w",encoding="utf-8") as f: f.write(html)
print("done")
