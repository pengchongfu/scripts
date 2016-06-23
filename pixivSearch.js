#!/usr/bin/node

var request=require('request');
var keyword=process.argv[2];
var number=process.argv[3];

function login(){
    console.log('标签为 '+keyword+' 收藏数大于等于 '+number+' 的链接');
    return new Promise(function(resolve,reject){
        request=request.defaults({jar:true});
        request({
            url:'https://www.pixiv.net/login.php',
            method:'POST',
            form:{
                mode:'login',
                return_to:'/',
                pixiv_id:'',
                pass:'',
                skip:'1',
            },
            followAllRedirects:true,
        },function(err,res,body){
            resolve(request);
        });
    });
}

function getPages(request){
    return new Promise(function(resolve,reject){
        request({
            url:encodeURI('http://www.pixiv.net/search.php?word='+keyword),
            method:"GET",
        },function(err,res,body){
            require("jsdom").env(body, function(err, window) {
                var $ = require("jquery")(window);
                var pages = $('span.count-badge').text();
                pages = Math.ceil((+pages.slice(0,-1))/20);
                console.log('总页数为 '+pages);
                request.pages=pages;
                resolve(request);
            });
        });
    });
}

function getUrl(request){
    for(var p=1;p<=request.pages;p++){
        request({
            method:'GET',
            url:encodeURI('http://www.pixiv.net/search.php?word='+keyword+'&p='+p),
        },function(err,res,body){
            require("jsdom").env(body, function(err, window) {
                var $ = require("jquery")(window);
                var li = $('li.image-item');
                for(var l=0;l<li.length;l++){
                    var bookmark_a=$(li[l]).find('a.bookmark-count._ui-tooltip');
                    var num = +$(bookmark_a).text();
                    if(num>=number){
                        console.log('http://www.pixiv.net'+$($(li[l]).children('a')[0]).attr('href'));
                    }
                }
            });
        });
    }
}

login().then(getPages).then(getUrl);