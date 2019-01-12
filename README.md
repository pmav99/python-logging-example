# python_logging_example

An example for python logging using StdLib.

## Prerequisites

To use the yaml configuration file you will need to install
[pyyaml](https://pypi.org/project/PyYAML/).

``` shell
pip install pyyaml
```

## SMTP handler

To use the SMTP handler you need an SMTP server.
You can run up a test stmp server on your local machine by running:

``` shell
python3 -m smtpd -n -c DebuggingServer 127.0.0.1:60025
```
