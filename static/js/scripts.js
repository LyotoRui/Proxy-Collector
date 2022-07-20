$(document).ready(function () {
    $('#run-button').click(function () {
        $('#load-page').toggleClass('invisible', '');
        let data = collect_data()
        $('.check').prop('checked', false)
        $('.button').css('background-color', '#f8f9fa')
        $.ajax({
            type: "POST",
            contentType: "application/json;charset=utf-8",
            url: "/",
            data: JSON.stringify({ data }),
            dataType: "json",
        }).done(function (response) {
            $('#load-page').addClass('invisible');
            $('.check').prop('checked', false);
            let json = JSON.stringify(response)
            let blob = new Blob([json]);
            let link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = `proxies ${Date.now()}.json`;
            link.click();
        });


    });

    function collect_data() {
        let countries = [];
        let types = [];
        let anon = [];
        let format = [];
        $.each($('input[prompt=country]:checked'), function () {
            countries.push($(this).val())
        });
        $.each($('input[prompt=protocol]:checked'), function () {
            types.push($(this).val())
        });
        $.each($('input[prompt=anonymity]:checked'), function () {
            anon.push($(this).val())
        });
        $.each($('input[prompt=format]:checked'), function () {
            format.push($(this).val())
        });
        let data = {
            'countries': countries,
            'types': types,
            'anon': anon,
            'format': format
        };
        return data
    };

    $('.button').click(function () {
        if ($(`#${$(this).val()}`).is(':checked')) {
            $(`#${$(this).val()}`).prop('checked', false);
            $(this).css('background-color', '#f8f9fa')
        } else {
            $(`#${$(this).val()}`).prop('checked', true);
            $(this).css('background-color', '#5eba7d')
        }
    });

    $('#reset-button').click(function () {
        $('.check').prop('checked', false)
        $('.button').css('background-color', '#f8f9fa')
    });

});