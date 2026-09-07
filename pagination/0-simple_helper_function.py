#!/usr/bin/env python3
''' 0-simple_helper_function '''


def index_range(page: int, page_size: int):
    ''' index_range '''
    start = page * page_size - page_size
    end = page * page_size
    return (start, end)
