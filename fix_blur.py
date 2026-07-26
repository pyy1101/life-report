with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The exact current verifyCode line to replace
old_line = "document.querySelectorAll('.locked').forEach(function(el){el.classList.replace('locked','unlocked')});document.getElementById('shareBar').style.display='';"

new_line = "document.querySelectorAll('#rContent .rs').forEach(function(el){el.style.filter='';el.style.pointerEvents='auto'});document.getElementById('shareBar').style.display='';"

if old_line in html:
    html = html.replace(old_line, new_line)
    print("replaced OK")
else:
    print("NOT FOUND - check exact string")
    # Show what we're looking for
    idx = html.find("document.querySelectorAll('.locked')")
    if idx > 0:
        end = html.index(';', html.index('shareBar', idx))
        actual = html[idx:end+1]
        print(f"Actual: {actual[:100]}...")
        html = html[:idx] + new_line + html[end+1:]
        print("replaced via position")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done")
