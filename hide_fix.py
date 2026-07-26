with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# In the inline onclick report HTML:
# Replace class=locked with style='display:none'
# The HTML is inside xh+='...' (single-quoted JS strings)
html = html.replace("class=locked", "style='display:none'")

# Fix unlock to clear inline style
html = html.replace(
    "function unlock(){var all=document.querySelectorAll('#rContent .locked');for(var i=0;i<all.length;i++){all[i].style.display=''};document.querySelector('.unlock-box').innerHTML='<p style=color:#aaa>已解锁</p>'",
    "function unlock(){var all=document.querySelectorAll(\"#rContent [style='display:none']\");for(var i=0;i<all.length;i++){all[i].style.display=''};document.querySelector('.unlock-box').innerHTML='<p style=color:#aaa>已解锁</p>'"
)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
