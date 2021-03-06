# -*- coding: utf-8 -*-
"""
See README for database download.
"""
from __future__ import unicode_literals
import sys

from intelmq.lib.bot import Bot


class TorExpertBot(Bot):

    database = set()

    def init(self):
        self.logger.info("Loading TOR exit node IPs.")

        try:
            with open(self.parameters.database) as fp:
                for line in fp:
                    line = line.strip()

                    if len(line) == 0 or line[0] == "#":
                        continue

                    self.database.add(line)

        except IOError:
            self.logger.critical("TOR rule not defined or failed on open.")
            self.stop()

    def process(self):
        event = self.receive_message()

        if event is None:
            self.acknowledge_message()
            return

        for key in ["source.", "destination."]:
            if event.contains(key + 'ip'):
                if event.get(key + 'ip') in self.database:
                    event.add(key + 'tor_node', True)

        self.send_message(event)
        self.acknowledge_message()


if __name__ == "__main__":
    bot = TorExpertBot(sys.argv[1])
    bot.start()
