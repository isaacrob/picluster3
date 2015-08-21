#! /usr/bin/python
import socket, click, os, paramiko, pwd, sys
from subprocess import call, check_output

try:
	import netifaces as ni
	if "wlan0" in ni.interfaces():
		print("using wireless")
		myip=ni.ifaddresses("wlan0")[ni.AF_INET][0]['addr']
		print("my ip address is "+myip)
	elif "etho" in ni.interfaces():
		print("could not find wlan0, using eth0")
		myip=ni.ifaddresses("eth0")[ni.AF_INET][0]['addr']
	else:
		print("could not find suitable interface with netifaces")
		sys.exit()
except ImportError:
	print("could not find netifaces, using socket")
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(('8.8.8.8',80))
	myip=s.getsockname()[0]
except:
	print("something else went wrong, using socket")
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	myip=s.getsockname()[0]

@click.command()
@click.option('--hostfile',default='ipaddresses',help='which hostfile to boot with')
@click.option('--configfile',default='/home/pi/.ipython/profile_picluster3/ipcluster_config.py',help='which config file to write')
@click.option('--controller_ip',default=myip,help='ip of the cluster controller')
def writehostdata(hostfile,configfile,controller_ip):
	file=open(hostfile,'r')
	readfile=file.read()
	splithosts=readfile.split('\n')
	file.close()
	file=open(configfile,'w')
	file.write('c = get_config()\n')
	#file.write("c.LocalControllerLauncher.controller_args=[\'--log-to-file\',\'--log-level=20\',\'--ip="+controller_ip+"\']\n")
	#file.write("c.LocalControllerLauncher.controller_args=[\'--log-to-file\',\'--log-level=20\',\"--ip=\'*\'\"]\n")
	file.write("c.IPClusterEngines.engine_launcher_class = \'SSH\'\n")
	file.write("c.IPClusterStart.controller_launcher_class = \'LocalControllerLauncher\'\n")
	file.write("c.LocalControllerLauncher.controller_args=[\'--log-to-file\',\'--log-level=20\',\'--ip="+myip+"\']\n")
	file.write("c.SSHEngineSetLauncher.engine_args = [\'--log-to-file\', \'--log-level=20\', \'--profile=picluster3\']\n")
	file.write("c.HubFactory.ip=\'*\'\n")
	file.write('c.SSHEngineSetLauncher.engines = {')
	reachable=[]
	print(splithosts)
	for host in splithosts:
		if host=='':
			break
		if str(host)==controller_ip:
			continue
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(2.5)
		try:
			s.connect((str(host),22))
			reachable.append(str(host))
			print("reached "+str(host))
			s.close()
		except:
			print("could not reach "+str(host))
			s.close()
			continue
		if call(['ssh','-oBatchMode=yes','-oStrictHostKeyChecking=no',str(host),"'date'"])==255:
			sshhost='pi@'+str(host)
			c=paramiko.SSHClient()
			c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			c.connect(str(host),username='pi',password='raspberry')
			c.exec_command('sudo chmod 777 /home/pi/.ssh/authorized_keys')
			c.open_sftp().file('/home/pi/.ssh/authorized_keys','a').write(open('/home/pi/.ssh/id_rsa.pub').read())
			#call(['ssh-keyscan',str(host)],stdout=open('/home/pi/.ssh/known_hosts','a'))
			#print 'mark 1'
			#call(['sshpass',"-p'raspberry'",'ssh-copy-id','-i','/home/pi/.ssh/id_rsa',sshhost])
			#call(['ssh-copy-id','-i','/home/pi/.ssh/id_rsa',sshhost])
			#print 'mark 2'
			c.exec_command('sudo chmod 755 /home/pi/.ssh/authorized_keys')
			c.close()
			print('established passwordless ssh to '+str(host))
	print(str(len(reachable))+" hosts reached")
	for host in reachable:
		file.write("\'"+host+"\':2,")
	file.write('}\n')
	file.close()

if __name__=='__main__':
	output=check_output(['ssh-agent'])
	for cmd in output.split(';\n'):
		for cmd2 in cmd.split('; '):
			try:
				cmd2.index('=')
				for var,val in [cmd2.split('=')]:
					print('setting '+var+' to '+val)
					os.environ[var]=val
			except:
				continue
	call(['ssh-add'])
	if not os.path.islink('/usr/local/bin/checknet'):
		call(['sudo','ln','-s','/home/pi/.ipython/profile_picluster3/writeremotehosts.py','/usr/local/bin/checknet'])
	os.chdir("/home/pi/.ipython/profile_picluster3")
	print(pwd.getpwuid( os.getuid() ).pw_name)
	writehostdata()
