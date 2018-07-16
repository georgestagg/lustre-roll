Summary: lustre-client roll
Name: roll-lustre-client
Version: 7.0.0_2.10.3
Release: 1
License: University of California
Vendor: Rocks Clusters
Group: System Environment/Base
Source: roll-lustre-client-7.0.0_2.10.3.tar.gz
Buildroot: /state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.buildroot
Prefix: /export/profile
Buildarch: noarch


%description
XML files for the lustre-client roll

%package kickstart
Summary: lustre-client roll
Group: System Environment/Base
%description kickstart
XML files for the lustre-client roll
%prep
%setup
%build
printf "\n\n\n### build ###\n\n\n"
BUILDROOT=/state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.buildroot make -f /state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.spec.mk build
%install
printf "\n\n\n### install ###\n\n\n"
BUILDROOT=/state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.buildroot make -f /state/partition1/src/roll/lustre-client-2.10.3/roll-lustre-client.spec.mk install
%files kickstart
/export/profile

