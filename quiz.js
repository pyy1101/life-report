var _quizQ=[
{q:"收到聚会邀请，第一反应？",a:[["太好了正好想出门","E"],["又要社交…能不能不去","I"]]},
{q:"在新环境里你通常？",a:[["主动跟陌生人搭话","E"],["先观察等别人找我","I"]]},
{q:"休息日更想？",a:[["约朋友出去浪一天","E"],["一个人待着充充电","I"]]},
{q:"电话铃响了你的反应？",a:[["秒接，喜欢即时沟通","E"],["犹豫一下再接或等对方挂","I"]]},
{q:"哪种状态让你更舒服？",a:[["周围有很多人很热闹","E"],["安静独处或只跟亲密的人","I"]]},
{q:"被夸奖时你通常？",a:[["开心，喜欢被关注","E"],["有点尴尬不知道怎么回应","I"]]},
{q:"周五晚上你更想？",a:[["出去参加各种活动","E"],["窝在沙发看剧看书","I"]]},
{q:"跟人聊天后你感觉？",a:[["精力充沛还想聊","E"],["被掏空需要独处恢复","I"]]},
{q:"你更相信？",a:[["亲身经历和具体事实","S"],["直觉和第六感","S"]]},
{q:"看书或电影更关注？",a:[["情节和人物细节","S"],["背后的主题和隐喻","N"]]},
{q:"朋友说你更偏向？",a:[["务实派注重眼前","S"],["梦想家总想未来","N"]]},
{q:"学习新东西时喜欢？",a:[["看具体步骤和案例","S"],["先理解理论和大框架","N"]]},
{q:"哪种说法更打动你？",a:[["眼见为实数据说话","S"],["万物皆有联系","N"]]},
{q:"你更欣赏哪种人？",a:[["靠谱踏实说到做到","S"],["有远见敢想敢做","N"]]},
{q:"工作方式你更像？",a:[["一步步按流程执行","S"],["跳过步骤直奔结果","N"]]},
{q:"讲故事时你更注重？",a:[["时间线清晰细节准确","S"],["氛围感和整体画面","N"]]},
{q:"朋友失恋找你哭，第一反应？",a:[["帮ta分析问题出在哪","T"],["先陪着让ta哭完","F"]]},
{q:"做重大决定时？",a:[["列个利弊表理性分析","T"],["听内心声音感觉对了就对了","F"]]},
{q:"同事方案有明显漏洞？",a:[["直接指出问题在哪","T"],["委婉提醒怕伤自尊","F"]]},
{q:"你更尊重哪种人？",a:[["逻辑缜密就事论事","T"],["善良温暖顾及他人","F"]]},
{q:"争论中你更看重？",a:[["谁说得对有理有据","T"],["谁受伤了需不需要安抚","F"]]},
{q:"做错事被批评时？",a:[["先想怎么解决","T"],["先觉得有点难过","F"]]},
{q:"看电影哭了你觉得？",a:[["剧情逻辑通不通","T"],["角色太让人心疼了","F"]]},
{q:"帮助别人时你更倾向于？",a:[["给实际建议和方案","T"],["给情感支持和陪伴","F"]]},
{q:"你的房间书桌通常是？",a:[["收拾得整整齐齐","J"],["看似凌乱但我知道在哪","P"]]},
{q:"面对一个项目你习惯？",a:[["提前规划每个节点","J"],["边做边调整计划赶不上变化","P"]]},
{q:"旅行你更喜欢？",a:[["按攻略走打卡不遗漏","J"],["走到哪算哪意外才是旅行","P"]]},
{q:"截止日期快到了你？",a:[["早就提前完成了","J"],["在最后一刻高效爆发","P"]]},
{q:"日常生活你更像？",a:[["有固定作息和习惯","J"],["每天随机应变","P"]]},
{q:"购物清单你通常？",a:[["写好清单按计划买","J"],["看到了想买就买","P"]]},
{q:"周末计划被打乱你会？",a:[["有点不爽不喜欢变动","J"],["无所谓反正本来也没定","P"]]},
{q:"对于规则的态度？",a:[["规则让人安心应该遵守","J"],["规则是死的没必要太认真","P"]]},
];

var _typeNames={INTJ:"建筑师 - 独立战略家",INTP:"逻辑学家 - 深度思考者",ENTJ:"指挥官 - 天生领导者",ENTP:"辩论家 - 创意探索者",INFJ:"提倡者 - 安静的理想主义者",INFP:"调停者 - 诗人与梦想家",ENFJ:"主人公 - 天生的导师",ENFP:"竞选者 - 热情社交家",ISTJ:"物流师 - 责任担当者",ISFJ:"守卫者 - 默默奉献者",ESTJ:"总经理 - 高效执行者",ESFJ:"执政官 - 关怀照顾者",ISTP:"鉴赏家 - 冷静实干家",ISFP:"探险家 - 艺术灵魂",ESTP:"企业家 - 冒险实干派",ESFP:"表演者 - 活力四射"};

