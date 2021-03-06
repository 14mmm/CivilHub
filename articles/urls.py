# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^contact/', views.TopLevelArticleView.as_view(article_slug='contact'), name='contact'),
    url(r'^cookies/', views.TopLevelArticleView.as_view(article_slug='cookies'), name='cookies'),
    url(r'^privacy/', views.TopLevelArticleView.as_view(article_slug='privacy'), name='privacy'),
    url(r'^about-us/', views.TopLevelArticleView.as_view(article_slug='about-us'), name='about-us'),
    url(r'^press/', views.TopLevelArticleView.as_view(article_slug='press', template_name='articles/press.html'), name='press'),
    url(r'^press-coverage/', views.TopLevelArticleView.as_view(article_slug='press-coverage', template_name='articles/press.html'), name='press-coverage'),
    url(r'^creed/', views.TopLevelArticleView.as_view(article_slug='creed', template_name='articles/creed.html'), name='creed'),
    url(r'^terms/', views.TopLevelArticleView.as_view(article_slug='terms'), name='terms'),
    url(r'^jobs/', views.TopLevelArticleView.as_view(article_slug='jobs'), name='jobs'),
    url(r'^features/', views.TopLevelArticleView.as_view(article_slug='features', template_name='articles/features.html'), name='features'),
    url(r'^team/', views.TopLevelArticleView.as_view(article_slug='team', template_name='articles/clear.html'), name='team'),
    url(r'^mission/', views.TopLevelArticleView.as_view(article_slug='mission', template_name='articles/mission.html'), name='mission'),
    url(r'^blog/(?P<slug>[\w-]+)/', views.BlogEntryView.as_view(), name='blog_entry'),
    url(r'^blog/', views.BlogListView.as_view(), name='blog'),
    #url(r'^support/(?P<slug>[\w-]+)/', views.SupportEntryView.as_view(), name='support_entry'),
    #url(r'^support/', views.SupportListView.as_view(), name='support'),
    url(r'^support/', views.TopLevelArticleView.as_view(article_slug='support', template_name='articles/support-list.html'), name='support'),
    url(r'^vector-map/', views.TopLevelArticleView.as_view(article_slug='vector-map', template_name='articles/vector-map.html'), name='vector-map'),
    url(r'^brief/', views.TopLevelArticleView.as_view(article_slug='brief', template_name='articles/brief.html'), name='brief'),
    url(r'^local-communities/', views.TopLevelArticleView.as_view(article_slug='local-communities', template_name='articles/brief.html'), name='brief'),
    url(r'^project-features/', views.TopLevelArticleView.as_view(article_slug='project-features', template_name='articles/brief.html'), name='project-features'),
    url(r'^idea-to-law/', views.TopLevelArticleView.as_view(article_slug='idea-to-law', template_name='articles/brief.html'), name='idea-to-law'),
    url(r'^idea-to-project/', views.TopLevelArticleView.as_view(article_slug='idea-to-project', template_name='articles/brief.html'), name='idea-to-project')
)
