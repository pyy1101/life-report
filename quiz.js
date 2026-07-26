var _quizQ=[
{q:"收到聚会邀请，你的第一反应是？",a:[["太好了！正好想见见大家","E"],["又要社交…能不能不去","I"]]},
{q:"在新环境里，你通常？",a:[["主动跟陌生人搭话，很快混熟","E"],["先观察，等别人来找我","I"]]},
{q:"休息日你更想？",a:[["约朋友出去浪一天","E"],["一个人待着充充电","I"]]},
{q:"你更相信？",a:[["亲身经历和具体事实","S"],["直觉和第六感","N"]]},
{q:"看书或电影时，你更关注？",a:[["情节和人物细节","S"],["背后的主题和隐喻","N"]]},
{q:"朋友说你更偏向？",a:[["务实派，注重眼前的","S"],["梦想家，总在想未来的","N"]]},
{q:"朋友失恋找你哭，你第一反应？",a:[["帮ta分析问题出在哪","T"],["先陪着ta让ta哭完","F"]]},
{q:"做重大决定时？",a:[["列个利弊表，理性分析","T"],["听内心的声音，感觉对了就对了","F"]]},
{q:"同事方案有明显漏洞，你会？",a:[["直接指出问题所在","T"],["委婉提醒，怕伤ta自尊","F"]]},
{q:"你的房间书桌通常是？",a:[["收拾得整整齐齐","J"],["看似凌乱但我知道东西在哪","P"]]},
{q:"面对一个项目你习惯？",a:[["提前规划好每个节点","J"],["边做边调整，计划赶不上变化","P"]]},
{q:"旅行你更喜欢？",a:[["按攻略走，打卡不遗漏","J"],["走到哪算哪，意外才是旅行","P"]]},
];
var _typeNames={INTJ:"建筑师 - 独立战略家",INTP:"逻辑学家 - 深度思考者",ENTJ:"指挥官 - 天生领导者",ENTP:"辩论家 - 创意探索者",INFJ:"提倡者 - 安静的理想主义者",INFP:"调停者 - 诗人与梦想家",ENFJ:"主人公 - 天生的导师",ENFP:"竞选者 - 热情社交家",ISTJ:"物流师 - 责任担当者",ISFJ:"守卫者 - 默默奉献者",ESTJ:"总经理 - 高效执行者",ESFJ:"执政官 - 关怀照顾者",ISTP:"鉴赏家 - 冷静实干家",ISFP:"探险家 - 艺术灵魂",ESTP:"企业家 - 冒险实干派",ESFP:"表演者 - 活力四射"};
var _typeDesc={INTJ:"你有清晰的远景规划能力，独立、果断、不会被情绪左右。你的座右铭是：凡事预则立。",INTP:"你对世界充满好奇，热爱探索真理和逻辑。你不喜欢被规则束缚，享受独自在思维迷宫中穿行。",ENTJ:"你拥有天然的号召力和组织才能。在混乱中你最冷静，在迷茫中你最清醒。",ENTP:"你的大脑像一台永不停机的创意引擎。你喜欢挑战常规，享受辩论的乐趣但并非为了赢。",INFJ:"你有一种超越常人的共情力和洞察力。你能看见别人看不见的东西，包括别人内心的光与暗。",INFP:"你内心住着一个浪漫的理想主义者。你对美和意义有某种偏执的追求，温柔但绝不软弱。",ENFJ:"你天生是人群中的灯塔。你不需要刻意的说教，你的存在本身就让人想要变得更好。",ENFP:"你是行走的太阳，温暖、好奇、热爱一切新鲜事物。你有把无聊变有趣的能力。",ISTJ:"你沉稳可靠，说到做到。你不是最闪耀的那个人，但你是最靠谱的那个。",ISFJ:"你默默守护着身边的人，不求回报。你的温柔不是软肋，是你最坚硬的铠甲。",ESTJ:"你尊重秩序和效率，是天生的管理者和执行者。别跟你比靠谱，你会赢。",ESFJ:"你天生懂得照顾他人，是朋友圈里的妈妈和爸爸。你的责任感让你成为团队的稳定器。",ISTP:"你不喜欢说太多话，但你的行动永远比语言更有力。你对机械和动手能力有与生俱来的天赋。",ISFP:"你是一个行走的艺术品。你对美有某种直觉，对自由有某种执念。你不需要被定义。",ESTP:"你喜欢刺激和挑战，是天生的冒险家。你对风险有着野兽般的嗅觉和对机会有着猎豹般的速度。",ESFP:"你是派对的生命和聚光灯下的宠儿。你让每个人感到快乐，包括你自己。"};

function answerQuiz(step,val){
  window._quizAnswers[step]=val;window._quizStep++;
  var box=document.getElementById("quizBox");var n=window._quizStep;
  if(n<12){
    var q=_quizQ[n];
    box.innerHTML="<p style='color:rgba(200,190,170,.4);font-size:12px;margin-bottom:4px'>第 "+(n+1)+" / 12 题</p>"+
      "<p style='text-align:left;color:rgba(200,190,170,.85);margin-bottom:14px;font-size:16px;line-height:1.6'>"+q.q+"</p>"+
      q.a.map(function(x){return"<button onclick=\"answerQuiz("+n+",'"+x[1]+"')\" style='width:100%;padding:14px 16px;margin-bottom:8px;background:rgba(255,255,255,.04);border:1px solid rgba(180,140,220,.15);border-radius:10px;color:rgba(220,210,190,.8);cursor:pointer;text-align:left;font-family:inherit;font-size:15px;transition:all .2s' onmouseover=\"this.style.background='rgba(180,140,220,.15)';this.style.borderColor='rgba(180,140,220,.4)'\" onmouseout=\"this.style.background='rgba(255,255,255,.04)';this.style.borderColor='rgba(180,140,220,.15)'\">"+x[0]+"</button>"}).join("")+
      "<div style='display:flex;gap:3px;margin-top:14px'>"+Array(12).fill(0).map(function(_,i){return"<div style='flex:1;height:3px;border-radius:2px;background:"+(i<n?"#b48cdc":"rgba(255,255,255,.08)")+"'></div>"}).join("")+"</div>";
  }else{
    var a=window._quizAnswers;
    var EI=(a.filter(function(x){return x==="E"}).length>=2?"E":"I");
    var SN=(a.filter(function(x){return x==="S"}).length>=2?"S":"N");
    var TF=(a.filter(function(x){return x==="T"}).length>=2?"T":"F");
    var JP=(a.filter(function(x){return x==="J"}).length>=2?"J":"P");
    var mbti=EI+SN+TF+JP;
    _type="personality_quiz";window._quizMbti=mbti;window._quizMbtiName=_typeNames[mbti]||"";
    document.getElementById("modal").classList.remove("active");
    generate();
  }
}
