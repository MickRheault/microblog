function create_entry() {
    $.ajax({
        url : "create-entry/", // the endpoint
        type : "POST", // http method
        data : { author : $('#id_author').val(),
                 text : $('#id_text').val(),
                 csrfmiddlewaretoken : $('#token').text(),
                 captcha_0 : $('#id_captcha_0').val(),
                 captcha_1 : $('#id_captcha_1').val()
                }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#id_author').val(''); // remove the value from the input
            $('#id_text').val('');
            console.log(json);
            $('#id_captcha_0').val(json.cptch_key);
            $('#id_captcha_1').val('');
            $('img.captcha').attr('src',json.cptch_image);

            if (json.html.length > 2) {
                $("#entries-list").prepend(json.html);
            }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        }
    });
}

$(document).ready(function () {
    $('#guest-form').on('submit', function (event) {
        event.preventDefault();
        create_entry()
    });
    $('#entries-list').on('click', '.list-group-item', function () {
        $(this).find('#item-desc').toggleClass('hide-me');
        $(this).find('#item-text').toggleClass('hide-me');
    });
});
