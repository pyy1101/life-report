with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the unlock box line in the inline onclick and add lucky section before it
old = "xh+='<div class=unlock-box>"
new = """xh+='<div class=rs><h2>五、专属幸运密码</h2><div class=lucky-box>';
xh+='<div class=lucky-item><div class=num>'+pk(LC||[],xr)+'</div><div class=label>幸运色</div></div>';
xh+='<div class=lucky-item><div class=num>'+pk(LN||[],xr)+'</div><div class=label>幸运数字</div></div>';
xh+='<div class=lucky-item><div class=num>'+pk(LI||[],xr)+'</div><div class=label>好运信物</div></div>';
xh+='</div><p style=\"text-align:center;margin-top:12px;color:rgba(200,190,170,.5)\"> * '+pk(LA||[],xr)+'</p></div>';
xh+='<div class=unlock-box>"""
html = html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
