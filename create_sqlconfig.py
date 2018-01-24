#!/usr/bin/python3
from cryptography.fernet import Fernet
from optparse import OptionParser
import json
import os

def main():
	parser = OptionParser()
	parser.add_option("-d", "--driver", dest="driver", type="string")
	parser.add_option("-b", "--db", dest="database", type="string")
	parser.add_option("-o", "--host", dest="host", type="string")
	parser.add_option("-u", "--user", dest="user", type="string")
	parser.add_option("-p", "--pass", dest="password", type="string")
	parser.add_option("-f", "--file", dest="filename", type="string")

	(options, args) = parser.parse_args()

	cwd = os.getcwd()
	if options.filename is None:
		fname = 'config.json'
		fdir = os.path.join(cwd, fname)
	else:
		if not options.filename.endswith('.json'):
			raise Exception('Filename must be of json extension')
		else:
			fdir = os.path.join(cwd, options.filename)

	key = Fernet.generate_key()
	f = Fernet(key)

	# iso-8859-15
	obj = {}
	if options.driver is not None:
		if options.driver == 'tsql':
			obj.update(dict(driver=f.encrypt('{ODBC Driver 13 for SQL Server}'.encode('iso-8859-15')).decode('utf-8')))
	if options.database is not None:
		obj.update(dict(database=f.encrypt(options.database.encode('iso-8859-15')).decode('utf-8')))
	if options.host is not None:
		obj.update(dict(host=f.encrypt(options.host.encode('iso-8859-15')).decode('utf-8')))
	if options.user is not None:
		obj.update(dict(user=f.encrypt(options.user.encode('iso-8859-15')).decode('utf-8')))
	if options.password is not None:
		print(options.password)
		obj.update(dict(password=f.encrypt(options.password.encode('iso-8859-15')).decode('utf-8')))

	obj.update(dict(key=key.decode('utf-8')))

	with open(fdir, 'w+') as file:
		file.write(str(json.dumps(obj)))

if __name__ == '__main__':
	main()
