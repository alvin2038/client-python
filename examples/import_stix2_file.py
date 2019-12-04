# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = 'https//demo.opencti.io'
api_token = '8f053d6e-cc8f-4ae3-ae24-107130510795'

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# File to import
file_to_import = './enterprise-attack.json'

# Import the bundle
opencti_api_client.stix2.import_bundle_from_file(
    file_to_import,
    True,
    [
        'identity',
        'attack-pattern',
        'course-of-action',
        'intrusion-set',
        'malware',
        'tool',
        'report'
    ])