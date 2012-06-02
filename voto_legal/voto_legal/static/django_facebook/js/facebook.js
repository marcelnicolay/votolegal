/*
Maps locale from django to Facebook
scraped like this from FB:
curl https://www.facebook.com/translations/FacebookLocales.xml -s | grep "<representation>" FacebookLocales.xml | sed 's@<\([^<>][^<>]*\)>\([^<>]*\)</\1>@\2@g'
* */
fbLocales = ["af_ZA", "ar_AR", "az_AZ", "be_BY", "bg_BG", "bn_IN", "bs_BA",
    "ca_ES", "cs_CZ", "cy_GB", "da_DK", "de_DE", "el_GR", "en_GB", "en_PI",
    "en_UD", "en_US", "eo_EO", "es_ES", "es_LA", "et_EE", "eu_ES", "fa_IR",
    "fb_LT", "fi_FI", "fo_FO", "fr_CA", "fr_FR", "fy_NL", "ga_IE", "gl_ES",
    "he_IL", "hi_IN", "hr_HR", "hu_HU", "hy_AM", "id_ID", "is_IS", "it_IT",
    "ja_JP", "ka_GE", "ko_KR", "ku_TR", "la_VA", "lt_LT", "lv_LV", "mk_MK",
    "ml_IN", "ms_MY", "nb_NO", "ne_NP", "nl_NL", "nn_NO", "pa_IN", "pl_PL",
    "ps_AF", "pt_BR", "pt_PT", "ro_RO", "ru_RU", "sk_SK", "sl_SI", "sq_AL",
    "sr_RS", "sv_SE", "sw_KE", "ta_IN", "te_IN", "th_TH", "tl_PH", "tr_TR",
    "uk_UA", "vi_VN", "zh_CN", "zh_HK", "zh_TW"];

fbLocaleMapping = {};
for (var i=0; i<fbLocales.length;i++){
    var k = fbLocales[i].split("_")[0];
    fbLocaleMapping[k] = fbLocales[i];
    fbLocaleMapping[fbLocales[i]] = fbLocales[i];
}

facebookClass = function() { this.initialize.apply(this, arguments); };
facebookClass.prototype = {
    initialize: function (appId) {
        this.appId = appId;
        
        var scope = this;
        function javascriptLoaded() {
            scope.javascriptLoaded.call(scope);
        }

    },
    
    getDefaultScope : function() {
        var defaultScope;
       if (typeof(facebookDefaultScope) != 'undefined') {
            defaultScope = facebookDefaultScope;
       } else {
           defaultScope = ['email', 'user_about_me', 'user_birthday', 'user_website'];
       }
       return defaultScope;
    },
    
    connect: function (formElement, requiredPerms) {
        requiredPerms = requiredPerms || this.getDefaultScope();
        var scope = this;
        FB.login(function(response) {
            if (response.authResponse) {
                console.log('Welcome!  Fetching your information.... ');
                FB.api('/me', function(response) {
                    console.log(response);
                });
                $.ajax({
                    url: formElement.attr('action'),
                    success: function (data, status){
                        console.log(data);
                        console.log(status);
                    }
                });
            } else {
                console.log('User cancelled login or did not fully authorize.');
            }
        },
        {scope: requiredPerms.join(',')}
        );
    },
    
    
    load: function () {
        var facebookScript = document.getElementById('facebook_js');
        if (!facebookScript) {
            var e = document.createElement('script');
            e.type = 'text/javascript';
            // gets the locale, tries to get the facebook synonym and
            // the checks if it is a valid FB locale
            var fbLocale = "en_US";
            if(typeof(locale) != 'undefined') {
                if (locale in fbLocaleMapping) {
                    fbLocale = fbLocaleMapping[locale];
                }
            }
            var fbLocation = '//connect.facebook.net/' + fbLocale + '/all.js';
            e.src = document.location.protocol + fbLocation;
            e.async = true;
            e.id = 'facebook_js';
            document.getElementById('fb-root').appendChild(e);
        }
    }
};
