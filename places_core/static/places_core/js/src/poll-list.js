/*
 * poll-list.js
 * ============
 * 
 * Lista wszystkich ankiet utworzonych w ramach jednej lokalizacji.
 */

require.config({
    
    baseUrl: window.STATIC_URL,
    
    urlArgs: "bust=" + (new Date()).getTime(),
    
    waitSeconds: 200,
    
    paths: {
        jquery     : "includes/jquery/jquery",
        jpaginate  : "includes/jquery/jquery.paginate",
        bootstrap  : "includes/bootstrap/bootstrap",
        underscore : "includes/underscore/underscore",
        backbone   : "includes/backbone/backbone",
        paginator  : "includes/backbone/backbone.paginator",
        tagsinput  : "includes/jquery/jquery.tagsinput",
        bootbox    : "includes/bootstrap/bootbox",
        moment     : "includes/momentjs/moment",
        tour       : "includes/tour/bootstrap-tour"
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
            deps: ["bootstrap"],
            exports: "bootbox"
        },
        
        tagsinput: {
            deps: ["jquery"]
        },

        tour: {
            deps: ["jquery"]
        }
    }
});

require(['jquery',
         'js/modules/ui/ui',
         'js/modules/common',
         'js/modules/locations/follow',
         'js/modules/polls/poll-list/pollList',
         'js/modules/inviter/userinviter'],

function ($) {

    "use strict";

    $(document).trigger('load');
    
});