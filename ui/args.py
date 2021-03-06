#!/usr/bin/env python
#coding=utf-8
#########################################################
# 							#
# This is BashStyle-NG  				#
#							#
# Licensed under GNU GENERAL PUBLIC LICENSE v3		#
#							#
# Copyright 2007 - 2013 Christopher Bratusek		#
#							#
#########################################################

MODULES = [ 'os', 'os.path', 'sys', 'string', 'ctypes', 'optparse', 'subprocess']

FAILED = []

for module in MODULES:
	try:
		globals()[module] = __import__(module)
	except ImportError:
		FAILED.append(module)

class CmdArgs(object):
	parser = optparse.OptionParser("bashstyle <option> [value]\
					\n\nBashStyle-NG (c) 2007 - 2013 Christopher Bratusek\
					\nLicensed under the GNU GENERAL PUBLIC LICENSE v3")

	if sys.platform == 'linux2':
		try:
			libc = ctypes.CDLL('libc.so.6')
			libc.prctl(15, 'bashstyle', 0, 0, 0)
		except:
			pass

	parser.add_option("-v", "--version", dest="version",
			  action="store_true", default=False, help="print version and exit")

	parser.add_option("-p", "--prefix", dest="prefix",
			  action="store_true", default=False, help="print prefix and exit")

	parser.add_option("-g", "--group", dest="group", default="style",
			  help="display a given group of options at startup, one of:\
			  \nstyle, alias, advanced, readline, vim, nano, ls or custom")

	(options, args) = parser.parse_args()

	if options.version:
		print "%s" % os.getenv('BSNG_UI_VERSION')
		sys.exit(0)

	if options.prefix:
		print "%s" % os.getenv('BSNG_UI_PREFIX')
		sys.exit(0)
