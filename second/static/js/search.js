var searchdata = function(){

    var x = document.getElementById("searchterm").value;
    $.ajax({
    type: "GET",
    url: '/meetings/ajax/get_meeting_details',
    data: {
        'x' : x
    },
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(result){
        console.log(x);
        mysearchindex(result, x)
        }
    });
};


var mysearchindex = function(details, x){

    var index = elasticlunr(function () {
        this.addField('title');
        this.addField('body');
        this.setRef('id');
    });

    console.log(details.idi)
    for(var i = 0, size = details.idi.length; i < size; i++){
        var doc = {
            "id": details.idi[i],
            "title": details.titl[i],
            "body": details.bod[i]
        }
        console.log(doc)
        index.addDoc(doc);
    }
    //console.log(index)
    searchresult = index.search(x)
    req = []
    for(var i =0, size = searchresult.length; i < size; i++)
    {
        ou = searchresult[i]['ref'];
        console.log(ou);
        req.push(ou)
    }
    $.ajax({
    type: "GET",
    url: '/meetings/ajax/get_search_results',
    data: {
        'req' : req.toString(),
        'x' : x
    },
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(result){  
        console.log(result);
        //window.location.href = "search";
        displaysearchresult(result)
        }
    });
};


var displaysearchresult = function(result){

console.log(result)
var a = document.getElementById('vuy')
    console.log(result)
    if(result.namee.length == 0){
        a.innerHTML = '<h4 align = "center">Could not find any results</h4>'
    }
    else{
        a.innerHTML = ''
    }
    for(var i = 0, size = result.namee.length;i < size; i++)
    {
        a.innerHTML = a.innerHTML +  '<div class="col-md-4">'+
        '<figure id ="' + result.idi[i] + '" class="effect-marley">' +
           '<img src="/static/img/8.jpg" alt="" class="img-responsive" />' +
           '<figcaption>'+ 
                '<h4>'+ result.namee[i]  + '</h4>' +
                '<p>' + result.timm[i] + '</p>' + 
            '</figcaption>' + 
        '</figure>'+ 
        '</div>'
    }
    for(var i = 0, size = result.namee.length;i < size; i++){
        document.getElementById(result.idi[i]).onclick = function() {
            var ikk = this.id;
            location.href = ikk;}
    }

}


var clearField = function(result){
    var a = document.getElementById("searchterm").value = "";
}
/*var example = function(){
    
    var index = elasticlunr(function () {
    this.addField('title');
    this.addField('body');
    this.setRef('id');
});

    var doc1 = {
    "id": 1,
    "title": "Oracle released its latest database Oracle 12g",
    "body": "Yestaday Oracle has released its new database Oracle 12g, this would make more money for this company and lead to a nice profit report of annual year."
}

    var doc2 = {
    "id": 2,
    "title": "Oracle released its profit report of 2015",
    "body": "As expected, Oracle released its profit report of 2015, during the good sales of database and hardware, Oracle's profit of 2015 reached 12.5 Billion."
}

    index.addDoc(doc1);
    index.addDoc(doc2);

    console.log(index.search("oracle"));
}*/
