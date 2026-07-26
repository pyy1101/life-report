with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix unlock: just open payment in new tab
old = """function unlock(){
  var box=document.querySelector('.unlock-box');
  box.innerHTML='<div style="padding:20px"><p style="color:#ccc;margin-bottom:16px">微信扫码支付 4.9 元</p><div style="background:white;width:180px;height:180px;margin:0 auto 12px;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#999;font-size:12px">收款码</div><p style="color:#888;font-size:13px;margin-bottom:8px">支付后输入面包多订单号解锁</p><input id="unlockCode" placeholder="输入订单号" style="width:80%;padding:10px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;font-size:15px;text-align:center;margin-bottom:8px"><br><button class=btn onclick=verifyCode()>确认解锁</button></div>';
}"""

new = """function unlock(){
  window.open('https://mbd.pub/o/bread/YZaUlplxaA==','_blank');
}"""
html = html.replace(old, new)

# 2. Add payment input always below unlock button in genReport
old_btn = "h+='<div class=unlock-box><button class=unlock-btn onclick=unlock() style=\"font-size:18px;padding:16px 40px\">🔓 付费解锁完整报告</button></div>';"
new_btn = """h+='<div class=unlock-box><button class=unlock-btn onclick=unlock() style=\"font-size:18px;padding:16px 40px\">🔓 付费解锁 (4.9元)</button><div style=\"margin-top:16px;padding-top:16px;border-top:1px solid rgba(180,140,220,.1)\"><p style=\"color:#888;font-size:13px;margin-bottom:8px\">支付后输入面包多订单号</p><div style=\"display:flex;gap:8px;justify-content:center\"><input id=unlockCode placeholder=输入订单号 style=\"padding:10px 14px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;font-size:14px;width:200px;text-align:center\"><button class=btn onclick=verifyCode() style=\"padding:10px 20px;font-size:14px\">确认解锁</button></div></div></div>';"""
html = html.replace(old_btn, new_btn)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
