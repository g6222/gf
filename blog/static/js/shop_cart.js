$(document).ready(function(){
    $('button').click(function(){
        var quantity=$(this).attr('data-count');
        var $this=$(this)
        var id = $(this).attr('data-id')
        $.ajax({
            url: "/shop_cart/",
            type: "POST",
            data: {quantity:quantity,
                id:$(this).attr('data-id')
                },
            success:function(counts_count) {
                if (counts_count.number == 0){
                    $this.parents('tr').remove()
                }
                $this.parent().find("span").text(counts_count.number);
                $("number").text(counts_count.total_count);
                $('p').text('总计:' + counts_count.totals.toFixed(1) + '元');

                if (counts_count.total_count == 0) {
                    location.href = '/shopping_list';
                }
                if (counts_count.free == 0){
                    $('#subtotals' + id).text(counts_count.total.toFixed(1) + '元')
                }
                else if(counts_count.moeny != 0){
                    $('#subtotals' + id).text(counts_count.free.toFixed(1) + '元' +' '+ '原价:' + counts_count.total.toFixed(1) + '元')
                }
            }
        })
    })
})