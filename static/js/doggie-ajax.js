function saveLikes() {
    var rid;
    rid = $(this).attr("data-dogid");
    $.get('like/', {dog_id: rid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
}

