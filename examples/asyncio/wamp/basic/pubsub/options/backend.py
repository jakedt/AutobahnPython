###############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import asyncio

from autobahn.wamp.types import PublishOptions, EventDetails, SubscribeOptions
from autobahn.asyncio.wamp import ApplicationSession



class Component(ApplicationSession):
   """
   An application component that publishes an event every second.
   """

   @asyncio.coroutine
   def onJoin(self, details):

      def on_event(i):
         print("Got event: {}".format(i))

      yield from self.subscribe(on_event, 'com.myapp.topic1')


      counter = 0
      while True:
         publication = yield from self.publish('com.myapp.topic1', counter,
               options = PublishOptions(acknowledge = True, discloseMe = True, excludeMe = False))
         print("Event published with publication ID {}".format(publication.id))
         counter += 1
         yield from asyncio.sleep(1)
