$(document).ready(function(){
    $('.determine').click(function(){
        //console.log($(this).attr('id'))
        $.ajax({
            url: "/payment/",
            type: "POST",
            success:function(){
                location.href = '/shopping_list';
            }
        })
    })
})