try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


try:
    import cPickle as pickle
except ImportError:
    import pickle


# Handle the case where the requests has been patched to not have urllib3
# bundled as part of it's source.
try:
    from pip._vendor.requests.packages.urllib3.response import HTTPResponse
except ImportError:
    from urllib3.response import HTTPResponse

try:
    from pip._vendor.requests.packages.urllib3.util import is_fp_closed
except ImportError:
    from urllib3.util import is_fp_closed
