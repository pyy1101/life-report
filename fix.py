with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# Find the report building section and wrap it
old = 'var r=sd((yr*10000+mo*100+parseInt(da)).toString());'
new = '''try{
var r=sd((yr*10000+mo*100+parseInt(da)).toString());'''
html = html.replace(old, new)

# Find the end of the function and add catch
old2 = 'window.scrollTo(0,0);'
new2 = '''window.scrollTo(0,0);
}catch(e){alert("ERROR: "+e.message+" line:"+e.lineNumber);}'''
html = html.replace(old2, new2)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
