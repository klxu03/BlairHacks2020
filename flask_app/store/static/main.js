$(".deleteItem").click(function() {
    console.log('clicked');
    console.log($(this).closest("tr"))
    $(this).closest("tr").remove();
});