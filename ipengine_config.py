# Configuration file for ipengine.

c = get_config()

#------------------------------------------------------------------------------
# IPEngineApp configuration
#------------------------------------------------------------------------------

# IPEngineApp will inherit config from: BaseParallelApplication,
# BaseIPythonApplication, Application

# The IPython profile to use.
# c.IPEngineApp.profile = u'default'

# Set the log level by value or name.
# c.IPEngineApp.log_level = 30

# specify a command to be run at startup
# c.IPEngineApp.startup_command = ''

# Set the working dir for the process.
# c.IPEngineApp.work_dir = u'/home/pi/.ipython/profile_demo'

# whether to log to a file
# c.IPEngineApp.log_to_file = False

# The URL for the iploggerapp instance, for forwarding logging to a central
# location.
# c.IPEngineApp.log_url = ''

# Whether to create profile dir if it doesn't exist
# c.IPEngineApp.auto_create = False

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPEngineApp.verbose_crash = False

# whether to cleanup old logfiles before starting
# c.IPEngineApp.clean_logs = False

# String id to add to runtime files, to prevent name collisions when using
# multiple clusters with a single profile simultaneously.
# 
# When set, files will be named like: 'ipcontroller-<cluster_id>-engine.json'
# 
# Since this is text inserted into filenames, typical recommendations apply:
# Simple character strings are ideal, and spaces are not recommended (but should
# generally work).
# c.IPEngineApp.cluster_id = ''

# specify a script to be run at startup
# c.IPEngineApp.startup_script = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPEngineApp.copy_config_files = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPEngineApp.ipython_dir = u'/home/pi/.ipython'

# The Logging format template
# c.IPEngineApp.log_format = '[%(name)s] %(message)s'

# 
# c.IPEngineApp.url_file_name = u'ipcontroller-engine.json'

# The full location of the file containing the connection information for the
# controller. If this is not given, the file must be in the security directory
# of the cluster directory.  This location is resolved using the `profile` or
# `profile_dir` options.
# c.IPEngineApp.url_file = u''

# Whether to overwrite existing config files when copying
# c.IPEngineApp.overwrite = False

# The maximum number of seconds to wait for url_file to exist. This is useful
# for batch-systems and shared-filesystems where the controller and engine are
# started at the same time and it may take a moment for the controller to write
# the connector files.
# c.IPEngineApp.wait_for_url_file = 5

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialiization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Username for the Session. Default is your system username.
# c.Session.username = 'pi'

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# The UUID identifying this session.
# c.Session.session = u''

# execution key, for extra authentication.
# c.Session.key = ''

# Debug output in the Session
# c.Session.debug = False

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# path to file containing execution key.
# c.Session.keyfile = ''

#------------------------------------------------------------------------------
# EngineFactory configuration
#------------------------------------------------------------------------------

# IPython engine

# EngineFactory will inherit config from: RegistrationFactory

# The SSH private key file to use when tunneling connections to the Controller.
# c.EngineFactory.sshkey = u''

# The 0MQ url used for registration. This sets transport, ip, and port in one
# variable. For example: url='tcp://127.0.0.1:12345' or url='epgm://*:90210'
# c.EngineFactory.url = ''

# The IP address for registration.  This is generally either '127.0.0.1' for
# loopback only or '*' for all interfaces. [default: '127.0.0.1']
# c.EngineFactory.ip = '127.0.0.1'

# The 0MQ transport for communications.  This will likely be the default of
# 'tcp', but other values include 'ipc', 'epgm', 'inproc'.
# c.EngineFactory.transport = 'tcp'

# The OutStream for handling stdout/err. Typically
# 'IPython.zmq.iostream.OutStream'
# c.EngineFactory.out_stream_factory = 'IPython.zmq.iostream.OutStream'

# The class for handling displayhook. Typically
# 'IPython.zmq.displayhook.ZMQDisplayHook'
# c.EngineFactory.display_hook_factory = 'IPython.zmq.displayhook.ZMQDisplayHook'

# The port on which the Hub listens for registration.
# c.EngineFactory.regport = 0

# Whether to use paramiko instead of openssh for tunnels.
# c.EngineFactory.paramiko = False

# The time (in seconds) to wait for the Controller to respond to registration
# requests before giving up.
# c.EngineFactory.timeout = 2

# The SSH server to use for tunneling connections to the Controller.
# c.EngineFactory.sshserver = u''

# The location (an IP address) of the controller.  This is used for
# disambiguating URLs, to determine whether loopback should be used to connect
# or the public address.
# c.EngineFactory.location = u''

#------------------------------------------------------------------------------
# Kernel configuration
#------------------------------------------------------------------------------

# 
# c.Kernel._execute_sleep = 0.0005

# 
# c.Kernel._poll_interval = 0.05

#------------------------------------------------------------------------------
# MPI configuration
#------------------------------------------------------------------------------

# Configurable for MPI initialization

# 
# c.MPI.default_inits = {'pytrilinos': 'from PyTrilinos import Epetra\nclass SimpleStruct:\npass\nmpi = SimpleStruct()\nmpi.rank = 0\nmpi.size = 0\n', 'mpi4py': 'from mpi4py import MPI as mpi\nmpi.size = mpi.COMM_WORLD.Get_size()\nmpi.rank = mpi.COMM_WORLD.Get_rank()\n'}

# Initialization code for MPI
# c.MPI.init_script = ''

# How to enable MPI (mpi4py, pytrilinos, or empty string to disable).
# c.MPI.use = ''
