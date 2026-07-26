with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# After setting innerHTML, hide locked elements with JS
old = "document.getElementById('rContent').innerHTML=xh;"
new = """document.getElementById('rContent').innerHTML=xh;
setTimeout(function(){
var all=document.querySelectorAll('#rContent .locked');
for(var i=0;i<all.length;i++){all[i].style.display='none'}
},50);"""
html = html.replace(old, new)

# Fix unlock
old2 = 'function unlock(){var mbd="https://mbd.pub/o/bread/YZaUlplxaA==";window.location.href=mbd;return;'
new2 = 'function unlock(){var all=document.querySelectorAll("#rContent .locked");for(var i=0;i<all.length;i++){all[i].style.display=""};document.querySelector(".unlock-box").innerHTML="<p style=color:#aaa>已解锁</p>"'
html = html.replace(old2, new2)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
