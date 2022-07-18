function refresh() {

}

function collect_args() {
    
}

$(document).ready(function () {
    $('#run-button').click(function () { 
        $('#load-page').toggleClass('invisible', 'visible');
        $.ajax({
            type: "POST",
            url: "/",
            data: "data",
            dataType: "dataType"
        });
    });
    $('#reset-button').click(function () { 
        refresh()
    });
});