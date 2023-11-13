"""
Parameter file
"""

logger = None
apiClient = None
cloud = None
adminHandle = None
downloadURL = None
downloadDir = None
adminUsers = None
topogen = None

platformParam = {
    "platformparams": {
        "ClassId": "techsupportmanagement.NiaParam",
        "ObjectType": "techsupportmanagement.NiaParam",
        "CollectionLevel": 1,
        "UpgradeLogs": False,
        "Filename": "",
        "ForceFresh": True,
        "Pids": ["APIC"],
        "SerialNumbers":
            ["FDO22181DH3"],
    },

}

platformParamSingle = {
    "platformparams": {
        "ClassId": "techsupportmanagement.NiaParam",
        "ObjectType": "techsupportmanagement.NiaParam",
        "CollectionLevel": 1,
        "UpgradeLogs": False,
        "Filename": "",
        "ForceFresh": True,
        "Pids": ["APIC"],
        "SerialNumbers":
            ["FDO22181DH3"],
    },
    'ExpectedReturn': 1,

}

platformParamMulti = {
    "platformparams": {
        "ClassId": "techsupportmanagement.NiaParam",
        "ObjectType": "techsupportmanagement.NiaParam",
        "CollectionLevel": 1,
        "UpgradeLogs": False,
        "Filename": "",
        "ForceFresh": True,
        "Pids": ["APIC"],
        "SerialNumbers":
            ["FDO22181DH3", "FDO20530A7T", "FDO20530AA3", "FDO212817NV"],
    },
    "ExpectedReturn": 4,
}

platformParamDup = {
    "platformparams": {
        "ClassId": "techsupportmanagement.NiaParam",
        "ObjectType": "techsupportmanagement.NiaParam",
        "CollectionLevel": 1,
        "UpgradeLogs": False,
        "Filename": "",
        "ForceFresh": True,
        "Pids": ["APIC"],
        "SerialNumbers":
            ["FDO22181DH3", "FDO22181DH3"],
    },
    "ExpectedReturn": 1,
}
