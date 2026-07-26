with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# Replace showReport with version that reads form
old = 'window.showReport=function(){document.getElementById("modal").classList.remove("active");document.getElementById("landing").style.display="none";document.getElementById("reportPage").classList.add("active");document.getElementById("rContent").innerHTML="<h1>WORKING!</h1><p>Report page is showing</p>";window.scrollTo(0,0)};'

new = '''window.showReport=function(){
var yrEl=document.getElementById("fYear"),moEl=document.getElementById("fMonth"),daEl=document.getElementById("fDay");
var gdEl=document.getElementById("fGender"),mbEl=document.getElementById("fMbti");
alert("fYear:"+(yrEl?"found value="+yrEl.value:"NULL")+" fMonth:"+(moEl?"value="+moEl.value:"NULL")+" fDay:"+(daEl?"value="+daEl.value:"NULL"));
var yr=yrEl?parseInt(yrEl.value):2000,mo=moEl?parseInt(moEl.value):6,da=daEl?daEl.value:"15";
if(!yr||!mo||!da){alert("no date values, using defaults");yr=2000;mo=6;da="15"}
var gd=gdEl?gdEl.value:"",mb="unknown",mbName="";
if(mbEl&&mbEl.value){var raw=mbEl.value.split(" - ");mb=raw[0];mbName=raw[1]||""}
var r=sd((yr*10000+mo*100+parseInt(da)).toString());
function fg(arr){if(!gd)return arr;var p=arr.filter(function(x){return x.g===gd}),n=arr.filter(function(x){return!x.g||x.g==="u"});return p.concat(p).concat(n)}
var PL=fg(P),GL=fg(G);
var pl=pk(PL,r),ts=pks(GL,3,r),ad=pk(A,r),ad2=pk(A,r);if(ad2[0]===ad[0])ad2=pk(A,r);
var bs=pks(B,3,r);
var h="";
h+="<p style='color:#888;margin-bottom:4px'>"+yr+"."+mo+"."+da+" | MBTI "+mb+(mbName?" - "+mbName:"")+"</p>";
h+="<div class=rs><h2>一、前世身份："+pl.t+"</h2><p>"+pl.d+"</p></div>";
h+="<div class=rs><h2>二、今生隐藏天赋</h2>"+ts.map(function(x,i){return"<p><b>"+(i+1)+". "+x[0]+"：</b>"+x[1]+"</p>"}).join("")+"</div>";
h+="<div class=rs><h2>三、2026年奇遇剧本</h2>";
h+="<p> * <b>"+ad[0]+"：</b>"+ad[1]+"</p>";
h+="<p class=locked> * <b>"+ad2[0]+"：</b>"+ad2[1]+"</p>";
h+="<p class=locked> * <b>避坑提醒：</b>"+(mo||1)+"月前后注意财务决策。</p></div>";
h+="<div class=\\"rs locked\\"><h2>四、人生Bug修复指南</h2>"+bs.map(function(x,i){return"<p><b>"+(i+1)+". "+x[0]+"：</b>"+x[1]+"</p>"}).join("")+"</div>";
h+="<div class=\\"rs locked\\"><h2>五、专属幸运密码</h2><div class=lucky-box>";
h+="<div class=lucky-item><div class=num>"+pk(LC,r)+"</div><div class=label>幸运色</div></div>";
h+="<div class=lucky-item><div class=num>"+pk(LN,r)+"</div><div class=label>幸运数字</div></div>";
h+="<div class=lucky-item><div class=num>"+pk(LI,r)+"</div><div class=label>好运信物</div></div>";
h+="</div><p style='text-align:center;margin-top:12px;color:rgba(200,190,170,.5)'> * "+pk(LA,r)+"</p></div>";
h+="<div class=unlock-box><h3> * 解锁完整报告</h3><p>全部隐藏天赋 · 完整奇遇 · Bug修复 · 幸运密码</p><button class=btn onclick=unlock()> * 解锁完整版</button></div>";
document.getElementById("modal").classList.remove("active");
document.getElementById("landing").style.display="none";
document.getElementById("reportPage").classList.add("active");
document.getElementById("rContent").innerHTML=h;
window.scrollTo(0,0);
};'''

html = html.replace(old, new)
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
