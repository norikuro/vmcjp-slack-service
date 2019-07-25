# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.type.ovf.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Cpu(VapiStruct):
    """
    Provide the CPU information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 num_cpus=None,
                 reservation=None,
                 limit=None,
                 shares=None,
                ):
        """
        :type  num_cpus: :class:`long`
        :param num_cpus: number of CPUs
        :type  reservation: :class:`long` or ``None``
        :param reservation: reservation in MHz
            It is optional to set a CPU reservation.
        :type  limit: :class:`long` or ``None``
        :param limit: CPU limit in MHz
            Is is optional to set a CPU limit.
        :type  shares: :class:`long` or ``None``
        :param shares: CPU shares
            It is optional to specify CPU shares.
        """
        self.num_cpus = num_cpus
        self.reservation = reservation
        self.limit = limit
        self.shares = shares
        VapiStruct.__init__(self)


Cpu._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.cpu', {
        'num_cpus': type.IntegerType(),
        'reservation': type.OptionalType(type.IntegerType()),
        'limit': type.OptionalType(type.IntegerType()),
        'shares': type.OptionalType(type.IntegerType()),
    },
    Cpu,
    False,
    None))



class Disk(VapiStruct):
    """
    Provide the disk information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 disk_capacity=None,
                 storage_policy=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the disk
        :type  disk_capacity: :class:`long`
        :param disk_capacity: Capacity of the disk in megabytes
        :type  storage_policy: :class:`com.vmware.content.type.ovf.policy_client.StoragePolicy` or ``None``
        :param storage_policy: Storage policy of the disk. 
            
            It is a reference to the storage policy group.
            It is not required that storage policy be specified.
        """
        self.name = name
        self.disk_capacity = disk_capacity
        self.storage_policy = storage_policy
        VapiStruct.__init__(self)


Disk._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.disk', {
        'name': type.StringType(),
        'disk_capacity': type.IntegerType(),
        'storage_policy': type.OptionalType(type.ReferenceType('com.vmware.content.type.ovf.policy_client', 'StoragePolicy')),
    },
    Disk,
    False,
    None))



class DiskController(VapiStruct):
    """
    Provide the disk controller information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 type=None,
                 sub_type=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the disk controller
        :type  type: :class:`str` or ``None``
        :param type: Disk controller type: DiskControllerType.IDE.SATA.SCSI;
            It is optional to specify a disk controller type.
        :type  sub_type: :class:`str` or ``None``
        :param sub_type: Disk controller sub type: DiskControllerSubType
            It is optional to specify a disk controller subtype.
        """
        self.name = name
        self.type = type
        self.sub_type = sub_type
        VapiStruct.__init__(self)


DiskController._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.disk_controller', {
        'name': type.StringType(),
        'type': type.OptionalType(type.StringType()),
        'sub_type': type.OptionalType(type.StringType()),
    },
    DiskController,
    False,
    None))



class Drive(VapiStruct):
    """
    Provide the drive information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 type=None,
                 sub_type=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the drive
        :type  type: :class:`str` or ``None``
        :param type: Drive type
            It is optional to specify a drive type.
        :type  sub_type: :class:`str` or ``None``
        :param sub_type: Drive sub type
            It is optional to specify a drive subtype.
        """
        self.name = name
        self.type = type
        self.sub_type = sub_type
        VapiStruct.__init__(self)


Drive._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.drive', {
        'name': type.StringType(),
        'type': type.OptionalType(type.StringType()),
        'sub_type': type.OptionalType(type.StringType()),
    },
    Drive,
    False,
    None))



class Floppy(VapiStruct):
    """
    Provide the floppy information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 connected=None,
                 type=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the floppy
        :type  connected: :class:`bool` or ``None``
        :param connected: True if floppy is connected
            It is optional to specify if a floppy is connected.
        :type  type: :class:`str` or ``None``
        :param type: Floppy type
            It is optional to specify the type of floppy drive.
        """
        self.name = name
        self.connected = connected
        self.type = type
        VapiStruct.__init__(self)


Floppy._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.floppy', {
        'name': type.StringType(),
        'connected': type.OptionalType(type.BooleanType()),
        'type': type.OptionalType(type.StringType()),
    },
    Floppy,
    False,
    None))



class Memory(VapiStruct):
    """
    Provide the memory information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 size=None,
                 reservation=None,
                 limit=None,
                 shares=None,
                ):
        """
        :type  size: :class:`long`
        :param size: memory size in MB
        :type  reservation: :class:`long` or ``None``
        :param reservation: memory reservation in MB
            It is not required that memory reservation be specified.
        :type  limit: :class:`long` or ``None``
        :param limit: memory limit in MB
            It is not required that memory limit be specified.
        :type  shares: :class:`long` or ``None``
        :param shares: memory shares
            It is not required that memory shares be specified.
        """
        self.size = size
        self.reservation = reservation
        self.limit = limit
        self.shares = shares
        VapiStruct.__init__(self)


