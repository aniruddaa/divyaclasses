$(document).ready(function() {
    // Animate sections on scroll
    $(window).on('scroll', function() {
        $('.animated-section').each(function() {
            var sectionTop = $(this).offset().top;
            var scroll = $(window).scrollTop() + $(window).height();
            if (scroll > sectionTop + 100) {
                $(this).addClass('visible');
            }
        });
    });

    // Enquiry form AJAX submission (connected to Django backend)
    $('#enquiry-form').on('submit', function(e) {
        e.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: '/enquiry/',
            type: 'POST',
            data: formData,
            success: function(response) {
                if (response.success) {
                    $('#enquiry-success').show();
                    $('#enquiry-form').trigger('reset');
                } else {
                    alert('Submission failed. Please try again.');
                }
            },
            error: function() {
                alert('Submission failed. Please try again.');
            }
        });
    });
});
