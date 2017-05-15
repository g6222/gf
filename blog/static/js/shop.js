 var $p = $("navigationbar").click();
        $p.toggle(function(){
            $p.css("background-color:black","color:white");
        },function(){
            $p.css("background-color: #373737","color: #bebdc1");
        })