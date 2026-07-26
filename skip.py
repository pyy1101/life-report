with open("index.html","r",encoding="utf-8") as f: html=f.read()

# Find 'generating...' and replace everything from there to 'about to show report'
start=html.index('generating...')
end=html.index('about to show report')+len('about to show report')
old=html[start-15:end+2]  # get full context

new='''alert("showing report...");var yr=2000,mo=6,da=15,mb="INFP",mbName="调停者";'''

html=html[:start-15]+new+html[end+2:]

with open("index.html","w",encoding="utf-8") as f: f.write(html)
print("done")
