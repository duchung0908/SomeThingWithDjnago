import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'json': {
            "()": "json_log_formatter.JSONFormatter",
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
    },
    'handlers': {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
            'stream': sys.stdout,
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
