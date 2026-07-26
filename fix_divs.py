with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The lucky section has incorrect div nesting. Fix the string.
# Current: ...'</div></div></div><p style=...> * '+pk(LA||[],xr)+'</p></div>';
# Need: ...'</div></div></div></div><p style=...> * '+pk(LA||[],xr)+'</p></div>';

old = "'</div></div></div><p style=\"text-align:center;margin-top:12px;color:rgba(200,190,170,.5)\"> * '+pk(LA||[],xr)+'</p></div>';"
new = "'</div></div></div></div><p style=\"text-align:center;margin-top:12px;color:rgba(200,190,170,.5)\">🔮 '+pk(LA||[],xr)+'</p>';"

if old in html:
    html = html.replace(old, new)
    print("fixed div count")
else:
    print("not found, searching...")
    # Search for the pattern
    idx = html.find("'</div></div></div>")
    if idx > 0:
        end = html.find("';", idx) + 2
        current = html[idx:end]
        print(f"Current: {current[:100]}...")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("done:", len(html))
