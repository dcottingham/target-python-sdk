# Copyright 2021 Adobe. All rights reserved.
# This file is licensed to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
"""Handles async operations"""
try:
    import asyncio
except ImportError:
    import trollius as asyncio
    from trollius import From # TODO - add to requirements.txt
import six


# TODO - This doesn't work bc it just acts like another generator in the chain
def yield_from(task):
    if six.PY3:
        yield from task
    else:
        yield From(task)

# TODO - any func passed in here needs to be annotated with @asyncio.coroutine
@asyncio.coroutine
def execute_async(func, args=None, kwargs=None, callback=None):
    """Non-blocking async function wrapper for event-loop based concurrency"""
    if not args:
        args = []
    if not kwargs:
        kwargs = {}
    task = asyncio.ensure_future(func(*args, **kwargs))
    while True:
        # if task.done():
        #     break

        # yield_from(task)  # TODO - will this work?

        if six.PY3:
            yield from task
            break
        yield From(task)
        break
    if callback:  # TODO - we would have to use this for Python2.7
        callback(task.result())
    else:
        return task.result()

# VERDICT - IF WE WANT TO ADD THIS FUNCTIONALITY WE SHOULD DROP SUPPORT FOR PYTHON 2.7.  TOO MANY LOW LEVEL LANGUAGE CONSTRUCTS HAVE CHANGED
# It's not impossible to add the change to 2.7, but will make the code ugly and need to use a bunch of old/deprecated code and will need to use callbacks instead of task.result()
https://medium.com/analytics-vidhya/python-generators-coroutines-async-io-with-examples-28771b586578
https: // gist.github.com / pkazmierczak / efc4a1a62d234379f863
https://docs.python.org/3.6/library/asyncio-dev.html#chain-coroutines-correctly
https://docs.python.org/3/library/asyncio-task.html#task-object
https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future
https://robusgauli.medium.com/non-blocking-i-o-for-python-f4da77d3353a
