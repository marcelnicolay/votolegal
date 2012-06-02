(function($) {
	$(document).ready(function () {

		var fbConnect = {
			$: {
				forms: $('.facebook-connect')
			},
			init: function (){
				this.$.forms.each(function (e){
					var $this = $(this),
						$button = $this.find('.entrar');

					$button.on({
						'click': function (e){
							e.preventDefault();
							F.connect($this);
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
