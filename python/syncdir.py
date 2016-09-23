# -*- coding: utf-8 -*-
# http://oldj.net/
# edit by wkj 2016/9/14
 
"""
同步两个文件夹
 
用法：
 
python syncdir.py source_dir target_dir
 
执行后，source_dir 中的文件将被同步到 target_dir 中
这个同步是单向的，即只将 source_dir 中更新或新增的文件拷到 target_dir 中，
如果某个文件在 source_dir 中不存在而在 target_dir 中存在，本程序不会删除那个文件，
也不会将其拷贝到 source_dir 中
 
判断文件是否更新的方法是比较文件最后修改时间以及文件大小是否一致
"""
 
import os
import sys
import shutil
import logging
import time
#日志文件配置
log_filename =time.strftime("%Y%m%d%H%M%S_", time.localtime())+'sync.log'
#日志输出格式化
log_format = '%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format,datefmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG) 
#日志输出到日志文件
fileLogger = logging.getLogger('fileLogger')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.INFO)
fileLogger.addHandler(fh);
 
def errExit(msg):
	print "-" * 50
	print "ERROR:"
	print msg
	sys.exit(1)
 
def main(source_dir, target_dir):
	print "synchronize '%s' >> '%s'..." % (source_dir, target_dir)
	print "=" * 50
	sync_file_count = 0
	sync_file_size = 0
 
	for root, dirs, files in os.walk(source_dir):
		relative_path = root.replace(source_dir, "")
		if len(relative_path) > 0 and relative_path[0] in ("/", "\\"):
			relative_path = relative_path[1:]
		dist_path = os.path.join(target_dir, relative_path)
 
		if os.path.isdir(dist_path) == False:
			os.makedirs(dist_path)
 
		last_copy_folder = ""
		for fn0 in files:
			fn = os.path.join(root, fn0)
			fn2 = os.path.join(dist_path, fn0)
			is_copy = False
			if os.path.isfile(fn2) == False:
				is_copy = True
			else:
				statinfo = os.stat(fn)
				statinfo2 = os.stat(fn2)
				is_copy = (
						round(statinfo.st_mtime, 3) != round(statinfo2.st_mtime, 3) 
						or statinfo.st_size != statinfo2.st_size
					)
 
			if is_copy:
				if dist_path != last_copy_folder:
					print "[ %s ]" % dist_path
					last_copy_folder = dist_path
				print "copying '%s' ..." % fn0
				fileLogger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" "+source_dir +" => "+target_dir+"  %s " % dist_path+" %s " % fn0)
				shutil.copy2(fn, fn2)
				sync_file_count += 1
				sync_file_size += os.stat(fn).st_size
 
	if sync_file_count > 0:
		print "-" * 50
	print "%d files synchronized!" % sync_file_count
	if sync_file_size > 0:
		print "%d bytes." % sync_file_size
	print "done!"
 
if __name__ == "__main__":
	'''
	#使用参数
	if len(sys.argv) != 3:
		if "-h" in sys.argv or "--help" in sys.argv:
			print __doc__
			sys.exit(1)
		errExit(u"invalid arguments!")
	source_dir, target_dir = sys.argv[1:]
	'''
	#source_dir 原文件
	#target_dir 目标 //edit by wkj 2016-09-14
	source_dir = './test1'
	target_dir = './test2'
	if os.path.isdir(source_dir) == False:
		errExit(u"'%s' is not a folder!" % source_dir)
	elif os.path.isdir(target_dir) == False:
		errExit(u"'%s' is not a folder!" % target_dir)
 
	main(source_dir, target_dir)