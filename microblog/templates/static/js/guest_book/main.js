function create_entry() {
    $.ajax({
        url : "create-entry/", // the endpoint
        type : "POST", // http method
        data : { author : $('#id_author').val(),
                 text : $('#id_text').val(),
                 csrfmiddlewaretoken : $('#token').text()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#id_author').val(''); // remove the value from the input
            $('#id_text').val('');
            console.log(json);
            $("#entries-list").prepend(json.html);
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
