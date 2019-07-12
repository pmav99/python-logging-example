# python_logging_example

An example for setting up logging using Python's StdLib.

## Prerequisites

To use the yaml configuration file you will need to install
[ruamel.yaml](https://pypi.org/project/ruamel.yaml/).

``` shell
pip install ruamel.yaml
```

## Examples

- `example_simple.py` contains a lot of explanatory comments. Make sure you read it.
- `example_multi.py` showcases what happens when you spawn multiple processes/threads

## SMTP handler

If you run `python3 simple_example.py` as it is, you will get the following output:

```
INFO:root:This is the logger configured by `logging.basicConfig()`.
INFO:root:We will disable this logger when we setup logger using the config file.
INFO:root:This logger can be useful if we e.g. want to log the path of the config file
INFO:root:we will be using which we can get e.g. as a command line argument etc.
INFO:root:
INFO:root:config file: log_config.yml
2019-07-12 18:00:51,099; INFO    ; [19123 - 139698662942528]; root                               ; <module>            ;  78: This is the logger configured by `logging.config.dictConfig()`.
2019-07-12 18:00:51,099; INFO    ; [19123 - 139698662942528]; root                               ; main                ;  44: This is an INFO message on the root logger.
2019-07-12 18:00:51,099; WARNING ; [19123 - 139698662942528]; child                              ; main                ;  48: This is a WARNING message on the child logger.
2019-07-12 18:00:51,099; ERROR   ; [19123 - 139698662942528]; child                              ; main                ;  51: This is an ERROR message.
--- Logging error ---
Traceback (most recent call last):
  File "/usr/lib/python3.6/logging/handlers.py", line 1010, in emit
    smtp = smtplib.SMTP(self.mailhost, port, timeout=self.timeout)
  File "/usr/lib/python3.6/smtplib.py", line 251, in __init__
    (code, msg) = self.connect(host, port)
  File "/usr/lib/python3.6/smtplib.py", line 336, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "/usr/lib/python3.6/smtplib.py", line 307, in _get_socket
    self.source_address)
  File "/usr/lib/python3.6/socket.py", line 724, in create_connection
    raise err
  File "/usr/lib/python3.6/socket.py", line 713, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused
Call stack:
  File "example_simple.py", line 80, in <module>
    main()
  File "example_simple.py", line 51, in main
    child.error("This is an ERROR message.")
Message: 'This is an ERROR message.'
Arguments: ()
2019-07-12 18:00:51,122; DEBUG   ; [19123 - 139698662942528]; mypkg                              ; <module>            ;   5: Logging from mypkg!
2019-07-12 18:00:51,122; DEBUG   ; [19123 - 139698662942528]; mypkg.subpkg1                      ; <module>            ;   5: Logging from subpkg1!
2019-07-12 18:00:51,122; DEBUG   ; [19123 - 139698662942528]; mypkg.subpkg1.a                    ; func_a              ;   7: Logging from a
2019-07-12 18:00:51,122; DEBUG   ; [19123 - 139698662942528]; mypkg.subpkg1.b                    ; func_b              ;   7: Logging from b
2019-07-12 18:00:51,123; DEBUG   ; [19123 - 139698662942528]; mypkg.subpkg2                      ; <module>            ;   5: Logging from subpkg2!
```

This traceback is not a related to our application. It has to do with the logging configuration.
More specifically we have set an smtp handler that tries to send an email using a MailServer that
runs on 127.0.0.1:60025, but there is no server listening to that ip/port. While developing, we can
easily setup such a server by running the following command on a separate console session:

``` shell
python3 -m smtpd -n -c DebuggingServer 127.0.0.1:60025
```


Needless to say, on production we should set up a proper MailServer. Anyway, now, if we execute the
script we will get the following output:

```
INFO:root:This is the logger configured by `logging.basicConfig()`.
INFO:root:We will disable this logger when we setup logger using the config file.
INFO:root:This logger can be useful if we e.g. want to log the path of the config file
INFO:root:we will be using which we can get e.g. as a command line argument etc.
INFO:root:
INFO:root:config file: log_config.yml
2019-07-12 18:01:38,170; INFO    ; [19540 - 140070813353792]; root                               ; <module>            ;  78: This is the logger configured by `logging.config.dictConfig()`.
2019-07-12 18:01:38,170; INFO    ; [19540 - 140070813353792]; root                               ; main                ;  44: This is an INFO message on the root logger.
2019-07-12 18:01:38,170; WARNING ; [19540 - 140070813353792]; child                              ; main                ;  48: This is a WARNING message on the child logger.
2019-07-12 18:01:38,170; ERROR   ; [19540 - 140070813353792]; child                              ; main                ;  51: This is an ERROR message.
2019-07-12 18:01:38,233; DEBUG   ; [19540 - 140070813353792]; mypkg                              ; <module>            ;   5: Logging from mypkg!
2019-07-12 18:01:38,233; DEBUG   ; [19540 - 140070813353792]; mypkg.subpkg1                      ; <module>            ;   5: Logging from subpkg1!
2019-07-12 18:01:38,234; DEBUG   ; [19540 - 140070813353792]; mypkg.subpkg1.a                    ; func_a              ;   7: Logging from a
2019-07-12 18:01:38,234; DEBUG   ; [19540 - 140070813353792]; mypkg.subpkg1.b                    ; func_b              ;   7: Logging from b
2019-07-12 18:01:38,234; DEBUG   ; [19540 - 140070813353792]; mypkg.subpkg2                      ; <module>            ;   5: Logging from subpkg2!
```

While, on the console that runs the Mail Server we will get the following output:

```
---------- MESSAGE FOLLOWS ----------
b'From: sender@example.com'
b'To: recipient@example.com'
b'Subject: Something went wrong'
b'Date: Fri, 12 Jul 2019 18:01:38 +0200'
b'Content-Type: text/plain; charset="utf-8"'
b'Content-Transfer-Encoding: 7bit'
b'MIME-Version: 1.0'
b'X-Peer: 127.0.0.1'
b''
b'Level: ERROR\\nTime: 2019-07-12 18:01:38,170\\nProcess: 19540\\nThread: 140070813353792\\nLogger: child\\nPath: example_simple:51\\nFunction :main\\nMessage: This is an ERROR message.\\n'
------------ END MESSAGE ------------
```
