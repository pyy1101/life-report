with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# Add showReport before generate
old = 'window.generate=function(){'
new = 'window.showReport=function(){document.getElementById("modal").classList.remove("active");document.getElementById("landing").style.display="none";document.getElementById("reportPage").classList.add("active");document.getElementById("rContent").innerHTML="<h1>WORKING!</h1><p>Report page is showing</p>";window.scrollTo(0,0)};' + old
html = html.replace(old, new)

# Change button onclick
html = html.replace('onclick="window.generate()"', 'onclick="window.showReport()"')

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
