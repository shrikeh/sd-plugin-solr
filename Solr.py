# -*- coding: utf-8 -*-

"""
Server Density Solr Monitoring Plugin
"""

class Solr(object):
    def __init__(self, agent_config, checks_logger, raw_config):
        self.agent_config = agent_config
        self.logger = checks_logger
        self.raw_config = raw_config

    def run(self):
