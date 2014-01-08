def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_test'


def includeme(config):
    config.scan()
