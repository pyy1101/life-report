with open("index.html","r",encoding="utf-8") as f: html=f.read()

# Wrap entire generate function body in try-catch
# Find: window.generate=function(){ LET TP=...
# Replace function body start with try{
old='window.generate=function(){let tp=_type'
new='window.generate=function(){try{let tp=_type'
html=html.replace(old,new)

# Find end of generate: the line that shows report page and add }catch before it
old2='document.getElementById("landing").style.display="none";'
new2='}catch(e){alert("Error: "+e.message+" at line "+e.lineNumber)}document.getElementById("landing").style.display="none";'
html=html.replace(old2,new2)

with open("index.html","w",encoding="utf-8") as f: f.write(html)
print("done")
