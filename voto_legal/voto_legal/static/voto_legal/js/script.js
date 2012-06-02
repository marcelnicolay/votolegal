(function($) {
    $(document).ready(function () {

        var fbConnect = {
            $: {
                forms: $('.facebook-connect')
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
        };
        fbConnect.init();
        function politico_search(term, cb_response) {
            $.getJSON("/politicos/buscar", {q: term.term}, function(response) {
                return cb_response(response.politicos);
            });
        }
        $('#politico-search-box').autocomplete({
            source: politico_search,
            minLength: 3,
            select: function(evn, ui) {
                $('#politico-page').val(ui.item.id);
            }
        });
    });
})(jQuery);