Memory._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.memory', {
        'size': type.IntegerType(),
        'reservation': type.OptionalType(type.IntegerType()),
        'limit': type.OptionalType(type.IntegerType()),
        'shares': type.OptionalType(type.IntegerType()),
    },
    Memory,
    False,
    None))



class Network(VapiStruct):
    """
    Provide network information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 description=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the network
        :type  description: :class:`str` or ``None``
        :param description: Description of the network
            Networks do not require a description.
        """
        self.name = name
        self.description = description
        VapiStruct.__init__(self)


Network._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.network', {
        'name': type.StringType(),
        'description': type.OptionalType(type.StringType()),
    },
    Network,
    False,
    None))



class Nic(VapiStruct):
    """
    Provide NIC information in a VM template

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 network_name=None,
                 mac_address=None,
                 start_connected=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of NIC
        :type  network_name: :class:`str` or ``None``
        :param network_name: Name of the network that this NIC connects to
            It is not required that network name be specified.
        :type  mac_address: :class:`str` or ``None``
        :param mac_address: Mac address of this NIC
            It is not required that MAC address be specified.
        :type  start_connected: :class:`bool` or ``None``
        :param start_connected: True if this nic will be connected on start.
            It is not required that whether the NIC is connected be specified.
        """
        self.name = name
        self.network_name = network_name
        self.mac_address = mac_address
        self.start_connected = start_connected
        VapiStruct.__init__(self)


Nic._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.nic', {
        'name': type.StringType(),
        'network_name': type.OptionalType(type.StringType()),
        'mac_address': type.OptionalType(type.StringType()),
        'start_connected': type.OptionalType(type.BooleanType()),
    },
    Nic,
    False,
    None))



class OvfTemplate(VapiStruct):
    """
    Provides extra information about a library item of type "ovf". 
    
    An OVF library item is the basic building block for instantiating virtual
    machines from content library. It may contain one or multiple virtual
    machine templates. This structure provides a rich view of the virtual
    machines within the ovf container as well as information about to the ovf
    descriptor associated with the library item 

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 vm_count=None,
                 version=None,
                 library_id_parent=None,
                 is_vapp_template=None,
                 vm_template=None,
                 vapp_template=None,
                 networks=None,
                 storage_policy_groups=None,
                ):
        """
        :type  id: :class:`str`
        :param id: Library item id.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.Item``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.content.library.Item``.
        :type  vm_count: :class:`long`
        :param vm_count: Number of virtual machines in the the ovf template.
        :type  version: :class:`str`
        :param version: A version number indicating the generation of the ``OvfTemplate`` 
            
             This value is incremented every time ``OvfTemplate`` changes. 
        :type  library_id_parent: :class:`str`
        :param library_id_parent: The identifier of the
            :class:`com.vmware.content_client.LibraryModel` to which this item
            belongs. This is used to set the parent of the ovf template for
            permission propagation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.Library``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.content.Library``.
        :type  is_vapp_template: :class:`bool`
        :param is_vapp_template: True if this is a vApp template, otherwise this is a VM template.
        :type  vm_template: :class:`VmTemplate` or ``None``
        :param vm_template: The Vitrual Machine if this is a VM template
            An OVF template does not require a VM template.
        :type  vapp_template: :class:`VAppTemplate` or ``None``
        :param vapp_template: The root VApp template in this OVF template if this is a vApp
            template
            An OVF template does not require a vApp template.
        :type  networks: :class:`list` of :class:`Network`
        :param networks: networks in this OVF template
        :type  storage_policy_groups: :class:`list` of :class:`com.vmware.content.type.ovf.policy_client.StoragePolicyGroup` or ``None``
        :param storage_policy_groups: Storage policy groups for disks, virtual machines and/or virtual
            machine collections.
            An OVF template does not require policies.
        """
        self.id = id
        self.vm_count = vm_count
        self.version = version
        self.library_id_parent = library_id_parent
        self.is_vapp_template = is_vapp_template
        self.vm_template = vm_template
        self.vapp_template = vapp_template
        self.networks = networks
        self.storage_policy_groups = storage_policy_groups
        VapiStruct.__init__(self)


OvfTemplate._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.ovf_template', {
        'id': type.IdType(resource_types='com.vmware.content.library.Item'),
        'vm_count': type.IntegerType(),
        'version': type.StringType(),
        'library_id_parent': type.IdType(resource_types='com.vmware.content.Library'),
        'is_vapp_template': type.BooleanType(),
        'vm_template': type.OptionalType(type.ReferenceType(__name__, 'VmTemplate')),
        'vapp_template': type.OptionalType(type.ReferenceType(__name__, 'VAppTemplate')),
        'networks': type.ListType(type.ReferenceType(__name__, 'Network')),
        'storage_policy_groups': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.content.type.ovf.policy_client', 'StoragePolicyGroup'))),
    },
    OvfTemplate,
    True,
    ["id"]))



class USBController(VapiStruct):
    """
    Provide USB controller information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                 auto_connect=None,
                 ehci_pci_slot_number=None,
                 pci_slot_number=None,
                ):
        """
        :type  type: :class:`str` or ``None``
        :param type: USBControllerType.EHCI (USB 2.0), XHCI (USB 3.0)
            A template is not required to specify the USB type.
        :type  auto_connect: :class:`bool` or ``None``
        :param auto_connect: True if the USB controller is connected automatically
            A template is not required to specify if auto connect.
        :type  ehci_pci_slot_number: :class:`long` or ``None``
        :param ehci_pci_slot_number: ehci.pci slot number
            A template is not required to specify the ehci.pci slot number.
        :type  pci_slot_number: :class:`long` or ``None``
        :param pci_slot_number: pci slot number
            A template is not required to specify the pci slot number.
        """
        self.type = type
        self.auto_connect = auto_connect
        self.ehci_pci_slot_number = ehci_pci_slot_number
        self.pci_slot_number = pci_slot_number
        VapiStruct.__init__(self)


