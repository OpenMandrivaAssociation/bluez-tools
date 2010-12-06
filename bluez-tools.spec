%define name    bluez-tools
%define version 0.1.38
%define rev	662e

Name:           %{name}
Summary:        Command line tools for bluez (bluetooth stack for Linux)
Version:        %{version}
Release:        %mkrel -c %rev 2 
Source0:        %{name}-%{version}-%{rev}.tar.gz
URL:            http://code.google.com/p/bluez-tools
License:	GPLv2
Group:          System/Kernel and hardware
Requires:	bluez >= 4.69
Requires:	obexd >= 0.30
BuildRequires:	dbus
BuildRequires:	libdbus-1_3
BuildRequires:	libdbus-1-devel
BuildRequires:	libdbus-glib-1_2
BuildRequires:	libdbus-glib-1_2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is a GSoC'10 project to implement a new command line tools for 
bluez (bluetooth stack for linux). The project implemented in C and 
uses the D-Bus interface of bluez.

%prep
%setup -q -a 0 -n %{name}-%{version}-%{rev}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean 
rm -rf %{buildroot} 

%files 
%defattr(-,root,root) 
%doc README NEWS COPYING AUTHORS 
%{_bindir}/*
%{_mandir}/man1/bt-adapter.1*
%{_mandir}/man1/bt-agent.1*
%{_mandir}/man1/bt-audio.1*
%{_mandir}/man1/bt-device.1*
%{_mandir}/man1/bt-input.1*
%{_mandir}/man1/bt-monitor.1*
%{_mandir}/man1/bt-network.1*
%{_mandir}/man1/bt-obex.1*
%{_mandir}/man1/bt-serial.1*

