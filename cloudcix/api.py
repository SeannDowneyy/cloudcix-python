# python
from __future__ import unicode_literals

# libs

# local
from .base import APIClient


# Membership
class membership(object):
    _application_name = 'Membership'
    address = APIClient(application=_application_name,
                        service_uri='Address/')
    address_link = APIClient(application=_application_name,
                             service_uri='Address/%(idAddress)s/Link/')
    country = APIClient(application=_application_name,
                        service_uri='Country/')
    currency = APIClient(application=_application_name,
                         service_uri='Currency/')
    department = APIClient(application=_application_name,
                           service_uri='Member/%(idMember)/Department/')
    language = APIClient(application=_application_name,
                         service_uri='Language/')
    member = APIClient(application=_application_name,
                       service_uri='Member/')
    member_link = APIClient(application=_application_name,
                            service_uri='Member/%(idMember)/Link/')
    notification = APIClient(application=_application_name,
                             service_uri='Address/%(idAddress)/Notification/')
    profile = APIClient(application=_application_name,
                        service_uri='Member/%(idMember)/Profile/')
    subdivision = APIClient(application=_application_name,
                            service_uri='Country/%(idCountry)s/Subdivision/')
    team = APIClient(application=_application_name,
                     service_uri='Member/%(idMember)/Team/')
    territory = APIClient(application=_application_name,
                          service_uri='Member/%(idMember)/Territory/')
    timezone = APIClient(application=_application_name,
                         service_uri='Timezone/')
    transaction_type = APIClient(application=_application_name,
                                 service_uri='TransactionType/')
    user = APIClient(application=_application_name,
                     service_uri='User/')


# Antenna services
class antenna(object):
    _application_name = 'Antenna'
    antenna = APIClient(application=_application_name,
                        service_uri='Antenna/')


# Contacts Services
class contacts(object):
    _application_name = 'Contacts'
    campaign = APIClient(application=_application_name,
                         service_uri='Campaign/')
    group = APIClient(application=_application_name,
                      service_uri='Group/')
    contact = APIClient(application=_application_name,
                        service_uri='Contact/')
    campaign_contact = APIClient(
        application=_application_name,
        service_uri='Campaign/%(idCampaign)s/Contact/')
    group_contact = APIClient(
        application=_application_name,
        service_uri='Group/%(idGroup)s/Contact/')


# DNS Services
class dns(object):
    _application_name = 'DNS'
    asn = APIClient(application=_application_name,
                    service_uri='ASN/')
    allocation = APIClient(application=_application_name,
                           service_uri='Allocation/')
    subnet = APIClient(application=_application_name,
                       service_uri='Subnet/')
    subnet_space = APIClient(
        application=_application_name,
        service_uri='Allocation/%(idAllocation)s/Subnet_space/')
    ipaddress = APIClient(application=_application_name,
                          service_uri='IPAddress/')
    recordptr = APIClient(application=_application_name,
                          service_uri='RecordPTR/')
    domain = APIClient(application=_application_name,
                       service_uri='Domain/')
    record = APIClient(application=_application_name,
                       service_uri='Record/')
    blacklist = APIClient(application=_application_name,
                          service_uri='Blacklist/')


# Documentation Services
class documentation(object):
    _application_name = 'Documentation'
    application = APIClient(application=_application_name,
                            service_uri='Application/')
