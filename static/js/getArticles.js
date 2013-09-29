$(document).ready(function(){
    $("#thing").click(function(){
        var topic = $(".topic").val();
        var callback = function (err, articles) {
           changeURL(articles);
        };
        getArticleArray(topic, callback);
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
                var url = "?article=" + value.web_url;
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
