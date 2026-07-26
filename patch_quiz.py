import re

with open('index.html','r',encoding='utf-8') as f:
    html = f.read()

with open('quiz.js','r',encoding='utf-8') as f:
    quiz = f.read()

# 1. Replace the personality case in start() with quiz modal
# Find the personality case and replace it
old_start = "else if(t==='personality'){h='🎭 隐藏人格解码';b='发现真正的你';box.innerHTML=`<h2>${h}</h2>${bdayHTML('fYear','fMonth','fDay')}<select id=\"fGender\"><option value=\"\">性别</option><option value=\"female\">女性</option><option value=\"male\">男性</option></select><select id=\"fMbti\"><option value=\"\">MBTI (选填)</option></select><button class=\"submit-btn\" onclick=\"generate()\">✨ ${b}</button><div class=\"modal-close\" onclick=\"document.getElementById('modal').classList.remove('active')\">先想想</div>`;popBday('fYear','fMonth','fDay');popMBTI('fMbti')}"

new_start = """else if(t==='personality'){
  h='🎭 隐藏人格解码 - 免费MBTI测试';
  box.innerHTML='<h2>'+h+'</h2><p style="color:rgba(200,190,170,.5);font-size:14px;margin-bottom:16px">4道题快速测出你的MBTI类型</p><div id="quizBox"><p style="text-align:left;color:rgba(200,190,170,.7);margin-bottom:8px">1. 周末你更喜欢怎么过？</p><button onclick="answerQuiz(0,\\'E\\')" style="width:100%;padding:10px;margin-bottom:6px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;cursor:pointer;text-align:left;font-family:inherit;font-size:14px">和朋友出去玩，人多才热闹</button><button onclick="answerQuiz(0,\\'I\\')" style="width:100%;padding:10px;margin-bottom:6px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;cursor:pointer;text-align:left;font-family:inherit;font-size:14px">在家待着，一个人或跟最亲近的人</button></div><div class="modal-close" onclick="document.getElementById(\\'modal\\').classList.remove(\\'active\\')">先想想</div>';
  window._quizAnswers=[];window._quizStep=0;
}"""

if old_start in html:
    html = html.replace(old_start, new_start)
    print("Start replaced OK")
else:
    print("Start not found, trying regex...")
    # Fallback: try to find with regex
    pattern = r"else if\(t==='personality'\)\{[^}]*popMBTI\('fMbti'\)\}"
    match = re.search(pattern, html)
    if match:
        html = html[:match.start()] + new_start + html[match.end():]
        print("Start regex replaced OK")
    else:
        print("Start regex also failed")

# 2. Insert quiz.js before generate function
marker = "// ============ GENERATE ============"
html = html.replace(marker, quiz + "\n" + marker)
print("Quiz functions inserted")

# 3. Handle personality_quiz in generate
old_type = "}else if(tp==='personality'){"
new_type = "}else if(tp==='personality'||tp==='personality_quiz'){mb=window._quizMbti||'未知';mbName=window._quizMbtiName||'';"
if old_type in html:
    html = html.replace(old_type, new_type)
    print("Type replaced")
else:
    print("Type not found")

# 4. Auto-unlock for free quiz
old_unlock = "html+='<div class=\"unlock-box\" id=\"unlockBox\">"
new_unlock = "var isFree=(tp==='personality_quiz');html+='<div class=\"unlock-box\" id=\"unlockBox\" style=\"'+(isFree?'display:none':'')+'\">\""
if old_unlock in html:
    html = html.replace(old_unlock, new_unlock)
    print("Unlock box replaced")
else:
    print("Unlock box not found")

# Auto-unlock free reports
old_show = "document.getElementById('landing').style.display='none';document.getElementById('reportPage').classList.add('active');"
new_show = "document.getElementById('landing').style.display='none';document.getElementById('reportPage').classList.add('active');if(isFree){setTimeout(function(){document.querySelectorAll('.locked').forEach(function(el){el.classList.replace('locked','unlocked')})},100);}"
if old_show in html:
    html = html.replace(old_show, new_show)
    print("Auto-unlock added")
else:
    print("Auto-unlock not found")

# 5. Fix quiz answer function to handle step and val correctly
# The quiz.js sends step but our internal counter uses _quizStep
# Let's fix: answerQuiz receives step (0,1,2,3) and val (E,I,S,N,T,F,J,P)
old_quiz = "function answerQuiz(step,val){window._quizAnswers[step]=val;window._quizStep++;"
new_quiz = "function answerQuiz(step,val){window._quizAnswers[step]=val;window._quizStep=step+1;"
html = html.replace(old_quiz, new_quiz)

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print(f"Done: {len(html)} bytes")
