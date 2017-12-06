#!/usr/bin/env python

import os
import logging

import credstash


CREDSTASH_TABLE = os.getenv("CREDSTASH_TABLE")
CREDSTASH_KEY = os.getenv("CREDSTASH_KEY")

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info("table: %s, key %s", CREDSTASH_TABLE, CREDSTASH_KEY)

if CREDSTASH_TABLE is None:
    secret = credstash.getSecret(CREDSTASH_KEY)
else:
    secret = credstash.getSecret(CREDSTASH_KEY, table=CREDSTASH_TABLE)

print("secret decrypted successfully: {}".format(secret))
