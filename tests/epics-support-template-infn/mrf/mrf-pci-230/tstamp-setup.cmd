#############################################
## Time propagation setup on EVG IOC       ##
#############################################

## Send out event 125 when receiving external trigger on input 2
dbpf("$(PREFIX)-$(EVG):TrigEvt0-EvtCode-SP","125")
dbpf("$(PREFIX)-$(EVG):UnivInp2-TrigSrc0-SP","Set")

## Disable Time-I record on EVR0, obsolete
dbpf("$(PREFIX)-$(EVR):Time-I.DISV", "0")
