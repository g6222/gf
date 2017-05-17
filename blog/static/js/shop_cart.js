$(document).ready(function(){
    $('button').click(function(){
        console.log($(this).attr('class'))
        console.log($(this).attr('id'))
        $.ajax({
            url: "/shop_cart/",
            type: "POST",
            data: {class:$(this).attr('class'),
                id:$(this).attr('id')},
            success:function(sum_count) {
                $("number1").text(sum_count);
            }
        })
        if(button = plus){
            sum_count+1
        }else{
            sum_count-1
        }
    })
})