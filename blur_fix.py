with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# After showing report, add blur overlay to locked sections
old = "document.getElementById('rContent').innerHTML=xh;"
new = """document.getElementById('rContent').innerHTML=xh;
setTimeout(function(){
  var sec=document.querySelectorAll('#rContent .rs');
  for(var i=2;i<sec.length;i++){
    sec[i].style.filter='blur(8px)';
    sec[i].style.position='relative';
    sec[i].style.pointerEvents='none';
  }
  var box=document.querySelector('.unlock-box');
  if(box){box.style.filter='none';box.style.pointerEvents='auto'}
},100);"""
html = html.replace(old, new)

# Fix unlock to clear blur
old2 = 'function unlock(){var mbd="https://mbd.pub/o/bread/YZaUlplxaA==";window.location.href=mbd;return;'
new2 = 'function unlock(){var sec=document.querySelectorAll("#rContent .rs");for(var i=0;i<sec.length;i++){sec[i].style.filter="";sec[i].style.pointerEvents="auto"}document.querySelector(".unlock-box").innerHTML="<p>已解锁</p>"}'
html = html.replace(old2, new2)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
