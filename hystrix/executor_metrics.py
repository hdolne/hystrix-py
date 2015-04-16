from __future__ import absolute_import
import logging

import six

log = logging.getLogger(__name__)


class ExecutorMetricsMetaclass(type):

    __instances__ = dict()
    __blacklist = ('ExecutorMetrics', 'ExecutorMetricsMetaclass')

    def __new__(cls, name, bases, attrs):

        if name in cls.__blacklist:
            return super(ExecutorMetricsMetaclass, cls).__new__(cls, name,
                                                                bases, attrs)

        class_name = attrs.get('__executor_metrics_name__',
                               '{}ExecutorMetrics'.format(name))
        new_class = super(ExecutorMetricsMetaclass, cls).__new__(cls,
                                                                 class_name,
                                                                 bases, attrs)
        setattr(new_class, 'executor_metrics_name', class_name)

        if class_name not in cls.__instances__:
            cls.__instances__[class_name] = new_class

        return cls.__instances__[class_name]


class ExecutorMetrics(six.with_metaclass(ExecutorMetricsMetaclass, object)):

    __executor_metrics_name__ = None