USBController._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.USB_controller', {
        'type': type.OptionalType(type.StringType()),
        'auto_connect': type.OptionalType(type.BooleanType()),
        'ehci_pci_slot_number': type.OptionalType(type.IntegerType()),
        'pci_slot_number': type.OptionalType(type.IntegerType()),
    },
    USBController,
    False,
    None))



class VAppTemplate(VapiStruct):
    """
    Provide information for vApp template in an OVF template file.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 vapp_name=None,
                 vm_templates=None,
                 storage_policies=None,
                ):
        """
        :type  vapp_name: :class:`str` or ``None``
        :param vapp_name: Name of the vApp template
            vApp templates do not require a name.
        :type  vm_templates: :class:`list` of :class:`VmTemplate` or ``None``
        :param vm_templates: Vitrual Machines in this vApp template
            vApp templates do not require a list of VM templates.
        :type  storage_policies: :class:`list` of :class:`com.vmware.content.type.ovf.policy_client.StoragePolicy` or ``None``
        :param storage_policies: Storage policies of the vApp template.
            vApp templates do not require a list of storage policies.
        """
        self.vapp_name = vapp_name
        self.vm_templates = vm_templates
        self.storage_policies = storage_policies
        VapiStruct.__init__(self)


VAppTemplate._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.V_app_template', {
        'vapp_name': type.OptionalType(type.StringType()),
        'vm_templates': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VmTemplate'))),
        'storage_policies': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.content.type.ovf.policy_client', 'StoragePolicy'))),
    },
    VAppTemplate,
    False,
    None))



class VideoCard(VapiStruct):
    """
    Provide video card information in a template VM.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 render_type=None,
                 video_ram_size=None,
                 graphics_memory_size=None,
                 enable3d=None,
                 num_displays=None,
                 use_auto_detect=None,
                ):
        """
        :type  render_type: :class:`str` or ``None``
        :param render_type: Render type
            A template is not required to specify the render type.
        :type  video_ram_size: :class:`long` or ``None``
        :param video_ram_size: video RAM size in KB
            A template is not required to specify the video RAM.
        :type  graphics_memory_size: :class:`long` or ``None``
        :param graphics_memory_size: graphics memory size in KB
            A template is not required to specify the amount of graphics
            memory.
        :type  enable3d: :class:`bool` or ``None``
        :param enable3d: True if 3D is enabled
            A template is not required to specify if 3D is enabled.
        :type  num_displays: :class:`long` or ``None``
        :param num_displays: number of displayes
            A template is not required to specify the number of displays.
        :type  use_auto_detect: :class:`bool` or ``None``
        :param use_auto_detect: True if use auto detect
            A template is not required to specify use auto dectect.
        """
        self.render_type = render_type
        self.video_ram_size = video_ram_size
        self.graphics_memory_size = graphics_memory_size
        self.enable3d = enable3d
        self.num_displays = num_displays
        self.use_auto_detect = use_auto_detect
        VapiStruct.__init__(self)


