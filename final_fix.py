with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# After innerHTML=xh, add JS hiding
old1 = "document.getElementById('rContent').innerHTML=xh;"
new1 = """document.getElementById('rContent').innerHTML=xh;
var locks=document.getElementById('rContent').getElementsByClassName('locked');
while(locks.length>0){locks[0].style.display='none';locks[0].classList.remove('locked')}"""
html = html.replace(old1, new1)

# Fix unlock to show hidden elements
old2 = 'function unlock(){var mbd="https://mbd.pub/o/bread/YZaUlplxaA==";window.location.href=mbd;return;'
new2 = 'function unlock(){var all=document.querySelectorAll("#rContent [style*=\\"none\\"]");for(var i=0;i<all.length;i++){all[i].style.display=""};document.querySelector(".unlock-box").innerHTML="<p>已解锁</p>"'
html = html.replace(old2, new2)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