var _typeDesc={INTJ:"你有清晰的远景规划能力，独立果断不会被情绪左右。你的座右铭是凡事预则立。",INTP:"你对世界充满好奇热爱探索真理和逻辑，不喜欢被规则束缚，在思维迷宫中穿行最自在。",ENTJ:"你拥有天然的号召力和组织才能。在混乱中你最冷静，在迷茫中你最清醒。",ENTP:"你的大脑像一台永不停机的创意引擎，喜欢挑战常规享受辩论的乐趣但并非为了赢。",INFJ:"你有超越常人的共情力和洞察力，能看见别人看不见的东西包括内心的光与暗。",INFP:"你内心住着一个浪漫的理想主义者，对美和意义有偏执的追求，温柔但绝不软弱。",ENFJ:"你是人群中的灯塔，不需要刻意的说教，存在本身就让人想要变得更好。",ENFP:"你是行走的太阳，温暖好奇热爱一切新鲜事物，有把无聊变有趣的能力。",ISTJ:"你沉稳可靠说到做到，不是最闪耀的那个但绝对是最靠谱的那个。",ISFJ:"你默默守护着身边的人不求回报，你的温柔不是软肋而是最坚硬的铠甲。",ESTJ:"你尊重秩序和效率是天生的管理者和执行者，别跟你比靠谱你会赢。",ESFJ:"你天生懂得照顾他人，是朋友圈里的稳定器和所有人的后盾。",ISTP:"你不喜欢说太多话但行动永远比语言更有力，对动手能力有与生俱来的天赋。",ISFP:"你是一个行走的艺术品，对美有直觉对自由有执念，不需要被任何人定义。",ESTP:"你喜欢刺激和挑战是天生的冒险家，对风险有野兽般的嗅觉对机会有猎豹般的速度。",ESFP:"你是派对的生命聚光灯下的宠儿，你让每个人都感到快乐包括你自己。"};

function answerQuiz(step,val){
  window._quizAnswers[step]=val;window._quizStep++;
  var box=document.getElementById("quizBox");var n=window._quizStep,total=32;
  if(n<total){
    var q=_quizQ[n],pct=Math.round(n/total*100);
    box.innerHTML="<p style='color:rgba(200,190,170,.4);font-size:12px;margin-bottom:4px'>第 "+(n+1)+" / "+total+" 题（"+pct+"%）</p>"+
      "<p style='text-align:left;color:rgba(200,190,170,.85);margin-bottom:14px;font-size:16px;line-height:1.6'>"+q.q+"</p>"+
      q.a.map(function(x){return"<button onclick=\"answerQuiz("+n+",'"+x[1]+"')\" style='width:100%;padding:14px 16px;margin-bottom:8px;background:rgba(255,255,255,.04);border:1px solid rgba(180,140,220,.15);border-radius:10px;color:rgba(220,210,190,.8);cursor:pointer;text-align:left;font-family:inherit;font-size:15px;transition:all .2s' onmouseover=\"this.style.background='rgba(180,140,220,.15)';this.style.borderColor='rgba(180,140,220,.4)'\" onmouseout=\"this.style.background='rgba(255,255,255,.04)';this.style.borderColor='rgba(180,140,220,.15)'\">"+x[0]+"</button>"}).join("")+
      "<div style='display:flex;gap:2px;margin-top:14px'>"+Array(total).fill(0).map(function(_,i){return"<div style='flex:1;height:3px;border-radius:2px;background:"+(i<n?"#b48cdc":"rgba(255,255,255,.08)")+"'></div>"}).join("")+"</div>";
  }else{
    var a=window._quizAnswers;
    function score(dim,letter){var cnt=0,start={"E":0,"I":0,"S":8,"N":8,"T":16,"F":16,"J":24,"P":24}[letter];for(var i=start;i<start+8;i++)if(a[i]===letter)cnt++;return cnt}
    var eScore=score(0,"E"),iScore=score(0,"I"),sScore=score(1,"S"),nScore=score(1,"N"),tScore=score(2,"T"),fScore=score(2,"F"),jScore=score(3,"J"),pScore=score(3,"P");
    var EI=eScore>iScore?"E":"I",SN=sScore>nScore?"S":"N",TF=tScore>fScore?"T":"F",JP=jScore>pScore?"J":"P";
    var mbti=EI+SN+TF+JP;
    // Match percentage: average consistency across 4 dimensions
    var eiMatch=Math.round((eScore>iScore?eScore:iScore)/8*100);
    var snMatch=Math.round((sScore>nScore?sScore:nScore)/8*100);
    var tfMatch=Math.round((tScore>fScore?tScore:fScore)/8*100);
    var jpMatch=Math.round((jScore>pScore?jScore:pScore)/8*100);
    var match=Math.round((eiMatch+snMatch+tfMatch+jpMatch)/4);
    _type="personality_quiz";window._quizMbti=mbti;window._quizMbtiName=_typeNames[mbti]||"";window._quizMatch=match;
    document.getElementById("modal").classList.remove("active");generate();
  }
}
