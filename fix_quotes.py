with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# Problem: xh+='...' uses single quotes. style='display:none' also uses single quotes.
# Fix: change locked content from xh+='...class=locked...' to use escaped quotes
# BUT: this is inside an onclick="..." attribute in HTML.
# The simplest reliable fix: DON'T put complex code in onclick.
# Instead: use xh+="..." (double quotes) for locked sections

# Find the locked sections in the inline onclick
# Section 3 locked paragraphs
old = "xh+='<p class=locked>'"+xad2[0]+"'：'"+xad2[1]+"'</p><p class=locked>避坑提醒：'"+(xmo||1)+"'月前后注意财务决策。</p></div>';"
new = 'xh+="<p style=\\'display:none\\'>"+xad2[0]+"："+xad2[1]+"</p><p style=\\'display:none\\'>避坑提醒："+(xmo||1)+"月前后注意财务决策。</p></div>";'
html = html.replace(old, new)

# Section 4 (bug fixes)
old2 = "xh+='<div class=rs locked><h2>四、人生Bug修复指南</h2>'"+xbs.map(function(x,i){return '<p>'+(i+1)+'. '+x[0]+'：'+x[1]+'</p>'}).join('')+"'</div>';"
new2 = 'xh+="<div class=rs style=\\'display:none\\'><h2>四、人生Bug修复指南</h2>"+xbs.map(function(x,i){return "<p>"+(i+1)+". "+x[0]+"："+x[1]+"</p>"}).join("")+"</div>";'
html = html.replace(old2, new2)

# Section 5 (lucky code) - this one was already added separately
# Find the unlock box line
old3 = "xh+='<div class=unlock-box>"
new3 = 'xh+="<div class=rs style=\\'display:none\\'><h2>五、专属幸运密码</h2></div>";xh+=\'<div class=unlock-box>'
html = html.replace(old3, new3)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
