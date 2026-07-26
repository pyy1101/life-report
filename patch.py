with open('index.html','r',encoding='utf-8') as f: html=f.read()

# 1. Add auto-unlock on page load
old='// ============ STARS ============'
new='''// ============ AUTO-UNLOCK FROM PAYMENT ============
(function(){
  var p=new URLSearchParams(window.location.search);
  if(p.get('paid')==='1'){
    setTimeout(function(){
      var els=document.querySelectorAll('.locked');
      if(els.length>0){
        els.forEach(function(x){x.classList.replace('locked','unlocked')});
        var box=document.getElementById('unlockBox');
        if(box) box.innerHTML='<p style="color:rgba(200,190,170,.5);font-size:14px">Pay success - full report unlocked</p>';
      }
    },500);
  }
})();

// ============ STARS ============'''
html=html.replace(old,new)

# 2. Replace unlock function to redirect to MBD
# Find the unlock function and replace it entirely
import re
old_unlock = r'function unlock\(\)\{[^}]*\}'
new_unlock = '''function unlock(){
  if(!_r)return;
  var mbd='https://mbd.pub/YOUR_PRODUCT_LINK';
  window.location.href=mbd+'?callback='+encodeURIComponent(location.origin+location.pathname+'?paid=1');
}'''
html = re.sub(old_unlock, new_unlock, html, flags=re.DOTALL)

with open('index.html','w',encoding='utf-8') as f: f.write(html)
print('OK:',len(html))
