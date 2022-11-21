
$("#btn_query").click(function() {
    let terminal_type = $('#terminal_type option:selected').val();
    let dot_key = $('#dot_key').val();
    let start_time = $('#start_time').val();
    let end_time = $('#end_time').val();
    let versions = [];
    $("input:checkbox:checked").each(function(){
        versions.push(this.id);
    });
    let data = {
        'terminal_type' : terminal_type,
        'dot_key'       : dot_key,
        'start_time'    : start_time,
        'end_time'      : end_time,
        'versions'      : versions
    };

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
            $('#terminal_type').val(terminal_type);
            $("#start_time").val(start_time);
            $("#end_time").val(end_time);
            $('#dot_key').val(dot_key);
            for (const version of versions) {
                $('#' + version.replace('.', '\\.')).prop("checked", true);
            }
        }
    });
});
