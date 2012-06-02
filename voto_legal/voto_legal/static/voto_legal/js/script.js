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
	});
})(jQuery);