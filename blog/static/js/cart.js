$(document).ready(function(){
$('.shopCartButton').click(function(){
    console.log($('.shopCartButton').attr('id'))
   $.ajax({
        url: "/shopping_list",
        type: "POST",
        data: "{$('button').attr('id') }"
          })
    })
})