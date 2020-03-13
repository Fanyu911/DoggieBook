function saveLikes() {
    var did;
    rid = $(this).attr("data-dogid");
    $.get('like/', {dog_id: did}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
}
