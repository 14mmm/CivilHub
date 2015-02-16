/*
 * news-create.js
 * ==============
 * 
 * Tworzenie/edycja wpisów w sekcji News lokalizacji.
 */

require.config({
    
    baseUrl: window.STATIC_URL,
    
    urlArgs: "bust=" + (new Date()).getTime(),
    
    waitSeconds: 200,
    
    paths: {
        jquery     : "includes/jquery/jquery",
        jpaginate  : "includes/jquery/jquery.paginate",
        jqueryui   : "includes/jquery-ui/jquery-ui",
        bootstrap  : "includes/bootstrap/bootstrap",
        bootbox    : "includes/bootstrap/bootbox",
        underscore : "includes/underscore/underscore",
        backbone   : "includes/backbone/backbone",
        tagsinput  : "includes/jquery/jquery.tagsinput",
        redactor   : "includes/redactor/redactor",
        dropzone   : "includes/dropzone/dropzone",
        tour       : "includes/tour/bootstrap-tour",
        leaflet    : "includes/leaflet/leaflet"
    },
    
    shim: {
        
        jpaginate: {
            deps: ["jquery"]
        },
        
        underscore: {
            deps: ["jquery"],
            exports: "_"
        },
        
        backbone: {
            deps: ["underscore"],
            exports: "Backbone"
        },
        
        bootstrap: {
            deps: ["jquery"]
        },
        
        bootbox: {
            deps: ["bootstrap"]
        },
        
        jqueryui: {
            deps: ["jquery"]
        },
        
        tagsinput: {
            deps: ["jqueryui"]
        }
    }
});

require(['jquery',
         'js/modules/common',
         'js/modules/editor/plugins/uploader',
         'js/modules/locations/follow',
         'js/modules/inviter/userinviter',
         'js/modules/blog/news-form'],

function ($) {
    
    "use strict";
    
    $(document).trigger('load');
    
});