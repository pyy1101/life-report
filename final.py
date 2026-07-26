with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add lucky section before unlock box
old = "xh+='<div class=unlock-box>"
new = """xh+='<div class=rs><h2>五、专属幸运密码</h2><div class=lucky-box><div class=lucky-item><div class=num>'+pk(LC||[],xr)+'</div><div class=label>幸运色</div></div><div class=lucky-item><div class=num>'+pk(LN||[],xr)+'</div><div class=label>幸运数字</div></div><div class=lucky-item><div class=num>'+pk(LI||[],xr)+'</div><div class=label>好运信物</div></div></div><p style=\"text-align:center;margin-top:12px;color:rgba(200,190,170,.5)\"> * '+pk(LA||[],xr)+'</p></div>';xh+='<div class=unlock-box>"""
html = html.replace(old, new)

# 2. Add blur to sections 3+ after render
old2 = "document.getElementById('rContent').innerHTML=xh;"
new2 = """document.getElementById('rContent').innerHTML=xh;setTimeout(function(){var s=document.querySelectorAll('#rContent .rs');for(var i=2;i<s.length;i++){s[i].style.filter='blur(8px)';s[i].style.pointerEvents='none'}var b=document.querySelector('.unlock-box');if(b){b.style.filter='none';b.style.pointerEvents='auto'}},100);"""
html = html.replace(old2, new2)

# 3. Fix unlock to clear blur
old3 = 'function unlock(){var mbd="https://mbd.pub/o/bread/YZaUlplxaA==";window.location.href=mbd;return;'
new3 = 'function unlock(){var s=document.querySelectorAll("#rContent .rs");for(var i=0;i<s.length;i++){s[i].style.filter="";s[i].style.pointerEvents="auto"}document.querySelector(".unlock-box").innerHTML="<p>已解锁</p>"}'
html = html.replace(old3, new3)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
