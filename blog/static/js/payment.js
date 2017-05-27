$(document).ready(function(){
    $('.payment').click(function(){
        $.ajax({
            url: "/shopping_list/",
            type: "POST",
            data: {id:$(this).attr('id')},
            success:function(total_count) {
                $("number").text(total_count);
            }
        })
    })
})