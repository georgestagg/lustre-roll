# This file is called from the generated spec file.
# It can also be used to debug rpm building.
# 	make -f roll-lustre-client.spec.mk build|install

ifndef __RULES_MK
build:
	make ROOT=/state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.buildroot build

install:
	make ROOT=/state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.buildroot install
endif
