var indF = function() { 
	$.ajax({
    type: "GET",
    url: '/meetings/ajax/get_index_page',
    data: {
    },
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(result){
        Indhtml(result);
    }
});
};


var Indhtml = function(result){

    var a = document.getElementById('vuy')
    console.log(result)
    a.innerHTML = ''
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
