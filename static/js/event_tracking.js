
$("#btn_query").click(function() {
    let terminal_type = $('#terminal_type option:selected').val();
    let dot_key = $('#dot_key').val();
    let start_time = $('#start_time').val();
    let end_time = $('#end_time').val();
    let start_version = $('#start_version').val();
    let end_version = $('#end_version').val();
    //console.log(terminal_type);
    //console.log(start_time);
    //console.log(end_time);
    //console.log(start_version);
    //console.log(end_version);
    let data = {
        'terminal_type' : terminal_type,
        'dot_key'       : dot_key,
        'start_time'    : start_time,
        'end_time'      : end_time,
        'start_version' : start_version,
        'end_version'   : end_version
    };
    //console.log(data);
    //console.log(data);
    //console.log(image_vs_novel);
    //window.location.href = novel_path;

    $.ajax({
        url: '/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(result) {
            //console.log(result);
            document.open();
            document.write(result);
            document.close();
            $('#terminal_type').val(terminal_type)
            $("#start_time").val(start_time)
            $("#end_time").val(end_time)
            $("#start_version").val(start_version)
            $("#end_version").val(end_version)
        }
    });
});
