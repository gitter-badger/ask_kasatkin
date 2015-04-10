from django.conf.urls import patterns, url
from core.views import index_page, new_question, add_new_question, question_thread, add_new_answer, all_by_tag, like_post, like_answer, user_profile_stats, mark_as_true, fetch_updates

urlpatterns = patterns('',
    url(r'^$', index_page, name='home'),
    url(r'^add/$', new_question, name='create_question'),   # do this in front-end later
    url(r'^save_question/$', add_new_question, name='save_question'),
    url(r'^question/(?P<qid>\d+)/$', question_thread, name='question'),
    url(r'^question/$', question_thread, name='question'),  # same but with error message
    url(r'^add_new_answer/$', add_new_answer, name='add_new_answer'),
    url(r'^tag/(?P<tag_n>[-\w]+)/$', all_by_tag, name='all_by_tag'),
    url(r'^like_post/$', like_post),
    url(r'^like_answ/$', like_answer),
    url(r'^mark_as_true/$', mark_as_true),
    url(r'^fetch_updates/$', fetch_updates),                # real-time notifications GET-endpoint
    url(r'^user/(?P<id>\d+)/$', user_profile_stats, name='user'),
    url(r'^user/$', user_profile_stats, name='user'),       # same but with error message
)
