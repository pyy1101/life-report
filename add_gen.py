with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add genReport function before unlock
old = "function unlock(){"
new = """// [报告生成] 读表单→生成完整报告→模糊锁定章节
window.genReport=function(){
  try{
    var yr=parseInt((document.getElementById('fYear')||{}).value)||2000;
    var mo=parseInt((document.getElementById('fMonth')||{}).value)||6;
    var da=(document.getElementById('fDay')||{}).value||'15';
    var r=sd((yr*10000+mo*100+parseInt(da)).toString());
    var pl=P?pk(P,r):{t:'Default',d:'Default'};
    var ts=G?pks(G,3,r):[['T1','d1'],['T2','d2'],['T3','d3']];
    var ad=A?pk(A,r):['Default','Default'];
    var ad2=A?pk(A,r):['Default2','Default2'];
    var bs=B?pks(B,3,r):[['B1','f1'],['B2','f2'],['B3','f3']];
    var h='';
    h+='<p style=color:#888>'+yr+'.'+mo+'.'+da+'</p>';
    h+='<div class=rs><h2>一、前世身份：'+pl.t+'</h2><p>'+pl.d+'</p></div>';
    h+='<div class=rs><h2>二、今生隐藏天赋</h2>'+ts.map(function(x,i){return'<p><b>'+(i+1)+'. '+x[0]+'：</b>'+x[1]+'</p>'}).join('')+'</div>';
    h+='<div class=rs><h2>三、2026年奇遇剧本</h2><p>'+ad[0]+'：'+ad[1]+'</p><p class=locked>'+ad2[0]+'：'+ad2[1]+'</p><p class=locked>避坑提醒：'+(mo||1)+'月前后注意财务决策。</p></div>';
    h+='<div class=rs locked><h2>四、人生Bug修复指南</h2>'+bs.map(function(x,i){return'<p>'+(i+1)+'. '+x[0]+'：'+x[1]+'</p>'}).join('')+'</div>';
    h+='<div class=rs locked><h2>五、专属幸运密码</h2><div class=lucky-box>';
    h+='<div class=lucky-item><div class=num>'+pk(LC||[],r)+'</div><div class=label>幸运色</div></div>';
    h+='<div class=lucky-item><div class=num>'+pk(LN||[],r)+'</div><div class=label>幸运数字</div></div>';
    h+='<div class=lucky-item><div class=num>'+pk(LI||[],r)+'</div><div class=label>好运信物</div></div>';
    h+='</div></div>';
    h+='<div class=unlock-box><button class=btn onclick=unlock()>解锁完整版</button></div>';
    document.getElementById('modal').classList.remove('active');
    document.getElementById('landing').style.display='none';
    document.getElementById('reportPage').classList.add('active');
    document.getElementById('rContent').innerHTML=h;
    setTimeout(function(){
      var s=document.querySelectorAll('#rContent .rs');
      for(var i=2;i<s.length;i++){s[i].style.filter='blur(8px)';s[i].style.pointerEvents='none'}
    },100);
  }catch(e){alert(e.message)}
};
function unlock(){"""
html = html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
