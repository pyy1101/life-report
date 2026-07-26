with open('test.html','r',encoding='utf-8') as f: base=f.read()
s_start = base.index('<script>') + 8
html_part = base[:s_start]

with open('templates_clean.js','r',encoding='utf-8') as f: tmpl=f.read()

script = '\n// === TEMPLATES ===\n' + tmpl + '''
var NUMS=Array.from({length:100},function(_,i){return i+1});
var LC=COLORS,LN=NUMS,LI=ITEMS,LA=ACTIONS,MN=MONTHS;
var mbtiNames={"INTJ":"建筑师","INTP":"逻辑学家","ENTJ":"指挥官","ENTP":"辩论家","INFJ":"提倡者","INFP":"调停者","ENFJ":"主人公","ENFP":"竞选者","ISTJ":"物流师","ISFJ":"守卫者","ESTJ":"总经理","ESFJ":"执政官","ISTP":"鉴赏家","ISFP":"探险家","ESTP":"企业家","ESFP":"表演者"};

function sd(s){var x=0;for(var i=0;i<s.length;i++)x=(x*31+s.charCodeAt(i))&0x7fffffff;return function(){x=(x*1103515245+12345)&0x7fffffff;return x/0x7fffffff}}
function pk(a,r){return a[Math.floor(r()*a.length)]}
function pks(a,n,r){var u=[],res=[];while(res.length<n){var x=pk(a,r);if(u.indexOf(x[0])<0){u.push(x[0]);res.push(x)}}return res}

(function(){
  var y=document.getElementById("fYear"),m=document.getElementById("fMonth"),d=document.getElementById("fDay"),mb=document.getElementById("fMbti");
  var ty=new Date().getFullYear();
  for(var i=ty;i>=1960;i--){var o=document.createElement("option");o.value=i;o.textContent=i+"年";y.appendChild(o)}
  for(var i=1;i<=12;i++){var o=document.createElement("option");o.value=i;o.textContent=i+"月";m.appendChild(o)}
  for(var i=1;i<=31;i++){var o=document.createElement("option");o.value=i;o.textContent=i+"日";d.appendChild(o)}
  Object.keys(mbtiNames).forEach(function(k){var o=document.createElement("option");o.value=k;o.textContent=k+" - "+mbtiNames[k];mb.appendChild(o)})
})();

(function(){
  var c=document.getElementById("stars");
  if(c){for(var i=0;i<100;i++){var s=document.createElement("div");s.style.cssText="position:absolute;background:white;border-radius:50%;left:"+Math.random()*100+"%;top:"+Math.random()*100+"%;width:"+(Math.random()*2+1)+"px;height:"+(Math.random()*2+1)+"px;opacity:"+(Math.random()*.3+.1)+";animation:tw"+(Math.random()*3+2)+"s infinite alternate";c.appendChild(s)}
  var st=document.createElement("style");st.textContent="@keyframes tw{0%{opacity:.1;transform:scale(1)}100%{opacity:.6;transform:scale(1.8)}}";document.head.appendChild(st)}
})();

function genReport(){
  var yr=parseInt(document.getElementById("fYear").value),mo=parseInt(document.getElementById("fMonth").value),da=document.getElementById("fDay").value;
  if(!yr||!mo||!da){alert("请选择完整的年月日");return}
  var gd=document.getElementById("fGender").value;
  var mbEl=document.getElementById("fMbti"),mb="未知",mbName="";
  if(mbEl&&mbEl.value){var raw=mbEl.value.split(" - ");mb=raw[0];mbName=raw[1]||""}
  var r=sd((yr*10000+mo*100+parseInt(da)).toString());
  function fg(arr){if(!gd)return arr;var p=arr.filter(function(x){return x.g===gd}),n=arr.filter(function(x){return!x.g||x.g==="u"});return p.concat(p).concat(n)}
  var PL=fg(PAST_LIVES),GL=fg(TALENTS);
  var pl=pk(PL,r),ts=pks(GL,3,r),ad=pk(ADVENTURES,r),ad2=pk(ADVENTURES,r);if(ad2[0]===ad[0])ad2=pk(ADVENTURES,r);
  var bs=pks(BUGS,3,r);
  var h="";
  h+='<p style="color:#888;margin-bottom:4px">'+yr+'.'+mo+'.'+da+' | MBTI '+mb+(mbName?" - "+mbName:"")+'</p>';
  h+='<div class="rs"><h2>一、前世身份：'+pl.t+'</h2><p>'+pl.d+'</p></div>';
  h+='<div class="rs"><h2>二、今生隐藏天赋</h2>'+ts.map(function(x,i){return'<p><b>'+(i+1)+'. '+x[0]+'：</b>'+x[1]+'</p>'}).join("")+'</div>';
  h+='<div class="rs"><h2>三、2026年奇遇剧本</h2>';
  h+='<p>✅ <b>'+ad[0]+'：</b>'+ad[1]+'</p>';
  h+='<p class="locked">✅ <b>'+ad2[0]+'：</b>'+ad2[1]+'</p>';
  h+='<p class="locked">✅ <b>避坑提醒：</b>'+(mo||1)+'月前后注意财务决策，别冲动消费或投资。</p></div>';
  h+='<div class="rs locked"><h2>四、人生Bug修复指南</h2>'+bs.map(function(x,i){return'<p><b>'+(i+1)+'. '+x[0]+'：</b>'+x[1]+'</p>'}).join("")+'</div>';
  h+='<div class="rs locked"><h2>五、专属幸运密码</h2><div class="lucky-box">';
  h+='<div class="lucky-item"><div class="num">'+pk(LC,r)+'</div><div class="label">幸运色</div></div>';
  h+='<div class="lucky-item"><div class="num">'+pk(LN,r)+'</div><div class="label">幸运数字</div></div>';
  h+='<div class="lucky-item"><div class="num">'+pk(LI,r)+'</div><div class="label">好运信物</div></div>';
  h+='</div><p style="text-align:center;margin-top:12px;color:rgba(200,190,170,.5)">✨ '+pk(LA,r)+'</p></div>';
  h+='<div class="unlock-box"><h3>🔮 解锁完整报告</h3><p>全部隐藏天赋 · 完整奇遇 · Bug修复 · 幸运密码</p><button class="btn" onclick="unlock()">✨ 解锁完整版</button></div>';
  document.getElementById("landing").style.display="none";
  document.getElementById("reportPage").classList.add("active");
  document.getElementById("rContent").innerHTML=h;
  window.scrollTo(0,0);
}

function unlock(){
  document.querySelectorAll(".locked").forEach(function(el){el.classList.replace("locked","unlocked")});
  document.querySelector(".unlock-box").innerHTML='<p style="color:#aaa">✨ 完整报告已解锁</p>';
}

document.getElementById("genBtn").onclick=genReport;
document.getElementById("shareBtn").onclick=function(){
  var txt=document.getElementById("rContent").innerText;
  var pl=txt.match(/前世身份：(.+)/);
  var tl=txt.match(/1. (.+)/);
  var card=document.createElement("div");card.style.cssText="position:fixed;inset:0;z-index:9999;background:rgba(5,5,10,.97);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px";card.onclick=function(){this.remove()};
  card.innerHTML='<div style="max-width:420px;background:linear-gradient(180deg,#0c0a20,#1a1040 35%,#0e0c2a 65%,#0a0a1a);border-radius:24px;overflow:hidden;text-align:center"><div style="padding:36px 24px"><div style="width:56px;height:56px;border-radius:50%;background:radial-gradient(circle at 35%35%,#f5e6d3,#d4b896 40%,#8b6c9a 72%,transparent 74%);margin:0 auto 16px"></div><div style="font-size:10px;color:rgba(200,190,170,.35);letter-spacing:3px;margin-bottom:12px">探寻命运密码</div><div style="font-size:24px;font-weight:900;background:linear-gradient(180deg,#f0e0cc,#d4b896,#8b6c9a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:16px">隐藏人生剧本</div>'+(pl?'<div style="background:rgba(30,20,50,.5);border-radius:12px;padding:14px;margin:12px 0;text-align:left"><div style="font-size:11px;color:rgba(200,190,170,.35);margin-bottom:4px">前世身份</div><div style="font-size:14px;color:#ddd">'+pl[1]+'</div></div>':'')+(tl?'<div style="background:rgba(30,20,50,.5);border-radius:12px;padding:14px;text-align:left"><div style="font-size:11px;color:rgba(200,190,170,.35);margin-bottom:4px">隐藏天赋</div><div style="font-size:14px;color:#ddd">'+tl[1]+'</div></div>':'')+'</div><div style="background:rgba(10,5,20,.6);padding:16px;border-top:1px solid rgba(180,140,220,.08);font-size:11px;color:#b48cdc">life.devshells.com</div></div><div style="margin-top:12px;color:#888;font-size:12px">长按截图保存</div>';
  document.body.appendChild(card);
};
document.getElementById("downloadBtn").onclick=function(){
  var el=document.getElementById("rContent");if(!el)return;
  var w=window.open("","_blank","width=500,height=700");
  w.document.write("<!DOCTYPE html><html><head><meta charset=UTF-8><style>body{background:#0a0a0f;color:#e0e0d0;font-family:sans-serif;padding:20px}</style></head><body>"+el.innerHTML+"</body></html>");
  w.document.close();
};
'''

new_html = html_part + script + '\n</script></body></html>'
with open('index_rebuild.html','w',encoding='utf-8') as f: f.write(new_html)
print('Built:', len(new_html), 'bytes')
