$(document).ready(function(){
    $('.shopCartButton').click(function(){
        $.ajax({
            url: "/shopping_list/",
            type: "POST",
            data: {id:$(this).attr('id')},
            success:function() {
                        }
          })
    })
})