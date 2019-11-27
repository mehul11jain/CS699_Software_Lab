$('#clear').click(function(){
    $('#q').empty()
});
$('textarea').click(function(){
    $('.hidden').toggleClass('show')
});

$('button[name ="suggest"]').click(function(){
//console.log($('span[name ="replacePosition"]#'+$(this).val().split(",")[1]))
    //console.log($(this).val());
    val=$(this).val().split(",")[0];
    if (val=="@#!@#")
    {
    val = prompt("Please write the value");
    console.log(val)
    if (val == '' || val == null ) {
    //document.getElementById(i).innerHTML = val;
    alert("enter some string");
    return ;
    }
    }

    $('span[name ="replacePosition"]#'+$(this).val().split(",")[1]).replaceWith( val);

    //console.log("namaste2");

$('div[name="errorCollapse"]')[$(this).val().split(",")[1]].style.display="none";
$('div[name="errorDiv"]')[$(this).val().split(",")[1]].style.display="none";
});

$('span[name ="replacePosition"]').bind("DOMSubtreeModified",function(){
    data=$('span[name ="replacePosition"]#'+$(this).attr('id')).text();
    //console.log(x)
    $('span[name ="replacePosition"]#'+$(this).attr('id')).replaceWith(data);
  });
// $('div[contenteditable=true]').keydown(function(e) {
//     // trap the return key being pressed
//     if (e.keyCode == 13) {
//     // insert 2 br tags (if only one br tag is inserted the cursor won't go to the second line)
//     document.execCommand('insertHTML', false, '<br><br>');
//     // prevent the default behaviour of return key pressed
//     return false;
//     }
// });
// $('span[name ="replacePosition"]').on('keypress',function(){
//     alert("asdas");
//     $('span[name ="replacePosition"]#'+$(this).attr('id').replaceWith("val");
//     console.log("ASasA");
//     document.write("asasD");
// });



$('span[name ="replacePosition"]').add('div[name="errorCollapse"]').click(function(){

    list=$('div[name="errorDiv"]')
    $.each(list, function (i) {
        if (list[i].style.display=="block")
            {
                list[i].style.display="none";
                $('div[name="errorCollapse"]')[i].style.display="block";
                return false;
            }
         });
         console.log("visibilty");
    //console.log(list[$(this).attr('id')].style.display);
    list[$(this).attr('id')].style.display="block";
    $('div[name="errorCollapse"]')[$(this).attr('id')].style.display="none";
    
});



document.getElementById("req").onsubmit = function(e){
    e.preventDefault();
    console.log("asohdaosdhaoshdoahsi");
    console.log ($('span[name ="replacePosition"]')[0]);
    list=$('span[name ="replacePosition"]')
    $.each(list, function (i) {
    console.log( list[i].innerText+"Sdasdas");
    list[i].replaceWith( list[i].innerText);
        });


    // list2=$("div#q").find("div")    
    // $.each(list2, function (i) {
    //     list2[i].replaceWith( list2[i].innerText+"\n");
    //         });
    


    var el = document.createElement("input");
    el.type = "hidden";
    el.name="hid";
    el.value = document.getElementById("q").innerText;
    document.getElementById("req").appendChild(el);
    //return false;
    document.getElementById("req").submit();
}



/*var value=document.getElementById("q").value
document.getElementByID("q").innerHTML=value;*/
/*$(document).on('submit','#req',function(p){
    p.preventDefault();
    $.ajax({
        type:'POST',
        url:'/index',
        data:{
            query:$('#q').val(),
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val()
        },
        success:function(){

        } 
    })
})*/
/*$(document).ready(function(){
    var flg = 0;
    $('span').click(function(){
            flg++;
            if(flg == 1){
                $this_html = jQuery('.wrapper').html();
                $("#platypusDropDown").append("<li>"+$this_html+"</li>");
            }
            $("#platypusDropDown").slideToggle();
    });
 });*/