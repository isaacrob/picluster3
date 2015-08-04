c = get_config()
c.IPClusterEngines.engine_launcher_class = 'SSH'
c.IPClusterStart.controller_launcher_class = 'LocalControllerLauncher'
c.LocalControllerLauncher.controller_args=['--log-to-file','--log-level=20','--ip=10.40.2.31']
c.SSHEngineSetLauncher.engine_args = ['--log-to-file', '--log-level=20', '--profile=picluster3']
c.HubFactory.ip='*'
c.SSHEngineSetLauncher.engines = {'10.40.2.64':2,'10.40.2.65':2,'10.40.2.66':2,}
