$('#toggle_header').addClass('red')
if ($('#toggle_header').hasClass('red')) {
    $('#toggle_header').on("click", function() {
        $(this).toggleClass('green')})}
else if ($('#toggle_header').hasClass('green')) {
    $('#toggle_header').on("click", function() {
        $(this).toggleClass('red')})
}
