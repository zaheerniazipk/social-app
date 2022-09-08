// AJAX jQuery Code
$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});

// JS Toggle model Event for new Post
$(document).on("click", ".js-toggle-modal", function (event) {
    event.preventDefault()
    $(".js-modal").toggleClass("hidden")
});


// AJAX jQuery code for Creating new post dynamically
$(document).on('click', '.js-submit', function (event) {
    event.preventDefault();
    console.log('submit working!');

    const $textarea = $('.js-post-text');
    const text = $('.js-post-text').val().trim();
    const $btn = $(this);

    if (!text) {
        return false
    }
    else {
        // When text is submitted, model will be closed
        $(".js-modal").addClass("hidden");
        // Return nox Text in the text Box for next attempt to submit
        $('.js-post-text').val('')

        // send to database
        $btn.prop('disabled', true).text('posting!')
        // jQuery ajax() Method
        $.ajax({
            type: 'POST',
            // Specifies the URL to send the request to
            url: $textarea.data('post-url'),
            // Specifies data to be sent to the server
            data: {
                text: text,
            },

            // A function to be run when the request succeeds
            success: (dataHtml) => {
                $(".js-modal").addClass("hidden");
                $('#posts-container').prepend(dataHtml);
                $btn.prop('disabled', false).text('New Post');
                $('.js-post-text').val();

            },

            // A function to run if the request fails.
            error: (error) => {
                console.warn(error);
                $btn.prop('disabled', false).text('Error');
            }

        });


    }
});