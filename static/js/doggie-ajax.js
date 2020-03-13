function saveLikes() {
    var did;
    did = $(this).attr("data-dogid");
    $.get('like/', {dog_id: did}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
}

