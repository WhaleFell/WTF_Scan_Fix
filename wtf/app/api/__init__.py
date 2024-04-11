from flask import Blueprint

api = Blueprint("api", __name__)

from . import baseinfo, subdomain, c_section, portscan, simple_portscan, Whois
from .cms import whatcms
from .ip2area import ip
from .dirscan import dirscan
