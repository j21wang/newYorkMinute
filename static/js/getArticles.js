$(document).ready(function(){
    $(".submit").click(function(){
        var topic = $(".topic").val();
        alert(topic);
        getArticleArray(topic);
    });
});

function getArticleArray(topic){

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
            });
        }
    });
    return articleArr;
}

function changeURL(){
    alert(articleArr);
}
