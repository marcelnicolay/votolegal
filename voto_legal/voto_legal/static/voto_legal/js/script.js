(function($) {
    $(document).ready(function () {

        var fbConnect = {
                $: {
                    forms: $('form.facebook-connect')
                },
                init: function (){
                    this.$.forms.each(function (e){
                        var $this = $(this),
                            $form = $this,
                            $button = $this.find('.entrar');
                        $button.on({
                            'click': function (e){
                                e.preventDefault();
                                var $this = $(this);
                                $this.html('Esperando Resposta...');
                                FB.login(function(response) {
                                    if (response.authResponse) {
                                        FB.api('/me', function(response) {
                                            console.log(response);
                                        });
                                        $.ajax({
                                            url: $form.attr('action'),
                                            success: function (data, status){
                                                $this.html('Registrado!');
                                                setTimeout(function() {
                                                   $this.html('Entrar');
                                                }, 2000);
                                                window.location = $form.find('input[name="redirect"]').val();
                                            },
                                            error: function (){
                                                $this.html('Erro!');
                                            }
                                        });
                                    } else {
                                        $this.html('Permissão negada');
                                    }
                                },
                                {scope: 'email,user_about_me,user_birthday,publish_stream,publish_actions,offline_access'}
                                );
                                return;
                            }
                        });
                    });
                }
            },
            search = {
                $: {
                    forms: $('form.search')
                },
                ajaxurl: function (term){
                    return ['/ajax/politicos/', term].join('');
                },
                url: function (slug){
                    return ['/politico/', slug].join('');
                },
                search: function (data, cb){
                    $.getJSON(search.ajaxurl(data.term), function(response) {
                        return cb(response.politicos);
                    });
                },
                init: function (){
                    this.$.forms.each(function (e){
                        var $form = $(this),
                            $send = $form.find('.send'),
                            $input = $form.find('.field');
                            $slug = $form.find('.slug'),
                            change = function(e, ui) {
                                e.preventDefault();
                                $slug.val(ui.item.value);
                                $input.val(ui.item.label);
                                window.location = search.url(ui.item.value);
                                return;
                            };

                        $input.autocomplete({
                            source: search.search,
                            minLength: 2,
                            select: change,
                            change: change,
                            focus: function(e, ui) {
                                e.preventDefault();
                                $slug.val(ui.item.value);
                                $input.val(ui.item.label);
                                return;
                            }
                        }).trigger('focus');
                    });
                }
            };
        fbConnect.init();
        search.init();
    });
})(jQuery);
