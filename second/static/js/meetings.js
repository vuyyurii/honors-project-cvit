var function1 = function(id, tti) {
    console.log(id) 
	$.ajax({
    type: "GET",
    url: '/meetings/ajax/get_meeting_images',
    data: {
    	'id':id
    },
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(result){
        console.log(result.output);
        function2(result, id, tti);
    }
});
};


var function2 = function(res, id, tti) {

    output = res.output
    name = res.nam
    images = res.imgs
    tti = tti.split(' ')
    tti = tti[3].split(':')
    console.log(tti)
    console.log("TEST")
    var a = document.getElementById('jjjss')
    a.innerHTML = ''
    if("NoImage" in output){
        a.innerHTML = '<div> <h4 align = "center">No Images were taken during meeting</h4></div>'
    }
    else{
    for(var i = 0, size = images.length; i < size ; i++){
        var temp = ''
        for(var j = 1, si = output[images[i]].length; j < si; j++){
            temp = temp + output[images[i]][j] + ', '
        }
        if(temp.length == 0){temp = 'None'}
        tsri = '/static/' + name + '/images_boxes/' + images[i];
        saa = output[images[i]][0]
        tto = saa.split(' ')
        tto = tto[3].split(':')
        if(tto.length != 3){
            tto = saa;
        }
        else{
            tres = Number(tto[0])*3600 + Number(tto[1])*60 + Number(tto[2])
            tres = tres - (Number(tti[0])*3600 + Number(tti[1])*60 + Number(tti[2]))
            //console.log(tres)
            tto[0] = Math.floor(tres/3600)
            tto[1] = Math.floor((tres%3600)/60)
            tto[2] = (tres%3600)%60
            //tto[0] = tto[0] - tti[0]
            //tto[1] = tto[1] - tti[1]
            //tto[2] = tto[2] - tti[2]
            tto = tto.join(':')
        }
        console.log(tto)
        a.innerHTML = a.innerHTML + '<div class="col-md-4"><div><figure id = "' + name + '" class="effect-marley">' +
                  '<img id = "show' + i + '" src = "' + tsri + '" alt="No Image available" class="img-responsive" />' + 
                  '<figcaption>' + 
                   '<p>Captured ' + tto + ' sec after the start of the meeting</p>' +
                    '</figcaption>'+
                    '</figure>'+
                    '<span class="caption"><h4>Recognized words:- ' + temp  + '</h4></span>' + 
                    '</div>' +
                    '</div>'
    }
    /*for(var i = 0, size = images.length; i < size ; i++)
    {
        var dd = images[i];
        console.log(dd, i, 'show' + i.toString())
        document.getElementById('show' + i.toString()).onclick = function(){
            this.src = '/static/'+ name + '/images/' + dd;
        }
    }*/
}
};