from .generators import simple_generator
from .selectors import select_event
import logging
logger = logging.getLogger(__name__)


def detect_counter_example(algorithm, args, kwargs):
    logger.info('Starting to find counter example on algorithm {0} with argument {1} ; {2} \n'.format(algorithm.__name__,
                                                                                                      args, kwargs))
    input_list = simple_generator(algorithm, 5)
    for d1, d2, extra_args in input_list:
        kwargs.update(extra_args)
        event = select_event(algorithm, args, kwargs, cores=cores, search_space=search_space)



