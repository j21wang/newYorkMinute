$(document).ready(function(){

    $(document).keypress(function(e){
        console.log(e);
        if(e.which == 13){
            $(".next.button").click();
        }
    });

    $(".topicForm").submit(function(e){
        e.preventDefault();
        $(".next.button").click();
    });

    $(".next.button").click(function(){
        var topic = $(".topic").val().replace(' ','+');
        console.log(topic);
        if(topic == '') {
            console.log("enters");
            topicArr = ['America','alcohol','kardashian','weight','cancer','Obama','money','joke','dead','football'];
            randomNum = Math.floor(Math.random()*9);
            console.log(randomNum);
            topic = topicArr[randomNum];
            console.log(topic);
        }
        var callback = function (err, articles) {
            console.log("HI");
           changeURL(articles);
        };
        getArticleArray(topic, callback);
    });

    $('.timeForm').submit(function(){
        $('.submit.button').click();
    });
});

function getArticleArray (topic, callback) {

    var articleArr;
    $.ajax({
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback : 'svc_search_v2_articlesearch',
        url:'http://api.nytimes.com/svc/search/v2/articlesearch.jsonp?q=' + topic + '&sort=newest&api-key=979d61de2e40719bc34dd2fe25f7da0b:6:67932469',
        success: function(resp){
            articleArr = resp.response.docs;
            $.each(articleArr,function(key,value){
                var url =  value.web_url;
                articleArr[key] = url;
                //console.log(articleArr[key]);
            });
            callback(null, articleArr);
        },
        error: function (err) { callback(err); }
    });
}

function changeURL(articleArr){
    console.log(articleArr);
    var actionString = "/findArticles?";
    
    $.each(articleArr,function(key,value){

        if(key==0){
            console.log(key);
            actionString += "url_" + key + "=" + value;
        } else {
            actionString += "&url_" + key + "=" + value;
        }
    });
    console.log(actionString);
    $("form").prop("action",actionString);
    
    return actionString;
}
