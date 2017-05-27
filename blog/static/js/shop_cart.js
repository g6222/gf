$(document).ready(function(){
    $('button').click(function(){
        var quantity=0;
        var group=$(this).attr('class')
        var id = $(this).attr('id')
        if(group == 'plus'){
            quantity = +1
        }else if(group == 'reduce'){
            quantity = -1
        }
        $.ajax({
            url: "/shop_cart/",
            type: "POST",
            data: {quantity:quantity,
                id:$(this).attr('id')},
            success:function(counts_count) {
                if(counts_count.number == 0){
                    $('#'+id).parents('tr').remove()
                }
                if(counts_count.total_count==0){
                    location.href = '/shopping_list';
                }
                if(counts_count.free == 0){
                    $('#subtotals'+id).text(counts_count.total.toFixed(1)+'元')
                }
                else {
                    $('#subtotals'+id).text(counts_count.free+'元'+'(原价:'+counts_count.total.toFixed(1)+'元)')
                }
                $('#'+id).next().text(counts_count.number);
                $("number").text(counts_count.total_count);
                $('p').text('总计:'+counts_count.totals.toFixed(2)+'元');
            }
        })
    })
})