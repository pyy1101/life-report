function answerQuiz(step,val){
  window._quizAnswers[step]=val;
  window._quizStep++;
  var box=document.getElementById("quizBox");
  var questions=[
    {q:"2. 读一本书时，你更关注？",a:[["📖 具体情节和细节描写","S"],["🔮 背后的寓意和可能性","N"]]},
    {q:"3. 做决定时你更依赖？",a:[["🧠 逻辑分析和客观事实","T"],["💝 个人感受和他人处境","F"]]},
    {q:"4. 你更喜欢的生活方式？",a:[["📋 有计划有安排，按部就班","J"],["🌊 随性而为，享受意外惊喜","P"]]}
  ];
  if(window._quizStep<3){
    var q=questions[window._quizStep-1];
    box.innerHTML="<p style='text-align:left;color:rgba(200,190,170,.7);margin-bottom:8px'>"+q.q+"</p>"+
      "<button onclick=\"answerQuiz("+(window._quizStep)+",'"+q.a[0][1]+"')\" style='width:100%;padding:10px;margin-bottom:6px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;cursor:pointer;text-align:left;font-family:inherit;font-size:14px'>"+q.a[0][0]+"</button>"+
      "<button onclick=\"answerQuiz("+(window._quizStep)+",'"+q.a[1][1]+"')\" style='width:100%;padding:10px;margin-bottom:6px;background:rgba(255,255,255,.05);border:1px solid rgba(180,140,220,.2);border-radius:8px;color:white;cursor:pointer;text-align:left;font-family:inherit;font-size:14px'>"+q.a[1][0]+"</button>";
  }else{
    var ei=window._quizAnswers[0],sn=window._quizAnswers[1],tf=window._quizAnswers[2],jp=window._quizAnswers[3];
    var mbti=ei+sn+tf+jp;
    var names={INTJ:"建筑师",INTP:"逻辑学家",ENTJ:"指挥官",ENTP:"辩论家",INFJ:"提倡者",INFP:"调停者",ENFJ:"主人公",ENFP:"竞选者",ISTJ:"物流师",ISFJ:"守卫者",ESTJ:"总经理",ESFJ:"执政官",ISTP:"鉴赏家",ISFP:"探险家",ESTP:"企业家",ESFP:"表演者"};
    _type="personality_quiz";window._quizMbti=mbti;window._quizMbtiName=names[mbti]||"";
    document.getElementById("modal").classList.remove("active");
    generate();
  }
}
