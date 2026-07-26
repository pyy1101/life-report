with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the life case in start()
start = html.index("if(t==='life')")
# Find end of this case (popMBTI call)
end = html.index('popMBTI', start) + 20
chunk = html[start:end]

# Count backticks
ticks = [i for i, c in enumerate(chunk) if c == '`']
print(f"Backtick count in life case: {len(ticks)}")
for i, pos in enumerate(ticks):
    ctx_start = max(0, pos - 15)
    ctx_end = min(len(chunk), pos + 15)
    ctx = chunk[ctx_start:ctx_end].replace('\n', '\\n')
    print(f"  [{i}] at offset {pos}: {repr(ctx)}")

# Also check the ENTIRE chunk between if and popMBTI for the start function
all_start = html.index("function start(t){")
all_end = html.index("document.getElementById('modal').classList.add('active');", all_start)
all_chunk = html[all_start:all_end]
all_ticks = [i for i, c in enumerate(all_chunk) if c == '`']
print(f"\nBacktick count in entire start() function: {len(all_ticks)}")

# Check if all backticks are properly paired
script = html[html.index('<script>')+8:html.index('</script>')]
open_ticks = 0
in_template = False
for i, c in enumerate(script):
    if c == '`':
        # Check if this backtick is inside a string (single/double quoted)
        # This is a rough check
        open_ticks += 1

print(f"Total backticks in script: {open_ticks}")
print(f"Paired: {'YES' if open_ticks % 2 == 0 else 'NO - UNPAIRED!'}")
