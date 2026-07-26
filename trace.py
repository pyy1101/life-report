with open("index.html","r",encoding="utf-8") as f: html=f.read()

# Add trace alerts before validation
old='if(!yr||!mo||!da){alert('
new='alert("yr="+yr+" mo="+mo+" da="+da);'+old
html=html.replace(old,new)

with open("index.html","w",encoding="utf-8") as f: f.write(html)
print("done")