VideoCard._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.video_card', {
        'render_type': type.OptionalType(type.StringType()),
        'video_ram_size': type.OptionalType(type.IntegerType()),
        'graphics_memory_size': type.OptionalType(type.IntegerType()),
        'enable3d': type.OptionalType(type.BooleanType()),
        'num_displays': type.OptionalType(type.IntegerType()),
        'use_auto_detect': type.OptionalType(type.BooleanType()),
    },
    VideoCard,
    False,
    None))



class VmTemplate(VapiStruct):
    """
    Provide template VM information in an OVF template (see OvfTemplate#type).
    The template VM provide the information about the operation system, CPU,
    memory, disks and NICs.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 vm_name=None,
                 os_type=None,
                 os_description=None,
                 cpu=None,
                 memory=None,
                 disks=None,
                 nics=None,
                 video_cards=None,
                 drives=None,
                 floppies=None,
                 disk_controllers=None,
                 usb_controllers=None,
                 storage_policies=None,
                ):
        """
        :type  vm_name: :class:`str`
        :param vm_name: Name of the VM
        :type  os_type: :class:`str` or ``None``
        :param os_type: OS type of the VM
            A VM template is not required to specify an OS.
        :type  os_description: :class:`str` or ``None``
        :param os_description: OS description
            A VM template is not required to specify an OS.
        :type  cpu: :class:`Cpu` or ``None``
        :param cpu: CPU information of the VM
            A VM template is not required to specify a CPU.
        :type  memory: :class:`Memory` or ``None``
        :param memory: memory information of the VM
            A VM template is not required to specify memory.
        :type  disks: :class:`list` of :class:`Disk` or ``None``
        :param disks: All hard disks on the VM
            A VM template is not required to specify a list of disks.
        :type  nics: :class:`list` of :class:`Nic` or ``None``
        :param nics: All NICs on the VM
            A VM template is not required to specify a list of network
            interfaces.
        :type  video_cards: :class:`list` of :class:`VideoCard` or ``None``
        :param video_cards: Video cards of the VM
            A VM template is not required to specify a list of video cards.
        :type  drives: :class:`list` of :class:`Drive` or ``None``
        :param drives: CD / DVD drives of the VM
            A VM template is not required to specify a list of drives.
        :type  floppies: :class:`list` of :class:`Floppy` or ``None``
        :param floppies: floppy drives of the VM
            A VM template is not required to specify a list of floppy drives.
        :type  disk_controllers: :class:`list` of :class:`DiskController` or ``None``
        :param disk_controllers: Disk Controllers
            A VM template is not required to specify a list of disk
            controllers.
        :type  usb_controllers: :class:`list` of :class:`USBController` or ``None``
        :param usb_controllers: USB Controllers
            A VM template is not required to specify a list of USB controllers.
        :type  storage_policies: :class:`list` of :class:`com.vmware.content.type.ovf.policy_client.StoragePolicy` or ``None``
        :param storage_policies: Storage policies of the VM.
            A VM template is not required to specify a list of storage
            policies.
        """
        self.vm_name = vm_name
        self.os_type = os_type
        self.os_description = os_description
        self.cpu = cpu
        self.memory = memory
        self.disks = disks
        self.nics = nics
        self.video_cards = video_cards
        self.drives = drives
        self.floppies = floppies
        self.disk_controllers = disk_controllers
        self.usb_controllers = usb_controllers
        self.storage_policies = storage_policies
        VapiStruct.__init__(self)


VmTemplate._set_binding_type(type.StructType(
    'com.vmware.content.type.ovf.vm_template', {
        'vm_name': type.StringType(),
        'os_type': type.OptionalType(type.StringType()),
        'os_description': type.OptionalType(type.StringType()),
        'cpu': type.OptionalType(type.ReferenceType(__name__, 'Cpu')),
        'memory': type.OptionalType(type.ReferenceType(__name__, 'Memory')),
        'disks': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Disk'))),
        'nics': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Nic'))),
        'video_cards': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VideoCard'))),
        'drives': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Drive'))),
        'floppies': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Floppy'))),
        'disk_controllers': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'DiskController'))),
        'usb_controllers': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'USBController'))),
        'storage_policies': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.content.type.ovf.policy_client', 'StoragePolicy'))),
    },
    VmTemplate,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'policy': 'com.vmware.content.type.ovf.policy_client.StubFactory',
    }

