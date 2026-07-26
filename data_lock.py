with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Approach: use data-lock="1" instead of class=locked
# This avoids ALL HTML parsing issues with unquoted class attributes

# 1. Replace class=locked with data-lock=1 in the inline onclick
html = html.replace("class=locked", "data-lock=1")

# 2. After innerHTML, hide data-lock elements
old = "document.getElementById('rContent').innerHTML=xh;"
new = """document.getElementById('rContent').innerHTML=xh;
setTimeout(function(){
var all=document.querySelectorAll('#rContent [data-lock]');
for(var i=0;i<all.length;i++){all[i].style.display='none'}
},100);"""
html = html.replace(old, new)

# 3. Fix unlock to show these elements
old2 = 'function unlock(){var mbd="https://mbd.pub/o/bread/YZaUlplxaA==";window.location.href=mbd;return;'
new2 = 'function unlock(){var all=document.querySelectorAll("#rContent [data-lock]");for(var i=0;i<all.length;i++){all[i].style.display=""};document.querySelector(".unlock-box").innerHTML="<p>已解锁</p>"'
html = html.replace(old2, new2)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
