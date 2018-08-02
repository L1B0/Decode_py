# -*- coding: utf-8 -*-
import binascii
import struct

crc32key = 0x402E2D95
width = '\x00\x00\x02\x72'
for i in range(256, 65535):
         height = struct.pack('>i', i)
         #CRC: 9A768270
         data = '\x49\x48\x44\x52' + width + height + '\x08\x06\x00\x00\x00'
         crc32result = binascii.crc32(data) & 0xffffffff
         if crc32result == crc32key:
                  print ''.join(map(lambda c: "%02X" % ord(c), height))
