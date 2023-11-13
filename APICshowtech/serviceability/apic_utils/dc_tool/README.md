## Installing Custom Device Connector Image
```
dc-tool install -H <apic_hostname> -i <dc_binary_path>
```

`apic_hostname` is bdsol-aci51-apic1.cisco.com for our APIC (or whatever you have aliased it as). 
Assuming you are in the root of the  **hanks** repo and you have built your device connector, 
`dc_binary_path` will be `.build/apic_dc`

## Reverting Device Connector
```
dc-tool revert -H <apic_hostname>
```
This will restore the device connector to the version originally deployed with the APIC platform software.

## Confirming a Custom Install
1. When building hanks, add a custom version string as below. (Note that `GO_SA_TARGET= ` is used to skip static analysis, speeding up build times for development.)
```
GO_SA_TARGET= SW_VERSION_STRING=<my_custom_version> make
```


2. After installing the device connector, head to the APIC GUI and navigate to `System -> System Settings -> Nexus Cloud Connectivity`. 
In the lower left corner of the "Device Connector" box, you should see your custom version string if your install was successful. 


## Note
This has only been used with our development APIC running 5.2(7f), there is **no guarantee** that this will 
work with other APICs.

## Requirements
- sshpass