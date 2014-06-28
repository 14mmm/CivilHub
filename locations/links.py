# -*- coding: utf-8 -*-
#
# Mapujemy linki dla sidebaru dla różnych widoków. Zakładam, że sidebary będą
# się różnić w zależności od modułu, ale w każdym module będziemy mieli ten
# sam zestaw linków dla poszczególnych pod-widoków (edycja, usuwanie itp.).
#
LINKS_MAP = {
    'summary': (
        'invite',
    ),
    'news': (
        'new_discussion',
        'new_poll',
        'new_idea',
        'add_news',
        'invite',
    ),
    'discussions': (
        'new_discussion',
        'new_poll',
        'new_location',
        'new_idea',
        'upload',
        'invite',
    ),
    'ideas': (
        'new_discussion',
        'new_poll',
        'new_idea',
        'add_news',
        'invite',
    ),
    'polls': (
        'new_discussion',
        'new_poll',
        'new_idea',
        'add_news',
        'invite',
    ),
    'gallery': (
        'new_discussion',
        'new_poll',
        'new_idea',
        'add_news',
        'invite',
    ),
    'followers': (
        'invite',
    ),
    'sublocations': (
        'invite',
    ),
}
