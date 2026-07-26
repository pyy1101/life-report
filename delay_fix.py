with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the hiding code with a setTimeout version
old = """document.getElementById('rContent').innerHTML=xh;
var locks=document.getElementById('rContent').getElementsByClassName('locked');
while(locks.length>0){locks[0].style.display='none';locks[0].classList.remove('locked')}"""

new = """document.getElementById('rContent').innerHTML=xh;
setTimeout(function(){
  var locks=document.getElementById('rContent').getElementsByClassName('locked');
  while(locks.length>0){locks[0].style.display='none';locks[0].classList.remove('locked')}
},100);"""

html = html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
