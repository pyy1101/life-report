with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Current button: <button class="submit-btn" onclick="try{...very long...}">✨ 解锁前世今生</button>
# Replace with: <button class="submit-btn" id="genBtn-life">✨ 解锁前世今生</button>
# Then bind click in start() after box.innerHTML

# Find the onclick with try{...} and replace with id
import re
# Match: onclick="try{...very long...}"
old_onclick = r'onclick="try\{[^}]*generate\(\).*?\}"'
match = re.search(old_onclick, html)
if match:
    # Replace the onclick with an id
    html = html.replace(match.group(), 'id="genBtn-life"')
    print("replaced onclick with id")
else:
    print("onclick pattern not found")
    # Try simpler: find onclick="try and replace up to the closing "
    idx = html.index('onclick="try{')
    # Find the closing " after the onclick - look for the next " after try block
    end = html.index('">✨ 解锁前世今生', idx)
    old = html[idx:end]
    html = html[:idx] + 'id="genBtn-life"' + html[end:]
    print("fallback: replaced from index")

# Now bind the click in start(). Find where start() calls classList.add('active')
old_start = "document.getElementById('modal').classList.add('active');"
new_start = """document.getElementById('modal').classList.add('active');
setTimeout(function(){
  var b=document.getElementById('genBtn-life');
  if(b)b.onclick=function(){
    try{
var xyr=parseInt((document.getElementById('fYear')||{}).value)||2000;
var xmo=parseInt((document.getElementById('fMonth')||{}).value)||6;
var xda=(document.getElementById('fDay')||{}).value||'15';
var xr=sd((xyr*10000+xmo*100+parseInt(xda)).toString());
var xpl=P?pk(P,xr):{t:'Test',d:'Test desc'};
var xts=G?pks(G,3,xr):[['T1','d1'],['T2','d2'],['T3','d3']];
var xad=A?pk(A,xr):['Test','desc'];
var xad2=A?pk(A,xr):['Test2','desc2'];
var xbs=B?pks(B,3,xr):[['B1','f1'],['B2','f2'],['B3','f3']];
var xh='';
xh+='<p style=color:#888>'+xyr+'.'+xmo+'.'+xda+'</p>';
xh+='<div class=rs><h2>一、前世身份：'+xpl.t+'</h2><p>'+xpl.d+'</p></div>';
xh+='<div class=rs><h2>二、今生隐藏天赋</h2>'+xts.map(function(x,i){return '<p><b>'+(i+1)+'. '+x[0]+'：</b>'+x[1]+'</p>'}).join('')+'</div>';
xh+='<div class=rs><h2>三、2026年奇遇剧本（预览）</h2><p>'+xad[0]+'：'+xad[1]+'</p><p class=locked>'+xad2[0]+'：'+xad2[1]+'</p><p class=locked>避坑提醒：'+(xmo||1)+'月前后注意财务决策。</p></div>';
xh+='<div class=rs locked><h2>四、人生Bug修复指南</h2>'+xbs.map(function(x,i){return '<p>'+(i+1)+'. '+x[0]+'：'+x[1]+'</p>'}).join('')+'</div>';
xh+='<div class=rs locked><h2>五、专属幸运密码</h2><div class=lucky-box><div class=lucky-item><div class=num>'+pk(LC||[],xr)+'</div><div class=label>幸运色</div></div><div class=lucky-item><div class=num>'+pk(LN||[],xr)+'</div><div class=label>幸运数字</div></div><div class=lucky-item><div class=num>'+pk(LI||[],xr)+'</div><div class=label>好运信物</div></div></div></div>';
xh+='<div class=unlock-box><h3>解锁完整报告</h3><p>完整奇遇 · Bug修复 · 幸运密码</p><button class=btn onclick=unlock()>解锁完整版</button></div>';
document.getElementById('modal').classList.remove('active');
document.getElementById('landing').style.display='none';
document.getElementById('reportPage').classList.add('active');
document.getElementById('rContent').innerHTML=xh;
setTimeout(function(){
var s=document.querySelectorAll('#rContent .rs');
for(var i=2;i<s.length;i++){s[i].style.filter='blur(8px)';s[i].style.pointerEvents='none'}
var b=document.querySelector('.unlock-box');
if(b){b.style.filter='none';b.style.pointerEvents='auto'}
},100);
}catch(e){alert(e.message)}
  };
},100);"""
html = html.replace(old_start, new_start)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
